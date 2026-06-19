"""Shared dataset + dark plotting style for the Types of Analytics charts.

Dev-only tooling (NOT served by the site). Regenerates every PNG embedded in
the visualization / diagnostic / predictive / prescriptive mini-series, so the
figures are reproducible and version-controlled.

Run a series script from the repo root, e.g.:
    python3 tools/charts/visualization.py

Every figure is seeded (numpy default_rng(42), sklearn random_state=42) and
saved to publications/images/analytics/ with the site's dark palette so the
charts blend into the dark theme.
"""
from __future__ import annotations

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# ── Output location ──────────────────────────────────────────────────────────
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(REPO_ROOT, "publications", "images", "analytics")
os.makedirs(OUT_DIR, exist_ok=True)

# ── Site palette (mirrors style.css tokens) ──────────────────────────────────
BG       = "#0e1422"   # --surface
PANEL    = "#111a2c"   # --surface-2
TEXT     = "#e7ecf6"   # --text
MUTED    = "#94a3bd"   # --text-muted
FAINT    = "#5d6b86"   # --text-faint
GRID     = "#1d2740"
ACCENT   = "#56b6ff"   # --accent (cyan)
PURPLE   = "#a78bfa"   # --purple
MINT     = "#4fd6a8"   # --mint
AMBER    = "#fbbf24"
ROSE     = "#fb7185"
# Ordered categorical cycle (colour-blind-friendly-ish, distinct hues)
CYCLE = [ACCENT, PURPLE, MINT, AMBER, ROSE]
# On-brand sequential colormap for heatmaps: deep navy -> cyan -> mint
CMAP = LinearSegmentedColormap.from_list("brand", ["#0b1a33", ACCENT, MINT])


def apply_style() -> None:
    """Set global rcParams so every figure matches the dark site theme."""
    plt.rcParams.update({
        "figure.facecolor": BG,
        "savefig.facecolor": BG,
        "axes.facecolor": BG,
        "axes.edgecolor": GRID,
        "axes.labelcolor": MUTED,
        "axes.titlecolor": TEXT,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
        "text.color": TEXT,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "font.size": 10,
        "legend.facecolor": PANEL,
        "legend.edgecolor": GRID,
        "legend.labelcolor": TEXT,
        "figure.titlesize": 13,
        "figure.titleweight": "bold",
        "axes.prop_cycle": plt.cycler(color=CYCLE),
    })


def save(fig, name: str) -> str:
    """Save a figure to publications/images/analytics/<name>.png."""
    path = os.path.join(OUT_DIR, f"{name}.png")
    fig.savefig(path, dpi=130, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    rel = os.path.relpath(path, REPO_ROOT)
    print(f"  wrote {rel}")
    return path


# ── Synthetic retail dataset (identical seed/logic to the descriptive notebook)
def raw_orders() -> pd.DataFrame:
    """Reproduce the raw, messy 20k-order retail dataset (seed 42)."""
    rng = np.random.default_rng(42)
    N = 20_000

    n_cust = 2_000
    ranks = np.arange(1, n_cust + 1)
    weights = 1 / ranks
    weights = weights / weights.sum()

    order_date = pd.to_datetime("2022-01-01") + pd.to_timedelta(
        rng.integers(0, 730, N), unit="D")
    month_num = order_date.month
    season = np.select([month_num.isin([11, 12]), month_num.isin([1, 2])],
                       [1.8, 0.7], default=1.0)
    quantity = np.maximum(1, (rng.integers(1, 12, N) * season).round().astype(int))

    orders = pd.DataFrame({
        "order_id": np.arange(1, N + 1),
        "order_date": order_date,
        "region": rng.choice(["West", "East", "Central", "South"], N),
        "category": rng.choice(["Furniture", "Office", "Technology"], N),
        "segment": rng.choice(["Consumer", "Corporate", "Home Office"], N),
        "customer_id": rng.choice(ranks, size=N, p=weights),
        "quantity": quantity,
        "discount": rng.choice([0.0, 0.1, 0.2, 0.3], N, p=[0.5, 0.25, 0.15, 0.1]),
    })

    bulk = pd.DataFrame({
        "order_id": np.arange(N + 1, N + 31),
        "order_date": pd.to_datetime("2023-06-15"),
        "region": "Central", "category": "Technology", "segment": "Corporate",
        "customer_id": rng.integers(1, n_cust, 30),
        "quantity": rng.integers(60, 150, 30),
        "discount": 0.0,
    })
    orders = pd.concat([orders, bulk], ignore_index=True)

    # messiness for the cleaning step
    dupes = orders.sample(300, random_state=1)
    orders = pd.concat([orders, dupes], ignore_index=True)
    orders.loc[orders.sample(200, random_state=2).index, "region"] = " west "
    orders.loc[orders.sample(150, random_state=3).index, "discount"] = np.nan
    orders.loc[orders.sample(50, random_state=4).index, "quantity"] = 0
    return orders


def clean_orders() -> pd.DataFrame:
    """Analysis-ready orders: cleaned + derived sales/profit/month, sales > 0."""
    orders = raw_orders()
    orders = orders.drop_duplicates(subset="order_id", keep="first").copy()
    orders["region"] = orders["region"].str.strip().str.title()
    orders["discount"] = orders["discount"].fillna(0.0)
    orders = orders[orders["quantity"] > 0]

    price = {"Furniture": 180, "Office": 25, "Technology": 320}
    orders["unit_price"] = orders["category"].map(price)
    orders["sales"] = orders["quantity"] * orders["unit_price"] * (1 - orders["discount"])
    orders["profit"] = orders["sales"] * (0.30 - orders["discount"])
    orders["month"] = orders["order_date"].dt.to_period("M").dt.to_timestamp()
    orders = orders[orders["sales"] > 0]
    return orders.reset_index(drop=True)


def focused_orders() -> pd.DataFrame:
    """clean_orders() with extreme sales outliers trimmed (IQR rule).

    Mirrors the descriptive series' 'filtering' step: drops the handful of
    bulk B2B orders so teaching charts show the underlying relationships
    instead of being dominated by a few extreme points.
    """
    df = clean_orders()
    q1, q3 = df["sales"].quantile([0.25, 0.75])
    iqr = q3 - q1
    low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    return df[df["sales"].between(low, high)].reset_index(drop=True)


if __name__ == "__main__":
    df = clean_orders()
    print("clean:", df.shape)
    print("focused:", focused_orders().shape)
    print(df.head())
