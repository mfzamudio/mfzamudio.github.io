"""Generate the charts for the Visualization Analytics mini-series.

    python3 tools/charts/visualization.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from _common import (focused_orders, apply_style, save,
                     ACCENT, PURPLE, MINT, AMBER, ROSE, MUTED, TEXT, GRID, BG, CMAP)

apply_style()
# Teaching charts use the outlier-trimmed dataset so relationships read clearly
orders = focused_orders()


# ── 1. Chart selection — one chart per question type ─────────────────────────
def bar_category():
    s = orders.groupby("category")["sales"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.barh(s.index, s.values / 1e6, color=ACCENT)
    ax.set_title("Comparison — sales by category")
    ax.set_xlabel("sales ($M)")
    ax.grid(axis="y", visible=False)
    save(fig, "viz-bar-category")


def line_monthly():
    m = orders.groupby("month")["sales"].sum() / 1e6
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.plot(m.index, m.values, color=ACCENT, linewidth=2)
    ax.fill_between(m.index, m.values, color=ACCENT, alpha=0.12)
    ax.set_title("Change over time — monthly sales")
    ax.set_ylabel("sales ($M)")
    save(fig, "viz-line-monthly")


def scatter_discount_profit():
    sample = orders.sample(2500, random_state=7)
    fig, ax = plt.subplots(figsize=(7, 3.8))
    ax.scatter(sample["discount"], sample["profit"], s=10, alpha=0.30,
               color=PURPLE, edgecolors="none")
    ax.axhline(0, color=ROSE, linewidth=1, linestyle="--", alpha=0.7)
    ax.set_title("Relationship — discount vs profit")
    ax.set_xlabel("discount"); ax.set_ylabel("profit ($)")
    save(fig, "viz-scatter-discount-profit")


def hist_sales():
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.hist(orders["sales"], bins=40, color=MINT, alpha=0.85)
    ax.set_title("Distribution — order sales")
    ax.set_xlabel("sales ($)"); ax.set_ylabel("orders")
    save(fig, "viz-hist-sales")


def heatmap_region_month():
    piv = (orders.assign(m=orders["order_date"].dt.month)
                 .pivot_table(index="region", columns="m",
                              values="sales", aggfunc="sum") / 1e6)
    fig, ax = plt.subplots(figsize=(8, 3.2))
    im = ax.imshow(piv.values, aspect="auto", cmap=CMAP)
    ax.set_xticks(range(12), ["J", "F", "M", "A", "M", "J",
                              "J", "A", "S", "O", "N", "D"])
    ax.set_yticks(range(len(piv)), piv.index)
    ax.set_title("Density — sales by region x month")
    ax.grid(False)
    cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.02)
    cb.set_label("sales ($M)", color=MUTED)
    cb.ax.yaxis.set_tick_params(color=MUTED)
    plt.setp(cb.ax.get_yticklabels(), color=MUTED)
    save(fig, "viz-heatmap-region-month")


# ── 2. Perceptual encoding ───────────────────────────────────────────────────
def bar_vs_pie():
    s = orders.groupby("region")["sales"].sum().sort_values(ascending=False) / 1e6
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9, 3.8))
    a1.bar(s.index, s.values, color=ACCENT)
    a1.set_title("Bar — lengths are easy to compare")
    a1.set_ylabel("sales ($M)")
    a1.tick_params(axis="x", rotation=20)
    a2.pie(s.values, labels=s.index, colors=[ACCENT, PURPLE, MINT, AMBER],
           autopct="%1.0f%%", textprops={"color": TEXT, "fontsize": 9})
    a2.set_title("Pie — angles are hard to compare")
    a2.grid(False)
    fig.suptitle("Same data, two encodings")
    save(fig, "viz-bar-vs-pie")


def axis_zero():
    s = orders.groupby("region")["sales"].sum().sort_values(ascending=False) / 1e6
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(9, 3.8))
    a1.bar(s.index, s.values, color=ROSE)
    a1.set_ylim(s.min() * 0.97, s.max() * 1.01)
    a1.set_title("Truncated axis — exaggerates gaps")
    a1.tick_params(axis="x", rotation=20)
    a2.bar(s.index, s.values, color=MINT)
    a2.set_ylim(0, s.max() * 1.05)
    a2.set_title("Zero baseline — honest comparison")
    a2.tick_params(axis="x", rotation=20)
    fig.suptitle("Why bar charts start at zero")
    save(fig, "viz-axis-zero")


# ── 3. Advanced charts ───────────────────────────────────────────────────────
def small_multiples():
    regions = sorted(orders["region"].unique())
    fig, axes = plt.subplots(2, 2, figsize=(9, 5), sharex=True, sharey=True)
    for ax, reg in zip(axes.ravel(), regions):
        m = orders[orders["region"] == reg].groupby("month")["sales"].sum() / 1e6
        ax.plot(m.index, m.values, color=ACCENT, linewidth=1.8)
        ax.fill_between(m.index, m.values, color=ACCENT, alpha=0.12)
        ax.set_title(reg, fontsize=10)
        ax.tick_params(axis="x", rotation=30, labelsize=7)
    fig.suptitle("Small multiples — monthly sales per region ($M)")
    fig.tight_layout()
    save(fig, "viz-small-multiples")


def box_profit_category():
    cats = ["Office", "Furniture", "Technology"]
    data = [orders.loc[orders["category"] == c, "profit"] for c in cats]
    fig, ax = plt.subplots(figsize=(7, 3.8))
    bp = ax.boxplot(data, tick_labels=cats, patch_artist=True, showfliers=False,
                    medianprops=dict(color=BG, linewidth=2))
    for patch, col in zip(bp["boxes"], [PURPLE, ACCENT, MINT]):
        patch.set_facecolor(col); patch.set_alpha(0.75)
    for w in bp["whiskers"] + bp["caps"]:
        w.set_color(MUTED)
    ax.set_title("Box plot — profit distribution by category")
    ax.set_ylabel("profit ($)")
    ax.grid(axis="x", visible=False)
    save(fig, "viz-box-profit-category")


def annotated_trend():
    m = orders.groupby("month")["sales"].sum() / 1e6
    trend = m.rolling(3, min_periods=1).mean()
    fig, ax = plt.subplots(figsize=(8, 3.8))
    ax.plot(m.index, m.values, color=MUTED, alpha=0.55, linewidth=1.3,
            label="Monthly sales")
    ax.plot(trend.index, trend.values, color=ACCENT, linewidth=2.4,
            label="3-month trend")
    # annotate the strongest Q4 peak
    peak = m.idxmax()
    ax.annotate("Q4 seasonal lift", xy=(peak, m.max()),
                xytext=(peak, m.max() * 1.18),
                color=AMBER, fontsize=9, ha="center",
                arrowprops=dict(color=AMBER, arrowstyle="->"))
    ax.set_title("Annotated time series — sales with rolling trend")
    ax.set_ylabel("sales ($M)")
    ax.legend(loc="upper left")
    save(fig, "viz-annotated-trend")


# ── 4. Dashboard composition ─────────────────────────────────────────────────
def dashboard():
    fig, axes = plt.subplots(2, 2, figsize=(11, 7))
    # line trend
    m = orders.groupby("month")["sales"].sum() / 1e6
    axes[0, 0].plot(m.index, m.values, color=ACCENT, linewidth=2)
    axes[0, 0].fill_between(m.index, m.values, color=ACCENT, alpha=0.12)
    axes[0, 0].set_title("Monthly sales ($M)")
    axes[0, 0].tick_params(axis="x", rotation=25, labelsize=8)
    # category bar
    s = orders.groupby("category")["sales"].sum().sort_values() / 1e6
    axes[0, 1].barh(s.index, s.values, color=PURPLE)
    axes[0, 1].set_title("Sales by category ($M)")
    axes[0, 1].grid(axis="y", visible=False)
    # region x month heatmap
    piv = (orders.assign(mm=orders["order_date"].dt.month)
                 .pivot_table(index="region", columns="mm",
                              values="sales", aggfunc="sum") / 1e6)
    im = axes[1, 0].imshow(piv.values, aspect="auto", cmap=CMAP)
    axes[1, 0].set_yticks(range(len(piv)), piv.index, fontsize=8)
    axes[1, 0].set_xticks([0, 5, 11], ["Jan", "Jun", "Dec"], fontsize=8)
    axes[1, 0].set_title("Sales: region x month")
    axes[1, 0].grid(False)
    # discount vs profit scatter
    sample = orders.sample(1800, random_state=7)
    axes[1, 1].scatter(sample["discount"], sample["profit"], s=8, alpha=0.25,
                       color=MINT, edgecolors="none")
    axes[1, 1].axhline(0, color=ROSE, linestyle="--", linewidth=1, alpha=0.7)
    axes[1, 1].set_title("Discount vs profit")
    axes[1, 1].set_xlabel("discount")
    fig.suptitle("Retail performance dashboard — one screen, four questions",
                 fontsize=13)
    fig.tight_layout()
    save(fig, "viz-dashboard")


if __name__ == "__main__":
    print("Visualization charts ->")
    bar_category(); line_monthly(); scatter_discount_profit()
    hist_sales(); heatmap_region_month()
    bar_vs_pie(); axis_zero()
    small_multiples(); box_profit_category(); annotated_trend()
    dashboard()
    print("done.")
