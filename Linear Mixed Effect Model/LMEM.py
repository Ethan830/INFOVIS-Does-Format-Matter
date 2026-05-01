import pandas as pd
import statsmodels.formula.api as smf

# -----------------------------
# 1. Load CSV
# -----------------------------

file_path = "CS 441 Data Sheet - Linear mixed-effects model.csv"

df = pd.read_csv(file_path)

# -----------------------------
# 2. Required columns
# -----------------------------

required_cols = [
    "Row_Label",
    "Row_Brier",
    "Accuracy",
    "Modality",
    "Dataset_ID",
    "Visualization_Type",
    "Model"
]

missing_cols = [col for col in required_cols if col not in df.columns]

if missing_cols:
    raise ValueError(f"Missing required columns: {missing_cols}")

# -----------------------------
# 3. Convert numeric columns
# -----------------------------

df["Row_Brier_raw"] = df["Row_Brier"]
df["Accuracy_raw"] = df["Accuracy"]

df["Row_Brier"] = pd.to_numeric(df["Row_Brier"], errors="coerce")
df["Accuracy"] = pd.to_numeric(df["Accuracy"], errors="coerce")

# -----------------------------
# 4. Identify and drop bad rows
# -----------------------------

bad_rows = df[df[required_cols].isna().any(axis=1)].copy()
df_model = df.dropna(subset=required_cols).copy()

print("Rows in original data:", len(df))
print("Rows used in analysis:", len(df_model))
print("Rows omitted:", len(df) - len(df_model))

# -----------------------------
# 5. Clean categorical variables
# -----------------------------

df_model["Modality"] = df_model["Modality"].astype(str)
df_model["Model"] = df_model["Model"].astype(str)
df_model["Dataset_ID"] = df_model["Dataset_ID"].astype(str)
df_model["Visualization_Type"] = df_model["Visualization_Type"].astype(str)

type_map = {
    "1": "Line_Graph",
    "2": "Color_Map",
    "3": "Isoline",
    "4": "Arrow_Glyph"
}

df_model["Visualization_Type"] = df_model["Visualization_Type"].map(type_map)

# Drop invalid visualization-type rows, if any
df_model = df_model.dropna(subset=["Visualization_Type"]).copy()

# -----------------------------
# 6. Convert model result to table
# -----------------------------

def result_to_dataframe(result, model_name, model_type):
    params = result.params
    conf = result.conf_int()

    return pd.DataFrame({
        "Model_Name": model_name,
        "Model_Type": model_type,
        "Term": params.index,
        "Estimate": params.values,
        "Std_Error": result.bse.values,
        "z_or_t": result.tvalues.values,
        "p_value": result.pvalues.values,
        "CI_Lower": conf[0].values,
        "CI_Upper": conf[1].values
    })

# -----------------------------
# 7. Run model
# -----------------------------

def run_analysis(outcome, formula_rhs, data):
    formula = f"{outcome} ~ {formula_rhs}"

    print("\n" + "=" * 60)
    print(f"Running analysis for: {outcome}")
    print("=" * 60)

    try:
        mixed_model = smf.mixedlm(
            formula,
            data=data,
            groups=data["Dataset_ID"]
        )

        mixed_result = mixed_model.fit(
            method="powell",
            reml=False,
            maxiter=1000,
            disp=False
        )

        print("\nMixed-effects model succeeded.")
        print(mixed_result.summary())

        result_df = result_to_dataframe(
            mixed_result,
            model_name=outcome,
            model_type="Mixed-effects model"
        )

        return mixed_result, result_df, "Mixed-effects model"

    except Exception as e:
        print("\nMixed-effects model failed. Continuing with OLS + clustered SEs.")
        print("Reason:", e)

        ols_result = smf.ols(
            formula,
            data=data
        ).fit(
            cov_type="cluster",
            cov_kwds={"groups": data["Dataset_ID"]}
        )

        print("\nOLS with dataset-clustered standard errors:")
        print(ols_result.summary())

        result_df = result_to_dataframe(
            ols_result,
            model_name=outcome,
            model_type="OLS with dataset-clustered SEs"
        )

        return ols_result, result_df, "OLS with dataset-clustered SEs"

# -----------------------------
# 8. Run Brier and Accuracy models
# -----------------------------

rhs = "C(Modality) + C(Visualization_Type) + C(Model)"

brier_result, brier_table, brier_model_type = run_analysis(
    outcome="Row_Brier",
    formula_rhs=rhs,
    data=df_model
)

accuracy_result, accuracy_table, accuracy_model_type = run_analysis(
    outcome="Accuracy",
    formula_rhs=rhs,
    data=df_model
)

# -----------------------------
# 9. Create summary tables
# -----------------------------

run_summary = pd.DataFrame({
    "Metric": [
        "Rows in original data",
        "Rows used in analysis",
        "Rows omitted",
        "Brier model type used",
        "Accuracy model type used"
    ],
    "Value": [
        len(df),
        len(df_model),
        len(df) - len(df_model),
        brier_model_type,
        accuracy_model_type
    ]
})

group_summary = (
    df_model
    .groupby(["Modality", "Visualization_Type", "Model"], as_index=False)
    .agg(
        Mean_Row_Brier=("Row_Brier", "mean"),
        SD_Row_Brier=("Row_Brier", "std"),
        N_Row_Brier=("Row_Brier", "count"),
        Mean_Accuracy=("Accuracy", "mean"),
        SD_Accuracy=("Accuracy", "std"),
        N_Accuracy=("Accuracy", "count")
    )
)

# -----------------------------
# 10. Save outputs as CSV files
# -----------------------------

run_summary.to_csv("run_summary.csv", index=False)
brier_table.to_csv("brier_model_results.csv", index=False)
accuracy_table.to_csv("accuracy_model_results.csv", index=False)
group_summary.to_csv("group_summary.csv", index=False)
df_model.to_csv("cleaned_data_used_in_analysis.csv", index=False)

if len(bad_rows) > 0:
    bad_rows.to_csv("omitted_rows.csv", index=False)
else:
    pd.DataFrame({"Message": ["No bad rows omitted."]}).to_csv(
        "omitted_rows.csv",
        index=False
    )

print("\nSaved CSV outputs:")
print("run_summary.csv")
print("brier_model_results.csv")
print("accuracy_model_results.csv")
print("group_summary.csv")
print("omitted_rows.csv")
print("cleaned_data_used_in_analysis.csv")