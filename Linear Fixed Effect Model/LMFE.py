import pandas as pd
import statsmodels.formula.api as smf

# ============================================================
# Input / output
# ============================================================

input_csv = "CS 441 LMEM-2 Input.csv"

output_model_results = "question_type_brier_model_results.csv"
output_long_data = "question_type_brier_long_data_used.csv"
output_summary = "question_type_brier_summary.csv"

# ============================================================
# Load CSV
# ============================================================

raw = pd.read_csv(input_csv)

# ============================================================
# Keep the relevant table only
# Based on your uploaded file:
#
# Column 0 = Visualization Type
# Column 1 = Group, e.g. Claude-1
# Column 2 = Q1
# Column 3 = ECR-1a
# Column 4 = Q2
# Column 5 = ECR-1b
# Column 6 = Q3
# Column 7 = ECR-1c
# Column 8 = ECR Average
# ============================================================

df = raw.iloc[1:, 0:9].copy()

df.columns = [
    "Visualization_Type",
    "Group",
    "Q1",
    "ECR_1a",
    "Q2",
    "ECR_1b",
    "Q3",
    "ECR_1c",
    "ECR_Average"
]

# Drop empty rows
df = df.dropna(subset=["Visualization_Type", "Group"]).copy()

# ============================================================
# Extract Model from Group
# Example:
# Claude-1 -> Claude
# GPT-2    -> GPT
# Gemini-3 -> Gemini
# ============================================================

df["Model"] = df["Group"].astype(str).str.extract(r"^(Claude|GPT|Gemini)")

# Normalize visualization type names
df["Visualization_Type"] = df["Visualization_Type"].replace({
    "Glyphs": "Arrow_Glyph",
    "Line Graph": "Line_Graph",
    "Color Map": "Color_Map",
    "Isolines": "Isoline"
})

# ============================================================
# Convert Brier columns to numeric
# ============================================================

brier_cols = [
    "Q1",
    "ECR_1a",
    "Q2",
    "ECR_1b",
    "Q3",
    "ECR_1c"
]

for col in brier_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ============================================================
# Reshape wide to long
# ============================================================

long_df = df.melt(
    id_vars=[
        "Visualization_Type",
        "Group",
        "Model"
    ],
    value_vars=brier_cols,
    var_name="Question_ID",
    value_name="Question_Brier"
)

# ============================================================
# Map question IDs to question type
# ============================================================

question_type_map = {
    "Q1": "Value_Retrieval",
    "Q2": "Trend_Detection",
    "Q3": "Outlier_Detection",
    "ECR_1a": "ECR",
    "ECR_1b": "ECR",
    "ECR_1c": "ECR"
}

long_df["Question_Type"] = long_df["Question_ID"].map(question_type_map)

# ============================================================
# Drop bad rows
# ============================================================

required_cols = [
    "Visualization_Type",
    "Group",
    "Model",
    "Question_ID",
    "Question_Type",
    "Question_Brier"
]

bad_rows = long_df[long_df[required_cols].isna().any(axis=1)].copy()
model_df = long_df.dropna(subset=required_cols).copy()

print("Rows in aggregated input:", len(df))
print("Rows after reshaping:", len(long_df))
print("Rows used in model:", len(model_df))
print("Rows omitted:", len(long_df) - len(model_df))

if len(bad_rows) > 0:
    bad_rows.to_csv("question_type_brier_omitted_rows.csv", index=False)

# ============================================================
# Set reference categories
#
# Baseline:
# Question_Type = Value_Retrieval
# Visualization_Type = Arrow_Glyph
# Model = Claude
# ============================================================

model_df["Question_Type"] = pd.Categorical(
    model_df["Question_Type"],
    categories=[
        "Value_Retrieval",
        "Trend_Detection",
        "Outlier_Detection",
        "ECR"
    ],
    ordered=False
)

model_df["Visualization_Type"] = pd.Categorical(
    model_df["Visualization_Type"],
    categories=[
        "Arrow_Glyph",
        "Color_Map",
        "Isoline",
        "Line_Graph"
    ],
    ordered=False
)

model_df["Model"] = pd.Categorical(
    model_df["Model"],
    categories=[
        "Claude",
        "GPT",
        "Gemini"
    ],
    ordered=False
)

# ============================================================
# Run model
# ============================================================
# This is not a mixed-effects model because this aggregated input
# no longer contains dataset IDs for a random intercept.
# ============================================================

formula = (
    "Question_Brier ~ "
    "C(Question_Type) + "
    "C(Visualization_Type) + "
    "C(Model)"
)

result = smf.ols(
    formula,
    data=model_df
).fit()

print(result.summary())

# ============================================================
# Save model results
# ============================================================

conf = result.conf_int()

results_table = pd.DataFrame({
    "Model_Type": "OLS on aggregated question-type Brier scores",
    "Term": result.params.index,
    "Estimate": result.params.values,
    "Std_Error": result.bse.values,
    "z_or_t": result.tvalues.values,
    "p_value": result.pvalues.values,
    "CI_Lower": conf[0].values,
    "CI_Upper": conf[1].values,
})

results_table.to_csv(output_model_results, index=False)

# ============================================================
# Save descriptive summaries
# ============================================================

summary = (
    model_df
    .groupby("Question_Type", as_index=False)
    .agg(
        Mean_Question_Brier=("Question_Brier", "mean"),
        SD_Question_Brier=("Question_Brier", "std"),
        N=("Question_Brier", "count")
    )
)

summary_by_type_model = (
    model_df
    .groupby(["Question_Type", "Visualization_Type", "Model"], as_index=False)
    .agg(
        Mean_Question_Brier=("Question_Brier", "mean"),
        SD_Question_Brier=("Question_Brier", "std"),
        N=("Question_Brier", "count")
    )
)

summary.to_csv(output_summary, index=False)
summary_by_type_model.to_csv(
    "question_type_brier_by_type_model_summary.csv",
    index=False
)

model_df.to_csv(output_long_data, index=False)

print("\nSaved outputs:")
print(output_model_results)
print(output_summary)
print("question_type_brier_by_type_model_summary.csv")
print(output_long_data)