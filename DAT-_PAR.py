import csv
import re
from pathlib import Path
from typing import Dict, List, Tuple


def parse_metadata_and_table(csv_path: str) -> Tuple[Dict[str, str], List[Dict[str, str]], List[str]]:
    """
    Reads a CSV file with leading metadata lines in the format:
    # key: value

    Returns:
        metadata: dict
        rows: list of dict rows
        headers: list of column names
    """
    metadata = {}
    table_lines = []

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("#"):
                match = re.match(r"#\s*([^:]+)\s*:\s*(.*)", stripped)
                if match:
                    key = match.group(1).strip()
                    value = match.group(2).strip()
                    metadata[key] = value
            elif stripped:
                table_lines.append(line)

    if not table_lines:
        raise ValueError("No CSV table found after metadata block.")

    reader = csv.DictReader(table_lines)
    rows = list(reader)

    if not reader.fieldnames:
        raise ValueError("Could not detect CSV header row.")

    headers = [h.strip() for h in reader.fieldnames]

    if not rows:
        raise ValueError("No data rows found in the CSV.")

    return metadata, rows, headers


def format_number(value: str) -> str:
    value = str(value).strip()
    if value == "":
        return "missing"

    cleaned = value.replace(",", "")
    try:
        num = float(cleaned)
        if num.is_integer():
            return str(int(num))
        return f"{num:.2f}".rstrip("0").rstrip(".")
    except ValueError:
        return value


def join_list(items: List[str]) -> str:
    items = [str(x) for x in items if str(x).strip() != ""]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} and {items[1]}"
    return ", ".join(items[:-1]) + f", and {items[-1]}"


def get_required(metadata: Dict[str, str], key: str) -> str:
    if key not in metadata or not metadata[key].strip():
        raise ValueError(f"Missing required metadata field: {key}")
    return metadata[key].strip()


def render_time_series_matrix(metadata: Dict[str, str], rows: List[Dict[str, str]], headers: List[str]) -> str:
    title = get_required(metadata, "title")
    subject = get_required(metadata, "subject")
    unit = get_required(metadata, "unit")
    index_column = get_required(metadata, "index_column")
    entity_type = metadata.get("entity_type", "entities")

    entities = [h for h in headers if h != index_column]
    index_values = [format_number(row[index_column]) for row in rows]

    parts = []
    parts.append(
        f"The dataset titled {title} records {subject} for {len(entities)} {entity_type} — "
        f"{join_list(entities)} — across {len(rows)} indexed observations: {join_list(index_values)}, "
        f"with values measured in {unit}."
    )

    for i, row in enumerate(rows):
        idx = format_number(row[index_column])
        values = [format_number(row[e]) for e in entities]

        if i == 0:
            opener = f"In {idx}"
        elif i == len(rows) - 1:
            opener = f"In {idx}"
        elif i % 2 == 1:
            opener = f"By {idx}"
        else:
            opener = f"In {idx}"

        parts.append(
            f"{opener}, the recorded {subject} values were {join_list(values)} for "
            f"{join_list(entities)} respectively."
        )

    return " ".join(parts)


def render_spatial_grid(metadata: Dict[str, str], rows: List[Dict[str, str]], headers: List[str]) -> str:
    title = get_required(metadata, "title")
    subject = get_required(metadata, "subject")
    unit = get_required(metadata, "unit")
    row_axis_name = get_required(metadata, "row_axis_name")
    column_axis_name = get_required(metadata, "column_axis_name")

    row_label = headers[0]
    column_labels = headers[1:]

    row_values = [row[row_label].strip() for row in rows]

    parts = []
    parts.append(
        f"The dataset titled {title} presents {subject} on a spatial grid, with rows representing "
        f"{row_axis_name} and columns representing {column_axis_name}. The values are measured in {unit}. "
        f"The row coordinates are {join_list(row_values)}, and the column coordinates are {join_list(column_labels)}."
    )

    for row in rows:
        r = row[row_label].strip()
        cell_values = [format_number(row[c]) for c in column_labels]
        parts.append(
            f"At {row_axis_name} {r}, the recorded {subject} values across {column_axis_name} positions "
            f"{join_list(column_labels)} were {join_list(cell_values)} respectively."
        )

    return " ".join(parts)


def render_record_table(metadata: Dict[str, str], rows: List[Dict[str, str]], headers: List[str]) -> str:
    title = get_required(metadata, "title")
    subject = get_required(metadata, "subject")
    unit = get_required(metadata, "unit")
    record_label = get_required(metadata, "record_label")

    if record_label not in headers:
        raise ValueError(f"record_label '{record_label}' is not a column in the CSV.")

    attribute_columns = [h for h in headers if h != record_label]

    parts = []
    parts.append(
        f"The dataset titled {title} records {subject} for {len(rows)} entries, with values reported in {unit}. "
        f"Each record is identified by {record_label} and described using the attributes "
        f"{join_list(attribute_columns)}."
    )

    for row in rows:
        label = row[record_label].strip()
        attrs = [f"{col} = {format_number(row[col])}" for col in attribute_columns]
        parts.append(f"For {label}, the recorded attributes were {join_list(attrs)}.")

    return " ".join(parts)


def parse_vector_cell(cell: str) -> Dict[str, str]:
    """
    Parses cells like:
    'U:3.8;V:0.9;Spd:3.9'
    """
    result = {}
    for part in str(cell).split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            result[k.strip()] = v.strip()
    return result


def render_vector_grid(metadata: Dict[str, str], rows: List[Dict[str, str]], headers: List[str]) -> str:
    title = get_required(metadata, "title")
    subject = get_required(metadata, "subject")
    unit = get_required(metadata, "unit")
    row_axis_name = get_required(metadata, "row_axis_name")
    column_axis_name = get_required(metadata, "column_axis_name")
    cell_components = get_required(metadata, "cell_components").split(",")

    row_label = headers[0]
    column_labels = headers[1:]
    components = [c.strip() for c in cell_components]

    parts = []
    parts.append(
        f"The dataset titled {title} presents a grid of {subject} values, with rows representing {row_axis_name} "
        f"and columns representing {column_axis_name}. Each cell contains the components "
        f"{join_list(components)}, reported in {unit}."
    )

    for row in rows:
        r = row[row_label].strip()
        cell_descriptions = []
        for col in column_labels:
            parsed = parse_vector_cell(row[col])
            comp_text = ", ".join(
                f"{comp} = {format_number(parsed.get(comp, 'missing'))}" for comp in components
            )
            cell_descriptions.append(f"at {column_axis_name} {col}, {comp_text}")
        parts.append(f"At {row_axis_name} {r}, the recorded vector values were {join_list(cell_descriptions)}.")

    return " ".join(parts)


def render_vector_long(metadata: Dict[str, str], rows: List[Dict[str, str]], headers: List[str]) -> str:
    title = get_required(metadata, "title")
    subject = get_required(metadata, "subject")
    unit = get_required(metadata, "unit")
    components = [c.strip() for c in get_required(metadata, "components").split(",")]

    if "Latitude" not in headers or "Longitude" not in headers:
        raise ValueError("vector_long requires 'Latitude' and 'Longitude' columns.")

    parts = []
    parts.append(
        f"The dataset titled {title} records {subject} in long format, with each row corresponding to a coordinate pair "
        f"defined by Latitude and Longitude. The measured components are {join_list(components)}, reported in {unit}."
    )

    for row in rows:
        lat = row["Latitude"].strip()
        lon = row["Longitude"].strip()
        comp_text = [f"{c} = {format_number(row.get(c, 'missing'))}" for c in components]
        parts.append(
            f"At Latitude {lat} and Longitude {lon}, the recorded values were {join_list(comp_text)}."
        )

    return " ".join(parts)


def render_paragraph(metadata: Dict[str, str], rows: List[Dict[str, str]], headers: List[str]) -> str:
    table_type = get_required(metadata, "table_type")

    renderers = {
        "time_series_matrix": render_time_series_matrix,
        "spatial_grid": render_spatial_grid,
        "record_table": render_record_table,
        "vector_grid": render_vector_grid,
        "vector_long": render_vector_long,
    }

    if table_type not in renderers:
        raise ValueError(
            f"Unsupported table_type '{table_type}'. Supported types: {', '.join(renderers.keys())}"
        )

    return renderers[table_type](metadata, rows, headers)


def csv_to_txt_paragraph(csv_path: str, txt_path: str = None) -> str:
    metadata, rows, headers = parse_metadata_and_table(csv_path)
    paragraph = render_paragraph(metadata, rows, headers)

    if txt_path is None:
        txt_path = str(Path(csv_path).with_suffix(".txt"))

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(paragraph)

    return paragraph


if __name__ == "__main__":
    input_csv = "4c.csv"   #change this for different files
    output_txt = "PAR4c.txt"

    try:
        paragraph = csv_to_txt_paragraph(input_csv, output_txt)
        print(f"Paragraph written to: {output_txt}\n")
        print(paragraph)
    except Exception as e:
        print("Error:", e)