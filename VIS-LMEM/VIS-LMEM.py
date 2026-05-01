import pandas as pd
import numpy as np
import itertools
import statsmodels.formula.api as smf
from statsmodels.stats.multitest import multipletests
from patsy import build_design_matrices

# ============================================================
# Input / output
# ============================================================

input_file = "CS 441 Data Sheet.csv"

output_long_csv = "vis_only_ecr_long_from_original.csv"
output_means_csv = "vis_only_ecr_viztype_means.csv"
output_pairwise_csv = "vis_only_ecr_viztype_pairwise_tests.csv"

# ============================================================
# Helper functions
# ============================================================

def make_unique_columns(cols):
    """
    Make duplicate column names unique:
    Row_Label, Row_Label -> Row_Label, Row_Label.1
    """
    counts = {}
    new_cols = []

    for col in cols:
        col = str(col).strip()

        if col not in counts:
            counts[col] = 0
            new_cols.append(col)
        else:
            counts[col] += 1
            new_cols.append(f"{col}.{counts[col]}")

    return new_cols


def load_original_sheet(file_path):
    """
    Loads the original CS 441 sheet even if the first row is blank
    or pandas reads columns as Unnamed.
    """
    raw = pd.read_csv(file_path, header=None)

    header_row_idx = None

    for i in range(len(raw)):
        row_values = raw.iloc[i].astype(str).str.strip().tolist()

        if "Row_Label" in row_values and "Brier-ECR1" in row_values:
            header_row_idx = i
            break

    if header_row_idx is None:
        raise ValueError(
            "Could not find a header row containing both 'Row_Label' and "
            "'Brier-ECR1'. Check the CSV export."
        )

    df = raw.iloc[header_row_idx + 1:].copy()
    df.columns = make_unique_columns(raw.iloc[header_row_idx].tolist())

    df = df.dropna(axis=1, how="all")

    return df


def build_design_matrix(model, new_data):
    """
    Builds a model-consistent design matrix for pairwise contrasts.
    """
    design_info = model.model.data.design_info

    return build_design_matrices(
        [design_info],
        new_data,
        return_type="dataframe"
    )[0]


# ============================================================
# 1. Load original data sheet
# ============================================================

df = load_original_sheet(input_file)

print("Detected columns:")
print(list(df.columns))

# ============================================================
# 2. Identify row-label and ECR Brier columns
# ============================================================

# Prefer the right-side Row_Label if duplicated.
row_label_candidates = [
    col for col in df.columns
    if str(col).startswith("Row_Label")
]

if not row_label_candidates:
    raise ValueError("Could not find Row_Label column.")

if "Row_Label.1" in row_label_candidates:
    row_label_col = "Row_Label.1"
else:
    row_label_col = row_label_candidates[0]

required_ecr_cols = ["Brier-ECR1", "Brier-ECR2", "Brier-ECR3"]

missing = [col for col in required_ecr_cols if col not in df.columns]

if missing:
    raise ValueError(
        f"Missing required ECR Brier columns: {missing}\n"
        f"Available columns are:\n{list(df.columns)}"
    )

work = df[[row_label_col] + required_ecr_cols].copy()

work = work.rename(columns={
    row_label_col: "Row_Label",
    "Brier-ECR1": "Brier_ECR1",
    "Brier-ECR2": "Brier_ECR2",
    "Brier-ECR3": "Brier_ECR3",
})

# ============================================================
# 3. Extract metadata from Row_Label
# ============================================================

work["Row_Label"] = work["Row_Label"].astype(str).str.strip()

# Keep only valid row labels such as Vis-1A Claude
work = work[
    work["Row_Label"].str.contains(r"^(Vis|Dat|Par)-\d[A-J]\s+(Claude|GPT|Gemini)$",
                                   regex=True,
                                   na=False)
].copy()

work["Modality"] = work["Row_Label"].str.extract(r"^(Vis|Dat|Par)")
work["Dataset_ID"] = work["Row_Label"].str.extract(r"-(\d[A-J])")
work["Visualization_Code"] = work["Dataset_ID"].str.extract(r"^(\d)")
work["Model"] = work["Row_Label"].str.extract(r"(Claude|GPT|Gemini)$")

viz_map = {
    "1": "Line_Graph",
    "2": "Color_Map",
    "3": "Isoline",
    "4": "Arrow_Glyph",
}

work["Visualization_Type"] = work["Visualization_Code"].map(viz_map)

# ============================================================
# 4. Filter to VIS-only input modality
# ============================================================

vis = work[work["Modality"] == "Vis"].copy()

for col in ["Brier_ECR1", "Brier_ECR2", "Brier_ECR3"]:
    vis[col] = pd.to_numeric(vis[col], errors="coerce")

# ============================================================
# 5. Reshape ECR items into long format
# ============================================================

long_df = vis.melt(
    id_vars=[
        "Row_Label",
        "Dataset_ID",
        "Visualization_Type",
        "Model",
    ],
    value_vars=[
        "Brier_ECR1",
        "Brier_ECR2",
        "Brier_ECR3",
    ],
    var_name="ECR_Item",
    value_name="ECR_Brier"
)

long_df["ECR_Item"] = long_df["ECR_Item"].replace({
    "Brier_ECR1": "ECR_1",
    "Brier_ECR2": "ECR_2",
    "Brier_ECR3": "ECR_3",
})

# Drop bad rows
required_cols = [
    "Dataset_ID",
    "Visualization_Type",
    "Model",
    "ECR_Item",
    "ECR_Brier",
]

long_df["ECR_Brier"] = pd.to_numeric(long_df["ECR_Brier"], errors="coerce")

bad_rows = long_df[long_df[required_cols].isna().any(axis=1)].copy()
analysis_df = long_df.dropna(subset=required_cols).copy()

print("\nRows after VIS filtering and ECR reshape:", len(long_df))
print("Rows used in analysis:", len(analysis_df))
print("Rows omitted:", len(bad_rows))

# ============================================================
# 6. Set categorical ordering
# ============================================================

viz_order = ["Line_Graph", "Color_Map", "Isoline", "Arrow_Glyph"]
model_order = ["Claude", "GPT", "Gemini"]
ecr_order = ["ECR_1", "ECR_2", "ECR_3"]

analysis_df["Visualization_Type"] = pd.Categorical(
    analysis_df["Visualization_Type"],
    categories=viz_order,
    ordered=False
)

analysis_df["Model"] = pd.Categorical(
    analysis_df["Model"],
    categories=model_order,
    ordered=False
)

analysis_df["ECR_Item"] = pd.Categorical(
    analysis_df["ECR_Item"],
    categories=ecr_order,
    ordered=False
)

analysis_df = analysis_df.dropna(
    subset=["Visualization_Type", "Model", "ECR_Item"]
).copy()

analysis_df.to_csv(output_long_csv, index=False)

# ============================================================
# 7. Inference model
# ============================================================
# Goal:
# Determine whether a specific visualization type produces weaker
# hallucination resistance under VIS-only input.
#
# Outcome:
# ECR_Brier
#
# Predictors:
# Visualization_Type + Model + ECR_Item
#
# Standard errors:
# Clustered by Dataset_ID

formula = "ECR_Brier ~ C(Visualization_Type) + C(Model) + C(ECR_Item)"

model = smf.ols(
    formula,
    data=analysis_df
).fit(
    cov_type="cluster",
    cov_kwds={"groups": analysis_df["Dataset_ID"]}
)

print("\nModel summary:")
print(model.summary())

# ============================================================
# 8. Adjusted means by visualization type
# ============================================================
# Adjusted means are averaged over all models and ECR items.

prediction_rows = []

for viz in viz_order:
    for model_name in model_order:
        for ecr_item in ecr_order:
            prediction_rows.append({
                "Visualization_Type": viz,
                "Model": model_name,
                "ECR_Item": ecr_item,
            })

pred_df = pd.DataFrame(prediction_rows)

pred_df["Visualization_Type"] = pd.Categorical(
    pred_df["Visualization_Type"],
    categories=viz_order,
    ordered=False
)

pred_df["Model"] = pd.Categorical(
    pred_df["Model"],
    categories=model_order,
    ordered=False
)

pred_df["ECR_Item"] = pd.Categorical(
    pred_df["ECR_Item"],
    categories=ecr_order,
    ordered=False
)

predictions = model.get_prediction(pred_df).summary_frame(alpha=0.05)

pred_df["Predicted_ECR_Brier"] = predictions["mean"]
pred_df["CI_Lower"] = predictions["mean_ci_lower"]
pred_df["CI_Upper"] = predictions["mean_ci_upper"]

adjusted_means = (
    pred_df
    .groupby("Visualization_Type", as_index=False, observed=False)
    .agg(
        Adjusted_Mean_ECR_Brier=("Predicted_ECR_Brier", "mean"),
        CI_Lower=("CI_Lower", "mean"),
        CI_Upper=("CI_Upper", "mean"),
    )
)

raw_means = (
    analysis_df
    .groupby("Visualization_Type", as_index=False, observed=False)
    .agg(
        Raw_Mean_ECR_Brier=("ECR_Brier", "mean"),
        Raw_SD_ECR_Brier=("ECR_Brier", "std"),
        N=("ECR_Brier", "count"),
    )
)

means = adjusted_means.merge(
    raw_means,
    on="Visualization_Type",
    how="left"
)

means = means.sort_values(
    "Adjusted_Mean_ECR_Brier",
    ascending=False
)

means.to_csv(output_means_csv, index=False)

print("\nAdjusted visualization-type means:")
print(means)

# ============================================================
# 9. Pairwise visualization-type tests
# ============================================================
# These test whether the worst visualization type is significantly
# worse than the others.

def make_prediction_grid(viz):
    rows = []

    for model_name in model_order:
        for ecr_item in ecr_order:
            rows.append({
                "Visualization_Type": viz,
                "Model": model_name,
                "ECR_Item": ecr_item,
            })

    grid = pd.DataFrame(rows)

    grid["Visualization_Type"] = pd.Categorical(
        grid["Visualization_Type"],
        categories=viz_order,
        ordered=False
    )

    grid["Model"] = pd.Categorical(
        grid["Model"],
        categories=model_order,
        ordered=False
    )

    grid["ECR_Item"] = pd.Categorical(
        grid["ECR_Item"],
        categories=ecr_order,
        ordered=False
    )

    return grid


design_by_viz = {}

for viz in viz_order:
    grid = make_prediction_grid(viz)
    design = build_design_matrix(model, grid)
    design_by_viz[viz] = np.asarray(design).mean(axis=0)

pairwise_results = []

for viz_a, viz_b in itertools.combinations(viz_order, 2):
    contrast = design_by_viz[viz_a] - design_by_viz[viz_b]

    test = model.t_test(contrast)

    estimate = float(np.asarray(test.effect).squeeze())
    se = float(np.asarray(test.sd).squeeze())
    t_value = float(np.asarray(test.tvalue).squeeze())
    p_value = float(np.asarray(test.pvalue).squeeze())

    pairwise_results.append({
        "Comparison": f"{viz_a} - {viz_b}",
        "Estimate_Difference": estimate,
        "Std_Error": se,
        "t_value": t_value,
        "p_value": p_value,
        "Direction": (
            f"{viz_a} has higher ECR Brier than {viz_b}"
            if estimate > 0
            else f"{viz_a} has lower ECR Brier than {viz_b}"
        )
    })

pairwise_df = pd.DataFrame(pairwise_results)

reject, p_adj, _, _ = multipletests(
    pairwise_df["p_value"],
    alpha=0.05,
    method="holm"
)

pairwise_df["p_value_holm"] = p_adj
pairwise_df["Significant_Holm_0.05"] = reject

pairwise_df.to_csv(output_pairwise_csv, index=False)

print("\nPairwise visualization-type tests:")
print(pairwise_df)

# ============================================================
# 10. Identify worst visualization type
# ============================================================

worst_viz = means.iloc[0]["Visualization_Type"]
worst_mean = means.iloc[0]["Adjusted_Mean_ECR_Brier"]

print("\nWorst visualization type by adjusted mean ECR Brier:")
print(f"{worst_viz}: {worst_mean:.4f}")

worst_tests = pairwise_df[
    pairwise_df["Comparison"].str.contains(str(worst_viz))
].copy()

print("\nPairwise tests involving the worst visualization type:")
print(worst_tests)

print("\nSaved files:")
print(output_long_csv)
print(output_means_csv)
print(output_pairwise_csv)