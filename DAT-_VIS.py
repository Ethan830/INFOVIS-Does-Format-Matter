import io
import math
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.tri as mtri
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch
from matplotlib.colors import LinearSegmentedColormap, ListedColormap


# =========================================================
# GLOBAL SETTINGS
# =========================================================

IEEE_DOUBLE_COLUMN_WIDTH_IN = 7.0
DEFAULT_DPI = 300

# Okabe-Ito colorblind-safe palette
OKABE_ITO = [
    "#E69F00",  # orange
    "#56B4E9",  # sky blue
    "#009E73",  # bluish green
    "#D55E00",  # vermillion
    "#CC79A7",  # reddish purple
    "#0072B2",  # blue
    "#F0E442",  # yellow
    "#000000",  # black
]

OKABE_ITO_SEQ = LinearSegmentedColormap.from_list(
    "okabe_ito_seq",
    [
        "#0072B2",
        "#56B4E9",
        "#009E73",
        "#E69F00",
        "#D55E00",
    ]
)

OKABE_ITO_DIV = LinearSegmentedColormap.from_list(
    "okabe_ito_div",
    [
        "#0072B2",
        "#56B4E9",
        "#F7F7F7",
        "#E69F00",
        "#D55E00",
    ]
)

OKABE_ITO_LISTED = ListedColormap(OKABE_ITO)

MARKERS = ["o", "s", "^", "D", "v", "P", "X", "*"]

plt.rcParams.update({
    "figure.dpi": DEFAULT_DPI,
    "savefig.dpi": DEFAULT_DPI,
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.labelsize": 10,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "grid.linestyle": "--",
    "legend.frameon": False,
})
STATE_CENTROIDS = {
    "NSW": (147.0, -32.0),
    "VIC": (144.0, -37.0),
    "QLD": (145.0, -22.0),
    "SA": (135.0, -30.0),
    "WA": (122.0, -25.0),
    "TAS": (146.7, -42.0),
    "ACT": (149.1, -35.5),
    "NT": (133.0, -19.0),
}
''' 
STATE_CENTROIDS = {
    "AL": (-86.8, 32.8), "AK": (-152.0, 64.0), "AZ": (-111.7, 34.2), "AR": (-92.4, 35.1),
    "CA": (-119.5, 37.2), "CO": (-105.5, 39.0), "CT": (-72.7, 41.6), "DE": (-75.5, 39.0),
    "FL": (-81.7, 27.8), "GA": (-83.5, 32.7), "HI": (-157.5, 20.9), "ID": (-114.5, 44.2),
    "IL": (-89.2, 40.0), "IN": (-86.1, 40.0), "IA": (-93.5, 42.1), "KS": (-98.3, 38.5),
    "KY": (-84.7, 37.6), "LA": (-91.9, 31.0), "ME": (-69.2, 45.3), "MD": (-76.7, 39.0),
    "MA": (-71.8, 42.3), "MI": (-84.6, 44.4), "MN": (-94.3, 46.3), "MS": (-89.7, 32.7),
    "MO": (-92.6, 38.5), "MT": (-110.0, 46.9), "NE": (-99.8, 41.5), "NV": (-116.9, 39.3),
    "NH": (-71.6, 43.7), "NJ": (-74.7, 40.1), "NM": (-106.1, 34.5), "NY": (-75.0, 42.9),
    "NC": (-79.4, 35.5), "ND": (-100.5, 47.5), "OH": (-82.8, 40.3), "OK": (-97.5, 35.6),
    "OR": (-120.5, 43.9), "PA": (-77.8, 40.9), "RI": (-71.5, 41.7), "SC": (-80.9, 33.8),
    "SD": (-100.2, 44.4), "TN": (-86.4, 35.8), "TX": (-99.3, 31.4), "UT": (-111.7, 39.3),
    "VT": (-72.7, 44.1), "VA": (-78.7, 37.5), "WA": (-120.7, 47.4), "WV": (-80.6, 38.6),
    "WI": (-89.9, 44.6), "WY": (-107.6, 43.0), "DC": (-77.0, 38.9)
}
'''

# =========================================================
# COMMON PARSING
# =========================================================

def parse_metadata_and_dataframe(csv_path: str) -> Tuple[Dict[str, str], pd.DataFrame]:
    metadata: Dict[str, str] = {}
    table_lines: List[str] = []

    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        for line in f:
            stripped = line.strip()
            if stripped.startswith("#"):
                m = re.match(r"#\s*([^:]+)\s*:\s*(.*)", stripped)
                if m:
                    metadata[m.group(1).strip()] = m.group(2).strip()
            elif stripped:
                table_lines.append(line)

    if not table_lines:
        raise ValueError("No CSV table found after metadata block.")

    table_text = "".join(table_lines)
    df = pd.read_csv(io.StringIO(table_text), skipinitialspace=True)
    df.columns = [str(c).strip() for c in df.columns]

    return metadata, df


def get_required(meta: Dict[str, str], key: str) -> str:
    value = meta.get(key, "").strip()
    if not value:
        raise ValueError(f"Missing required metadata field: {key}")
    return value


def parse_coord(value) -> float:
    s = str(value).strip()
    m = re.search(r"(-?\d+(?:\.\d+)?)", s)
    if not m:
        raise ValueError(f"Could not parse numeric coordinate from '{value}'")
    num = float(m.group(1))

    s_upper = s.upper()
    if "W" in s_upper or "S" in s_upper:
        num = -abs(num)
    elif "E" in s_upper or "N" in s_upper:
        num = abs(num)

    return num


def to_numeric_series(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series.astype(str).str.replace(",", "", regex=False), errors="coerce")


def maybe_numeric_series(series: pd.Series) -> bool:
    try:
        pd.to_numeric(series.astype(str).str.replace(",", "", regex=False))
        return True
    except Exception:
        return False


def parse_vector_cell(cell: str) -> Dict[str, float]:
    out: Dict[str, float] = {}
    text = str(cell).strip().replace("\n", ";")
    for part in text.split(";"):
        part = part.strip()
        if ":" not in part:
            continue
        k, v = part.split(":", 1)
        try:
            out[k.strip()] = float(v.strip())
        except ValueError:
            pass
    return out


# =========================================================
# FIGURE HELPERS
# =========================================================

def figure_height_for(table_type: str) -> float:
    return {
        "time_series_matrix": 3.8,
        "spatial_grid": 4.6,
        "record_table": 4.8,
        "vector_grid": 5.2,
        "vector_long": 5.0,
    }.get(table_type, 4.5)


def make_figure(table_type: str):
    fig, ax = plt.subplots(
        figsize=(IEEE_DOUBLE_COLUMN_WIDTH_IN, figure_height_for(table_type)),
        dpi=DEFAULT_DPI
    )
    return fig, ax


def set_title(ax, title: str, subtitle: Optional[str] = None):
    if subtitle:
        ax.set_title(f"{title}\n{subtitle}")
    else:
        ax.set_title(title)


def output_name(input_csv: str, output_png: Optional[str]) -> str:
    if output_png:
        return output_png
    return str(Path(input_csv).with_suffix(".png"))


def finalize_and_save(fig, out_png: str, bottom: float = 0.16, left: float = 0.10, right: float = 0.98, top: float = 0.90):
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom)
    fig.savefig(out_png, dpi=DEFAULT_DPI)
    plt.close(fig)


# =========================================================
# RENDERERS
# =========================================================

def render_vis_time_series_matrix(meta: Dict[str, str], df: pd.DataFrame, out_png: str) -> None:
    title = get_required(meta, "title")
    subject = get_required(meta, "subject")
    unit = get_required(meta, "unit")
    index_column = get_required(meta, "index_column")

    fig, ax = make_figure("time_series_matrix")
    x = df[index_column].astype(str).tolist()
    series_cols = [c for c in df.columns if c != index_column]

    for i, col in enumerate(series_cols):
        y = to_numeric_series(df[col])
        ax.plot(
            x, y,
            label=col,
            color=OKABE_ITO[i % len(OKABE_ITO)],
            marker=MARKERS[i % len(MARKERS)],
            linewidth=1.8,
            markersize=5.5
        )

    ax.set_xlabel(index_column)
    ax.set_ylabel(f"{subject.title()} ({unit})")
    set_title(ax, title)
    ax.tick_params(axis="x", rotation=45)

    ncol = min(len(series_cols), 5)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.28), ncol=ncol, frameon=False)

    finalize_and_save(fig, out_png, bottom=0.28, left=0.10, right=0.98, top=0.88)


def render_vis_spatial_grid(meta: Dict[str, str], df: pd.DataFrame, out_png: str) -> None:
    title = get_required(meta, "title")
    subject = get_required(meta, "subject")
    unit = get_required(meta, "unit")
    row_axis_name = get_required(meta, "row_axis_name")
    column_axis_name = get_required(meta, "column_axis_name")

    fig, ax = make_figure("spatial_grid")

    y_labels = df.iloc[:, 0].tolist()
    x_labels = list(df.columns[1:])

    y = np.array([parse_coord(v) for v in y_labels], dtype=float)
    x = np.array([parse_coord(v) for v in x_labels], dtype=float)
    z = df.iloc[:, 1:].apply(to_numeric_series, axis=0).to_numpy(dtype=float)

    y_order = np.argsort(y)
    x_order = np.argsort(x)
    y = y[y_order]
    x = x[x_order]
    z = z[y_order][:, x_order]

    X, Y = np.meshgrid(x, y)

    cf = ax.contourf(X, Y, z, levels=14, cmap=OKABE_ITO_SEQ)
    ax.contour(X, Y, z, levels=8, colors="k", linewidths=0.6, alpha=0.4)

    set_title(ax, title)
    ax.set_xlabel(column_axis_name.replace("_", " ").title())
    ax.set_ylabel(row_axis_name.replace("_", " ").title())

    cbar = fig.colorbar(cf, ax=ax, pad=0.02)
    cbar.set_label(f"{subject.title()} ({unit})")

    finalize_and_save(fig, out_png, bottom=0.14, left=0.10, right=0.90, top=0.90)


def detect_record_vis_type(meta: Dict[str, str], df: pd.DataFrame) -> str:
    if meta.get("vis_type"):
        return meta["vis_type"].strip()

    cols = set(df.columns)
    has_lat = any("lat" in c.lower() for c in df.columns)
    has_lon = any("lon" in c.lower() for c in df.columns)
    has_bearing = any("bearing" in c.lower() for c in df.columns)
    has_duration = any("duration" in c.lower() for c in df.columns)
    has_volume = any("passengers" in c.lower() or "volume" in c.lower() for c in df.columns)

    if {"Origin State", "Top Destination", "Migration Volume"}.issubset(cols):
        return "state_migration_flow"
    if has_lat and has_lon and has_bearing and has_duration and has_volume:
        return "airport_vector"
    if has_lat and has_lon:
        return "geo_point_contour"

    return "record_dotplot"


def _lat_lon_columns(df: pd.DataFrame) -> Tuple[str, str]:
    lat_col = next((c for c in df.columns if "lat" in c.lower()), None)
    lon_col = next((c for c in df.columns if "lon" in c.lower()), None)
    if not lat_col or not lon_col:
        raise ValueError("Could not identify latitude/longitude columns.")
    return lat_col, lon_col


def _main_numeric_measure(df: pd.DataFrame, exclude: List[str]) -> str:
    candidates = []
    for col in df.columns:
        if col in exclude:
            continue
        s = to_numeric_series(df[col])
        if s.notna().sum() == len(df):
            candidates.append(col)

    if not candidates:
        raise ValueError("Could not identify a numeric measure column.")

    preference = [
        c for c in candidates
        if any(key in c.lower() for key in ["noise", "pm2.5", "aqi", "value", "temperature", "elevation"])
    ]
    return preference[0] if preference else candidates[0]


def render_record_geo_contour(meta: Dict[str, str], df: pd.DataFrame, out_png: str) -> None:
    title = get_required(meta, "title")
    subject = get_required(meta, "subject")
    unit = get_required(meta, "unit")
    record_label = get_required(meta, "record_label")

    lat_col, lon_col = _lat_lon_columns(df)
    measure_col = meta.get("measure_column", "").strip() or _main_numeric_measure(df, [record_label, lat_col, lon_col])

    fig, ax = make_figure("record_table")

    lats = df[lat_col].map(parse_coord).to_numpy()
    lons = df[lon_col].map(parse_coord).to_numpy()
    values = to_numeric_series(df[measure_col]).to_numpy()
    labels = df[record_label].astype(str).tolist()

    triang = mtri.Triangulation(lons, lats)

    cf = ax.tricontourf(triang, values, levels=12, cmap=OKABE_ITO_SEQ)
    ax.tricontour(triang, values, levels=8, colors="k", linewidths=0.5, alpha=0.4)
    ax.scatter(lons, lats, s=22, c="black", edgecolors="white", linewidths=0.4, zorder=3)

    for x, y, label in zip(lons, lats, labels):
        ax.annotate(
            label, (x, y), xytext=(-4, -4), textcoords="offset points",
            fontsize=8, weight="bold",
            bbox=dict(boxstyle="round,pad=0.15", facecolor="white", edgecolor="none", alpha=0.7)
        )

    set_title(ax, title)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    cbar = fig.colorbar(cf, ax=ax, pad=0.02)
    cbar.set_label(f"{subject.title()} ({unit})")

    finalize_and_save(fig, out_png, bottom=0.14, left=0.10, right=0.90, top=0.90)


def render_record_airport_vectors(meta: Dict[str, str], df: pd.DataFrame, out_png: str) -> None:
    import matplotlib.ticker as mticker

    def parse_airport_longitude(value) -> float:
        s = str(value).strip()
        m = re.search(r"(-?\d+(?:\.\d+)?)", s)
        if not m:
            raise ValueError(f"Could not parse longitude from '{value}'")
        num = float(m.group(1))
        if num < 0:
            return num
        s_upper = s.upper()
        if "W" in s_upper:
            return -abs(num)
        if "E" in s_upper:
            return abs(num)
        return num

    def parse_airport_latitude(value) -> float:
        s = str(value).strip()
        m = re.search(r"(-?\d+(?:\.\d+)?)", s)
        if not m:
            raise ValueError(f"Could not parse latitude from '{value}'")
        num = float(m.group(1))
        if num < 0:
            return num
        s_upper = s.upper()
        if "S" in s_upper:
            return -abs(num)
        if "N" in s_upper:
            return abs(num)
        return num

    title = get_required(meta, "title")
    record_label = get_required(meta, "record_label")

    lat_col, lon_col = _lat_lon_columns(df)
    duration_col = next(
        c for c in df.columns
        if "duration" in c.lower() or "route length" in c.lower() or "length" in c.lower()
    )

    bearing_col = next(
        c for c in df.columns
        if "bearing" in c.lower()
    )

    volume_col = next(
        c for c in df.columns
        if "passengers" in c.lower() or "volume" in c.lower() or "cargo" in c.lower()
    )
    fig, ax = plt.subplots(figsize=(7.0, 4.8), dpi=DEFAULT_DPI)

    lats = df[lat_col].map(parse_airport_latitude).to_numpy()
    lons = df[lon_col].map(parse_airport_longitude).to_numpy()
    duration = to_numeric_series(df[duration_col]).to_numpy()
    bearing = to_numeric_series(
        df[bearing_col].astype(str).str.replace("°", "", regex=False)
    ).to_numpy()
    volume = to_numeric_series(df[volume_col]).to_numpy()
    labels = df[record_label].astype(str).tolist()

    dur_scale = 4.35 / max(duration.max(), 1)
    vol_min, vol_max = volume.min(), volume.max()

    label_offsets = {
        "YVR": (4, 6), "SEA": (4, -8), "PDX": (4, 4), "SFO": (4, -10),
        "LAX": (4, -10), "PHX": (4, 4), "YYC": (4, 6), "YWG": (4, 10),
        "FAR": (4, 6), "MSP": (4, 6), "ORD": (4, 6), "DTW": (4, -10),
        "YYZ": (4, 6), "YUL": (4, 6), "BOS": (4, 6), "EWR": (4, -10),
        "PHL": (6, -8), "IAD": (4, -10), "ATL": (4, -10), "MIA": (4, -10),
        "MCO": (4, 6), "DFW": (4, 6), "IAH": (4, -10), "DEN": (4, 6),
        "BOI": (4, 6), "SLC": (4, 6), "BZN": (4, 6), "JAC": (4, 6),
        "OMA": (4, 6), "MCI": (4, 6), "STL": (4, 6), "BNA": (4, 6),
        "CLT": (4, 6), "MSY": (4, -10), "ELP": (4, 6),
    }

    label_offsets.update({
        "Vancouver (YVR)": (-3, 4),
        "Seattle (SEA)": (-4, 2),
        "Portland (PDX)": (-4, 2),
        "San Francisco (SFO)": (-3, -4),
        "Los Angeles (LAX)": (-5, -4),
        "Phoenix (PHX)": (1, -3),
        "El Paso (ELP)": (1, -4),
        "Calgary (YYC)": (4, 6),
        "Bozeman (BZN)": (4, 6),
        "Boise (BOI)": (0, 5),
        "Jackson (JAC)": (4, 8),
        "Salt Lake City (SLC)": (-4, -1),
        "Denver (DEN)": (2, 5),
        "Omaha (OMA)": (0, 4),
        "Kansas City (MCI)": (2, 4),
        "St. Louis (STL)": (3, -1),
        "Nashville (BNA)": (4, 3),
        "Atlanta (ATL)": (4, -3),
        "Charlotte (CLT)": (4, 3),
        "Orlando (MCO)": (4, 1),
        "Miami (MIA)": (4, -2),
        "New Orleans (MSY)": (0, -6),
        "Houston (IAH)": (-3, -4),
        "Dallas/Fort Worth (DFW)": (4, 8),
        "Minneapolis (MSP)": (4, 0),
        "Fargo (FAR)": (4, 0),
        "Winnipeg (YWG)": (4, 0),
        "Chicago (ORD)": (0, 5),
        "Detroit (DTW)": (4, -2),
        "Toronto (YYZ)": (4, 2),
        "Montreal (YUL)": (4, 3),
        "Boston (BOS)": (4, 3),
        "Newark (EWR)": (4, -1),
        "Philadelphia (PHL)": (4, -1),
        "Washington (IAD)": (4, -1),
    })

    for lon, lat, dur, bear, vol, label in zip(lons, lats, duration, bearing, volume, labels):
        theta = math.radians(90 - bear)
        dx = math.cos(theta) * dur * dur_scale
        dy = math.sin(theta) * dur * dur_scale

        lw = 0.8 + 3.0 * ((vol - vol_min) / (vol_max - vol_min + 1e-9))

        start_x = lon + 0.08 * dx
        start_y = lat + 0.08 * dy
        end_x = lon + dx
        end_y = lat + dy

        arrow = FancyArrowPatch(
            (start_x, start_y),
            (end_x, end_y),
            arrowstyle="-|>",
            mutation_scale=6,
            linewidth=lw,
            color="black",
            alpha=0.9,
            zorder=3
        )
        ax.add_patch(arrow)

        ax.scatter(
            lon, lat,
            s=18,
            color="black",
            edgecolor="white",
            linewidth=0.5,
            zorder=4
        )

        lx, ly = label_offsets.get(label, (4, 4))
        ha = "left" if lx >= 0 else "right"
        va = "bottom" if ly >= 0 else "top"

        ax.annotate(
            label,
            (lon, lat),
            xytext=(lx, ly),
            textcoords="offset points",
            fontsize=4.5,
            weight="bold",
            ha=ha,
            va=va,
            annotation_clip=False,
            zorder=10,
            bbox=dict(
                boxstyle="round,pad=0.10",
                facecolor="white",
                edgecolor="none",
                alpha=0.85
            )
        )

    set_title(ax, title)
    ax.set_xlabel("Longitude (°W)")
    ax.set_ylabel("Latitude")

    ax.set_xlim(-5, 35) #changed when map at different region of world
    ax.xaxis.set_major_formatter(
        mticker.FuncFormatter(lambda x, pos: f"{abs(int(round(x)))}")
    )

    ax.set_ylim(min(lats) - 2, max(lats) + 2)
    ax.grid(True, linestyle="--", alpha=0.25)

    handles = [
        Line2D([0], [0], color="black", linewidth=0.8, marker=">", markevery=[1],
               label="Shorter avg. flight duration"),
        Line2D([0], [0], color="black", linewidth=3.0, marker=">", markevery=[1],
               label="Longer avg. flight duration"),
        Line2D([0], [0], color="black", linewidth=0.8,
               label="Lower annual passengers"),
        Line2D([0], [0], color="black", linewidth=3.0,
               label="Higher annual passengers"),
    ]

    ax.legend(
        handles=handles,
        loc="upper center",
        bbox_to_anchor=(0.5, -0.28),
        ncol=2,
        frameon=False
    )

    fig.subplots_adjust(left=0.09, right=0.98, top=0.88, bottom=0.26)
    fig.savefig(out_png, dpi=DEFAULT_DPI)
    plt.close(fig)


def _draw_curved_arrow(ax, start, end, color, lw, alpha=0.8):
    x1, y1 = start
    x2, y2 = end
    rad = 0.15 if x2 >= x1 else -0.15
    patch = FancyArrowPatch(
        (x1, y1), (x2, y2),
        connectionstyle=f"arc3,rad={rad}",
        arrowstyle="-|>",
        mutation_scale=8,
        linewidth=lw,
        color=color,
        alpha=alpha
    )
    ax.add_patch(patch)


def render_record_state_migration(meta: Dict[str, str], df: pd.DataFrame, out_png: str) -> None:
    title = get_required(meta, "title")

    fig, ax = make_figure("record_table")

    vols = to_numeric_series(df["Migration Volume"]).to_numpy()
    vmin, vmax = vols.min(), vols.max()

    for abbr, (lon, lat) in STATE_CENTROIDS.items():
        ax.text(lon, lat, abbr, fontsize=5, ha="center", va="center", color="0.35")

    for _, row in df.iterrows():
        origin = str(row["Origin State"]).strip()
        dest = str(row["Top Destination"]).strip()
        vol = float(str(row["Migration Volume"]).replace(",", ""))

        if origin not in STATE_CENTROIDS or dest not in STATE_CENTROIDS:
            continue

        start = STATE_CENTROIDS[origin]
        end = STATE_CENTROIDS[dest]
        t = (vol - vmin) / (vmax - vmin + 1e-9)
        color = OKABE_ITO_SEQ(t)
        lw = 0.6 + 2.4 * t
        _draw_curved_arrow(ax, start, end, color=color, lw=lw)

    set_title(ax, title)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_xlim(120, 150) # change when displaying deifferent region of map
    ax.set_ylim(-45, -15) # change when displaying deifferent region of map

    sm = plt.cm.ScalarMappable(cmap=OKABE_ITO_SEQ, norm=plt.Normalize(vmin=vmin, vmax=vmax))
    cbar = fig.colorbar(sm, ax=ax, pad=0.02)
    cbar.set_label("Migration Volume")

    finalize_and_save(fig, out_png, bottom=0.14, left=0.10, right=0.90, top=0.90)


def render_record_dotplot(meta: Dict[str, str], df: pd.DataFrame, out_png: str) -> None:
    title = get_required(meta, "title")
    record_label = get_required(meta, "record_label")

    numeric_cols = [c for c in df.columns if c != record_label and maybe_numeric_series(df[c])]
    if not numeric_cols:
        raise ValueError("No numeric columns available for generic record dot plot.")
    measure_col = numeric_cols[0]

    fig, ax = make_figure("record_table")

    labels = df[record_label].astype(str).tolist()
    values = to_numeric_series(df[measure_col]).to_numpy()
    y = np.arange(len(labels))

    ax.hlines(y, 0, values, color=OKABE_ITO[1], linewidth=1.2)
    ax.plot(values, y, "o", color=OKABE_ITO[0], markersize=5)

    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.set_xlabel(measure_col)
    set_title(ax, title)

    finalize_and_save(fig, out_png, bottom=0.14, left=0.18, right=0.98, top=0.90)


def render_vis_record_table(meta: Dict[str, str], df: pd.DataFrame, out_png: str) -> None:
    vis_type = detect_record_vis_type(meta, df)

    if vis_type == "geo_point_contour":
        render_record_geo_contour(meta, df, out_png)
    elif vis_type == "airport_vector":
        render_record_airport_vectors(meta, df, out_png)
    elif vis_type == "state_migration_flow":
        render_record_state_migration(meta, df, out_png)
    else:
        render_record_dotplot(meta, df, out_png)


def render_vis_vector_grid(meta: Dict[str, str], df: pd.DataFrame, out_png: str) -> None:
    title = get_required(meta, "title")
    unit = get_required(meta, "unit")

    row_label = df.columns[0]
    x_labels = list(df.columns[1:])
    y_labels = df[row_label].tolist()

    x = np.array([parse_coord(v) for v in x_labels], dtype=float)
    y = np.array([parse_coord(v) for v in y_labels], dtype=float)

    U = np.zeros((len(y), len(x)))
    V = np.zeros((len(y), len(x)))
    SPD = np.zeros((len(y), len(x)))

    for i in range(len(y)):
        for j, col in enumerate(x_labels):
            parsed = parse_vector_cell(df.iloc[i][col])
            U[i, j] = parsed.get("U", np.nan)
            V[i, j] = parsed.get("V", np.nan)
            SPD[i, j] = parsed.get("Spd", np.nan)

    y_order = np.argsort(y)
    x_order = np.argsort(x)
    x = x[x_order]
    y = y[y_order]
    U = U[y_order][:, x_order]
    V = V[y_order][:, x_order]
    SPD = SPD[y_order][:, x_order]

    X, Y = np.meshgrid(x, y)

    fig, ax = make_figure("vector_grid")

    cf = ax.contourf(X, Y, SPD, levels=14, cmap=OKABE_ITO_SEQ)
    ax.quiver(
        X, Y, U, V, SPD,
        cmap=OKABE_ITO_SEQ,
        angles="xy",
        scale_units="xy",
        scale=None,
        width=0.003,
        edgecolors="black",
        linewidths=0.1
    )

    set_title(ax, title)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    cbar = fig.colorbar(cf, ax=ax, pad=0.02)
    cbar.set_label(f"Wind Speed ({unit})")

    finalize_and_save(fig, out_png, bottom=0.14, left=0.10, right=0.90, top=0.90)


def render_vis_vector_long(meta: Dict[str, str], df: pd.DataFrame, out_png: str) -> None:
    title = get_required(meta, "title")
    unit = get_required(meta, "unit")

    x = df["Longitude"].map(parse_coord).to_numpy()
    y = df["Latitude"].map(parse_coord).to_numpy()
    U = to_numeric_series(df["U"]).to_numpy()
    V = to_numeric_series(df["V"]).to_numpy()

    if "Spd" in df.columns:
        SPD = to_numeric_series(df["Spd"]).to_numpy()
    else:
        SPD = np.sqrt(U**2 + V**2)

    fig, ax = make_figure("vector_long")

    triang = mtri.Triangulation(x, y)
    cf = ax.tricontourf(triang, SPD, levels=14, cmap=OKABE_ITO_SEQ)
    ax.quiver(
        x, y, U, V, SPD,
        cmap=OKABE_ITO_SEQ,
        angles="xy",
        scale_units="xy",
        scale=None,
        width=0.003
    )

    set_title(ax, title)
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

    cbar = fig.colorbar(cf, ax=ax, pad=0.02)
    cbar.set_label(f"Wind Speed ({unit})")

    finalize_and_save(fig, out_png, bottom=0.14, left=0.10, right=0.90, top=0.90)


def render_visualization(csv_path: str, output_png: Optional[str] = None) -> str:
    meta, df = parse_metadata_and_dataframe(csv_path)
    table_type = get_required(meta, "table_type")
    out_png = output_name(csv_path, output_png)

    if table_type == "time_series_matrix":
        render_vis_time_series_matrix(meta, df, out_png)
    elif table_type == "spatial_grid":
        render_vis_spatial_grid(meta, df, out_png)
    elif table_type == "record_table":
        render_vis_record_table(meta, df, out_png)
    elif table_type == "vector_grid":
        render_vis_vector_grid(meta, df, out_png)
    elif table_type == "vector_long":
        render_vis_vector_long(meta, df, out_png)
    else:
        raise ValueError(f"Unsupported table_type: {table_type}")

    return out_png


# =========================================================
# CHANGE THESE TWO LINES
# =========================================================

INPUT_CSV = "DAT4j.csv"
OUTPUT_PNG = "VIS4j.png"


# =========================================================
# RUN
# =========================================================

png_path = render_visualization(INPUT_CSV, OUTPUT_PNG)
print(f"Saved figure to: {png_path}")

from IPython.display import Image, display
display(Image(filename=png_path))