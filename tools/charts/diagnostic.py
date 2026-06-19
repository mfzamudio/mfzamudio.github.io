"""Generate the charts for the Diagnostic Analytics mini-series.

    python3 tools/charts/diagnostic.py
"""
import numpy as np
import pandas as pd
from scipy import stats

from _common import (focused_orders, apply_style, save,
                     ACCENT, PURPLE, MINT, AMBER, ROSE, MUTED, TEXT, GRID, BG, CMAP)
import matplotlib.pyplot as plt

apply_style()
orders = focused_orders()
orders["margin"] = orders["profit"] / orders["sales"]          # = 0.30 - discount
orders["high_value"] = orders["sales"] > orders["sales"].median()


# ── Chapter 1 — correlation ──────────────────────────────────────────────────
def corr_matrix():
    cols = ["discount", "quantity", "sales", "profit", "margin"]
    c = orders[cols].corr()
    fig, ax = plt.subplots(figsize=(5.8, 5))
    im = ax.imshow(c.values, cmap=CMAP, vmin=-1, vmax=1)
    ax.set_xticks(range(len(cols)), cols, rotation=35, ha="right")
    ax.set_yticks(range(len(cols)), cols)
    for i in range(len(cols)):
        for j in range(len(cols)):
            ax.text(j, i, f"{c.values[i, j]:.2f}", ha="center", va="center",
                    color="#fff" if abs(c.values[i, j]) > 0.5 else MUTED, fontsize=9)
    ax.set_title("Correlation matrix of numeric drivers")
    ax.grid(False)
    fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    save(fig, "diag-corr-matrix")


def corr_target():
    drivers = ["discount", "quantity", "sales"]
    corr = orders[drivers + ["profit"]].corr()["profit"].drop("profit").sort_values()
    colors = [ROSE if v < 0 else MINT for v in corr.values]
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.barh(corr.index, corr.values, color=colors)
    ax.axvline(0, color=MUTED, linewidth=1)
    for y, v in enumerate(corr.values):
        ax.text(v + (0.03 if v >= 0 else -0.03), y, f"{v:.2f}",
                va="center", ha="left" if v >= 0 else "right", color=TEXT, fontsize=9)
    ax.set_xlim(-1, 1)
    ax.set_title("Correlation of each driver with profit")
    ax.set_xlabel("correlation with profit")
    ax.grid(axis="y", visible=False)
    save(fig, "diag-corr-target")


# ── Chapter 2 — hypothesis testing ───────────────────────────────────────────
def ttest_profit():
    disc = orders.loc[orders["discount"] > 0, "profit"]
    full = orders.loc[orders["discount"] == 0, "profit"]
    t, p = stats.ttest_ind(disc, full, equal_var=False)
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    bins = np.linspace(0, orders["profit"].quantile(0.99), 45)
    ax.hist(full, bins=bins, color=MINT, alpha=0.55, label="Full price")
    ax.hist(disc, bins=bins, color=ROSE, alpha=0.55, label="Discounted")
    ax.axvline(full.mean(), color=MINT, linewidth=2)
    ax.axvline(disc.mean(), color=ROSE, linewidth=2)
    ax.set_title(f"Profit by pricing — Welch t-test  (t = {t:.1f}, p < 0.001)")
    ax.set_xlabel("profit ($)"); ax.set_ylabel("orders")
    ax.legend()
    save(fig, "diag-ttest")


def chisquare_category():
    table = pd.crosstab(orders["category"], orders["high_value"])
    chi2, p, dof, _ = stats.chi2_contingency(table)
    share = (table[True] / table.sum(axis=1) * 100).sort_values()
    fig, ax = plt.subplots(figsize=(7, 3.4))
    ax.bar(share.index, share.values, color=[MINT, ACCENT, PURPLE])
    for x, v in enumerate(share.values):
        ax.text(x, v + 1, f"{v:.0f}%", ha="center", color=TEXT, fontsize=10)
    ax.set_title(f"High-value share by category  (chi-square p < 0.001)")
    ax.set_ylabel("% of orders above median sales")
    ax.grid(axis="x", visible=False)
    save(fig, "diag-chisquare")


# ── Chapter 3 — drill-down ───────────────────────────────────────────────────
def drilldown():
    g = (orders.groupby("discount")["margin"].mean() * 100)
    fig, ax = plt.subplots(figsize=(7, 3.4))
    ax.bar([f"{int(d*100)}%" for d in g.index], g.values, color=ACCENT)
    for x, v in enumerate(g.values):
        ax.text(x, v + 0.6, f"{v:.0f}%", ha="center", color=TEXT, fontsize=10)
    ax.set_title("Drill-down — average margin by discount level")
    ax.set_xlabel("discount applied"); ax.set_ylabel("average margin (%)")
    ax.grid(axis="x", visible=False)
    save(fig, "diag-drilldown")


# ── Chapter 4 — correlation is not causation (illustrative confounder) ────────
def confounder():
    rng = np.random.default_rng(3)
    months = np.arange(12)
    temp = 12 + 12 * np.sin((months - 3) / 12 * 2 * np.pi)        # the real cause
    ice_cream = 20 + 4 * temp + rng.normal(0, 6, 12)
    drownings = 1 + 0.25 * temp + rng.normal(0, 1.2, 12)
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ax2 = ax.twinx()
    l1, = ax.plot(months, ice_cream, color=ACCENT, linewidth=2.2, marker="o",
                  label="Ice-cream sales")
    l2, = ax2.plot(months, drownings, color=ROSE, linewidth=2.2, marker="s",
                   label="Drownings")
    ax.set_title("Strongly correlated — but neither causes the other")
    ax.set_xlabel("month"); ax.set_ylabel("ice-cream sales", color=ACCENT)
    ax2.set_ylabel("drownings", color=ROSE)
    ax2.grid(False)
    ax.legend(handles=[l1, l2], loc="upper left")
    save(fig, "diag-confounder")


if __name__ == "__main__":
    print("Diagnostic charts ->")
    corr_matrix(); corr_target()
    ttest_profit(); chisquare_category()
    drilldown(); confounder()
    print("done.")
