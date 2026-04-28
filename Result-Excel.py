import pandas as pd

input_files = {
    "Claude": "CLAUDE_results_1-4.csv",
    "GPT": "GPTresults1-4.csv",
    "Gemini": "GEMINI_results_1-4.csv",
}

output_excel = "confidence_pivot_ordered_1A_to_4J.xlsx"

llm_order = ["Claude", "GPT", "Gemini"]

modality_order = [
    ("Vis", "rendered image"),
    ("Dat", "data table"),
    ("Par", "paragraph"),
]

dataset_order = [
    f"{number}{letter}"
    for number in range(1, 5)
    for letter in "ABCDEFGHIJ"
]

question_order = [
    "Q1",
    "ECR_1a",
    "Q2",
    "ECR_1b",
    "Q3",
    "ECR_1c",
]

def normalize_columns(df):
    rename_map = {
        "Dataset ID": "Dataset_ID",
        "DatasetID": "Dataset_ID",
        "QuestionID": "Question_ID",
        "Question ID": "Question_ID",
        "Raw Answer": "Raw_Answer",
    }

    df = df.rename(columns=rename_map)

    required_cols = [
        "Dataset_ID",
        "LLM",
        "Modality",
        "Question_ID",
        "Accuracy",
        "Confidence",
        "Raw_Answer",
    ]

    missing = [col for col in required_cols if col not in df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return df


def clean_dataset_id(value):
    value = str(value).strip()

    for prefix in ["Vis-", "Dat-", "Dar-", "Par-"]:
        if value.startswith(prefix):
            return value.replace(prefix, "", 1)

    return value


def normalize_modality(value):
    value = str(value).strip().lower()

    modality_map = {
        "vis": "rendered image",
        "visual": "rendered image",
        "image": "rendered image",
        "rendered image": "rendered image",

        "dat": "data table",
        "dar": "data table",
        "data": "data table",
        "table": "data table",
        "data table": "data table",

        "par": "paragraph",
        "paragraph": "paragraph",
        "text": "paragraph",
    }

    return modality_map.get(value, value)


def normalize_confidence(value):
    if pd.isna(value):
        return pd.NA

    value = str(value).strip()

    if value == "":
        return pd.NA

    value = value.replace("%", "").strip()

    try:
        number = float(value)
    except ValueError:
        return pd.NA

    if number > 1:
        number = number / 100

    return number


all_dfs = []

for llm_name, file_path in input_files.items():
    df = pd.read_csv(file_path)
    df = normalize_columns(df)

    df["LLM"] = llm_name
    df["Dataset_ID"] = df["Dataset_ID"].apply(clean_dataset_id)
    df["Modality"] = df["Modality"].apply(normalize_modality)
    df["Confidence"] = df["Confidence"].apply(normalize_confidence)

    df = df[df["Question_ID"].isin(question_order)]

    all_dfs.append(df)

combined = pd.concat(all_dfs, ignore_index=True)

pivot = combined.pivot_table(
    index=["Dataset_ID", "LLM", "Modality"],
    columns="Question_ID",
    values="Confidence",
    aggfunc="first"
).reset_index()

pivot.columns.name = None

ordered_rows = []

for dataset in dataset_order:
    for llm in llm_order:
        for short_modality, full_modality in modality_order:
            ordered_rows.append({
                "Row_Label": f"{short_modality}-{dataset} {llm}",
                "Dataset_ID": dataset,
                "LLM": llm,
                "Modality": full_modality,
            })

order_df = pd.DataFrame(ordered_rows)

final_df = order_df.merge(
    pivot,
    on=["Dataset_ID", "LLM", "Modality"],
    how="left"
)

confidence_cols = []

for q in question_order:
    if q in final_df.columns:
        new_name = f"Confidence_{q}"
        final_df = final_df.rename(columns={q: new_name})
        confidence_cols.append(new_name)

final_df = final_df[
    ["Row_Label", "Dataset_ID", "LLM", "Modality"] + confidence_cols
]

missing_records = []

for _, row in final_df.iterrows():
    for col in confidence_cols:
        if pd.isna(row[col]):
            missing_records.append({
                "Row_Label": row["Row_Label"],
                "Dataset_ID": row["Dataset_ID"],
                "LLM": row["LLM"],
                "Modality": row["Modality"],
                "Missing_Column": col,
            })

missing_df = pd.DataFrame(missing_records)

summary_df = pd.DataFrame({
    "Metric": [
        "Number of datasets",
        "Number of LLMs",
        "Number of modalities",
        "Expected total rows",
        "Actual total rows",
        "Number of confidence columns",
        "Missing confidence cells",
    ],
    "Value": [
        len(dataset_order),
        len(llm_order),
        len(modality_order),
        len(dataset_order) * len(llm_order) * len(modality_order),
        len(final_df),
        len(confidence_cols),
        len(missing_df),
    ]
})

with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
    final_df.to_excel(writer, sheet_name="Confidence Pivot", index=False)
    missing_df.to_excel(writer, sheet_name="Missing Confidence", index=False)
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
    combined.to_excel(writer, sheet_name="Raw Inputs", index=False)

    ws = writer.sheets["Confidence Pivot"]

    for col_idx, col_name in enumerate(final_df.columns, start=1):
        if col_name.startswith("Confidence_"):
            for row_idx in range(2, len(final_df) + 2):
                ws.cell(row=row_idx, column=col_idx).number_format = "0%"

print(f"Saved Excel file to: {output_excel}")
