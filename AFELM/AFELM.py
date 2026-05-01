import pandas as pd
import statsmodels.formula.api as smf

# ============================================================
# Input / output files
# ============================================================

input_file = "CS 441 LMEM-2 Input.csv"

output_long_csv = "question_type_x_vistype_long_input.csv"
output_results_csv = "question_type_x_vistype_model_results.csv"
output_summary_csv = "question_type_x_vistype_summary.csv"

# ============================================================
# 1. Load the aggregated input table
# ============================================================

raw = pd.read_csv(input_file)

# Your CSV has an extra first row containing repeated headers.
# Drop rows where the group column is just "Group" or blank.
raw = raw.rename(columns={
    raw.columns[0]: "Visualization_Label",
    raw.columns[1]: "Group",
    raw.columns[2]: "Q1",
    raw.columns[3]: "ECR_1a",
    raw.columns[4]: "Q2",
    raw.columns[5]: "ECR_1b",
    raw.columns[6]: "Q3",
    raw.columns[7]: "ECR_1c",
    raw.columns[8]: "ECR_Average",
})

raw = raw[
    raw["Group"].notna() &
    (raw["Group"].astype(str).str.strip().str.lower() != "group")
].copy()

# Keep only the columns needed for this model
wide = raw[
    [
        "Visualization_Label",
        "Group",
        "Q1",
        "ECR_1a",
        "Q2",
        "ECR_1b",
        "Q3",
        "ECR_1c",
        "ECR_Average",
    ]
].copy()

# ============================================================
# 2. Extract Model and Visualization Type
# ============================================================

wide["Group"] = wide["Group"].astype(str).str.strip()

# Group looks like Claude-1, GPT-2, Gemini-4
wide["Model"] = wide["Group"].str.extract(r"^(Claude|GPT|Gemini)")
wide["Viz_Code"] = wide["Group"].str.extract(r"-(\d)$")

viz_map = {
    "1": "Line_Graph",
    "2": "Color_Map",
    "3": "Isoline",
    "4": "Arrow_Glyph",
}

wide["Visualization_Type"] = wide["Viz_Code"].map(viz_map)

# ============================================================
# 3. Convert question columns to numeric
# ============================================================

question_cols = [
    "Q1",
    "ECR_1a",
    "Q2",
    "ECR_1b",
    "Q3",
    "ECR_1c",
    "ECR_Average",
]

for col in question_cols:
    wide[col] = pd.to_numeric(wide[col], errors="coerce")

# ============================================================
# 4. Reshape wide table into long format
# ============================================================

long = wide.melt(
    id_vars=[
        "Visualization_Label",
        "Group",
        "Model",
        "Viz_Code",
        "Visualization_Type",
    ],
    value_vars=question_cols,
    var_name="Question_ID",
    value_name="Mean_Brier"
)

# ============================================================
# 5. Create Question_Type variable
# ============================================================

question_type_map = {
    "Q1": "Value_Retrieval",
    "Q2": "Trend_Detection",
    "Q3": "Outlier_Detection",
    "ECR_1a": "ECR",
    "ECR_1b": "ECR",
    "ECR_1c": "ECR",
    "ECR_Average": "ECR_Average",
}

long["Question_Type"] = long["Question_ID"].map(question_type_map)

# ============================================================
# 6. Choose whether to include ECR_Average
# ============================================================
# Usually, do NOT include ECR_Average in the model if ECR_1a,
# ECR_1b, and ECR_1c are already included. Otherwise, ECR is
# represented twice.
#
# Set this to True if you want to use ECR_Average instead of
# the three individual ECR columns.

USE_ECR_AVERAGE_ONLY = False

if USE_ECR_AVERAGE_ONLY:
    # Keep Q1, Q2, Q3, and ECR_Average only
    long = long[
        long["Question_ID"].isin(["Q1", "Q2", "Q3", "ECR_Average"])
    ].copy()

    long["Question_Type"] = long["Question_Type"].replace({
        "ECR_Average": "ECR"
    })

else:
    # Keep Q1, Q2, Q3, ECR_1a, ECR_1b, ECR_1c
    # Drop ECR_Average to avoid double-counting ECR
    long = long[
        long["Question_ID"] != "ECR_Average"
    ].copy()

# ============================================================
# 7. Drop bad rows
# ============================================================

required_cols = [
    "Model",
    "Visualization_Type",
    "Question_Type",
    "Mean_Brier",
]

bad_rows = long[long[required_cols].isna().any(axis=1)].copy()
analysis_df = long.dropna(subset=required_cols).copy()

print("Rows in long data:", len(long))
print("Rows used in analysis:", len(analysis_df))
print("Rows omitted:", len(long) - len(analysis_df))

if len(bad_rows) > 0:
    print("\nOmitted rows:")
    print(bad_rows)

# ============================================================
# 8. Set reference categories
# ============================================================
# Baseline:
# Question_Type = Value_Retrieval
# Visualization_Type = Arrow_Glyph
# Model = Claude

analysis_df["Question_Type"] = pd.Categorical(
    analysis_df["Question_Type"],
    categories=[
        "Value_Retrieval",
        "Trend_Detection",
        "Outlier_Detection",
        "ECR",
    ],
    ordered=False
)

analysis_df["Visualization_Type"] = pd.Categorical(
    analysis_df["Visualization_Type"],
    categories=[
        "Arrow_Glyph",
        "Color_Map",
        "Isoline",
        "Line_Graph",
    ],
    ordered=False
)

analysis_df["Model"] = pd.Categorical(
    analysis_df["Model"],
    categories=[
        "Claude",
        "GPT",
        "Gemini",
    ],
    ordered=False
)

# Drop rows made missing by category conversion, if any
analysis_df = analysis_df.dropna(
    subset=[
        "Question_Type",
        "Visualization_Type",
        "Model",
        "Mean_Brier",
    ]
).copy()

# Save the long-format data
analysis_df.to_csv(output_long_csv, index=False)

# ============================================================
# 9. Run aggregated fixed-effects model
# ============================================================
# This tests Question Type x Visualization Type interaction,
# controlling for Model.

formula = (
    "Mean_Brier ~ "
    "C(Question_Type) * C(Visualization_Type) + "
    "C(Model)"
)

model = smf.ols(
    formula,
    data=analysis_df
).fit()

# ============================================================
# 10. Save model results
# ============================================================

conf = model.conf_int()

results_table = pd.DataFrame({
    "Model_Type": "OLS on aggregated mean Brier scores",
    "Term": model.params.index,
    "Estimate": model.params.values,
    "Std_Error": model.bse.values,
    "z_or_t": model.tvalues.values,
    "p_value": model.pvalues.values,
    "CI_Lower": conf[0].values,
    "CI_Upper": conf[1].values,
})

results_table.to_csv(output_results_csv, index=False)

# ============================================================
# 11. Save group summary
# ============================================================

summary = (
    analysis_df
    .groupby(
        ["Question_Type", "Visualization_Type"],
        as_index=False
    )
    .agg(
        Mean_Brier=("Mean_Brier", "mean"),
        SD_Brier=("Mean_Brier", "std"),
        N=("Mean_Brier", "count")
    )
)

summary.to_csv(output_summary_csv, index=False)

# ============================================================
# 12. Print results
# ============================================================

print("\nModel results:")
print(results_table)

print("\nSaved files:")
print(output_long_csv)
print(output_results_csv)
print(output_summary_csv)