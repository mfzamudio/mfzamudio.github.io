"""Generate the charts for the Prescriptive Analytics mini-series.

    python3 tools/charts/prescriptive.py

A marketing-budget allocation problem: split a fixed budget across three
channels to maximize expected return, subject to per-channel min/max rules.
The expected-return-per-dollar figures are illustrative inputs (the kind a
predictive model would estimate); the optimization itself is real scipy.linprog.
"""
import numpy as np
from scipy.optimize import linprog

from _common import (apply_style, save,
                     ACCENT, PURPLE, MINT, AMBER, ROSE, MUTED, TEXT, GRID, BG)
import matplotlib.pyplot as plt

apply_style()

CHANNELS = ["West", "Email", "Paid search"]
RETURNS = np.array([2.10, 1.40, 3.05])      # expected $ return per $1 spent
BOUNDS = [(10_000, 60_000), (0, 40_000), (5_000, 50_000)]
BUDGET = 100_000


def optimize(budget=BUDGET, bounds=BOUNDS):
    c = -RETURNS                            # linprog minimizes -> negate to maximize
    res = linprog(c, A_ub=[[1, 1, 1]], b_ub=[budget], bounds=bounds, method="highs")
    return res.x, -res.fun


# ── Chapter 1 — scenarios (compare candidate allocations) ────────────────────
def scenarios():
    even = np.array([BUDGET / 3] * 3)
    # a plausible human choice: over-fund the familiar channel (West)
    intuition = np.array([60_000, 20_000, 20_000], dtype=float)
    opt, _ = optimize()
    allocs = {"Even split": even, "Favor familiar (West)": intuition, "Optimized (LP)": opt}
    returns = {k: (v * RETURNS).sum() / 1e3 for k, v in allocs.items()}
    fig, ax = plt.subplots(figsize=(7, 3.6))
    cols = [MUTED, PURPLE, MINT]
    bars = ax.bar(list(returns), list(returns.values()), color=cols)
    for b, v in zip(bars, returns.values()):
        ax.text(b.get_x() + b.get_width() / 2, v + 2, f"${v:,.0f}K",
                ha="center", color=TEXT, fontsize=10)
    ax.set_title("Scenario comparison — expected return by allocation strategy")
    ax.set_ylabel("expected return ($K)")
    ax.grid(axis="x", visible=False)
    save(fig, "presc-scenarios")


# ── Chapter 2 — business rules / constraints (feasibility) ───────────────────
def rules():
    opt, _ = optimize()
    y = np.arange(len(CHANNELS))
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    for i, (lo, hi) in enumerate(BOUNDS):
        ax.plot([lo / 1e3, hi / 1e3], [i, i], color=GRID, linewidth=10, solid_capstyle="round")
        ax.plot([lo / 1e3, hi / 1e3], [i, i], color=MUTED, linewidth=2, alpha=0.6)
        ax.scatter([lo / 1e3, hi / 1e3], [i, i], color=MUTED, s=20, zorder=3)
    ax.scatter(opt / 1e3, y, color=MINT, s=130, zorder=5, label="optimal allocation")
    for i, v in enumerate(opt):
        ax.text(v / 1e3, i - 0.28, f"${v/1e3:,.0f}K", ha="center", color=MINT, fontsize=9)
    ax.set_yticks(y, CHANNELS)
    ax.set_ylim(-0.6, len(CHANNELS) - 0.4)
    ax.set_xlim(-4, 66)
    ax.set_xlabel("spend ($K)")
    ax.set_title("Business rules — feasible range per channel, and the chosen point")
    ax.grid(axis="y", visible=False)
    ax.legend(loc="lower left")
    save(fig, "presc-rules")


# ── Chapter 3 — the optimization result ──────────────────────────────────────
def optimization():
    opt, total = optimize()
    fig, ax = plt.subplots(figsize=(7, 3.6))
    bars = ax.bar(CHANNELS, opt / 1e3, color=[ACCENT, PURPLE, MINT])
    for b, v, r in zip(bars, opt, RETURNS):
        ax.text(b.get_x() + b.get_width() / 2, v / 1e3 + 1,
                f"${v/1e3:,.0f}K\n@ {r:.2f}x", ha="center", color=TEXT, fontsize=9)
    ax.set_title(f"Optimal allocation of ${BUDGET/1e3:,.0f}K  "
                 f"(expected return ${total/1e3:,.0f}K)")
    ax.set_ylabel("spend ($K)")
    ax.set_ylim(0, max(opt) / 1e3 * 1.25)
    ax.grid(axis="x", visible=False)
    save(fig, "presc-optimization")


# ── Chapter 4 — sensitivity (optimal return vs budget) ───────────────────────
def sensitivity():
    budgets = np.linspace(40_000, 200_000, 33)
    rets = [optimize(budget=b)[1] / 1e3 for b in budgets]
    cap = sum(hi for _, hi in BOUNDS)       # max deployable spend = 150k
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ax.plot(budgets / 1e3, rets, color=ACCENT, linewidth=2.6)
    ax.axvline(cap / 1e3, color=AMBER, linestyle="--", alpha=0.85)
    ax.text(cap / 1e3 + 2, min(rets) + (max(rets) - min(rets)) * 0.1,
            "caps bind →\nextra budget wasted", color=AMBER, fontsize=9)
    ax.set_title("Sensitivity — optimal return as the budget changes")
    ax.set_xlabel("budget ($K)"); ax.set_ylabel("max expected return ($K)")
    save(fig, "presc-sensitivity")


if __name__ == "__main__":
    print("Prescriptive charts ->")
    scenarios(); rules(); optimization(); sensitivity()
    opt, total = optimize()
    print("  optimal:", {c: int(v) for c, v in zip(CHANNELS, opt)},
          f"-> ${total:,.0f}")
    print("done.")
