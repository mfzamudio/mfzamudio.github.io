"""Generate the charts for the Predictive Analytics mini-series.

    python3 tools/charts/predictive.py

The base synthetic dataset has no real churn outcome, so the classification
section uses a *constructed* churn label (a latent propensity from behavioural
features + noise) purely to illustrate the ML workflow. This is stated on the
page. The regression target (customer lifetime sales) is genuine.
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import (r2_score, mean_absolute_error, confusion_matrix,
                             roc_curve, auc)

from _common import (focused_orders, apply_style, save,
                     ACCENT, PURPLE, MINT, AMBER, ROSE, MUTED, TEXT, GRID, BG, CMAP)
import matplotlib.pyplot as plt

apply_style()
orders = focused_orders()

# ── Customer-level feature table ─────────────────────────────────────────────
asof = orders["order_date"].max()
cust = (orders.groupby("customer_id")
              .agg(total_sales=("sales", "sum"),
                   orders=("order_id", "nunique"),
                   avg_discount=("discount", "mean"),
                   avg_quantity=("quantity", "mean"),
                   first=("order_date", "min"),
                   last=("order_date", "max"))
              .reset_index())
cust["tenure_days"] = (cust["last"] - cust["first"]).dt.days
cust["recency_days"] = (asof - cust["last"]).dt.days

FEATURES = ["orders", "avg_discount", "avg_quantity", "tenure_days"]


# ── Chapter 1 — framing: clustering ──────────────────────────────────────────
def clusters():
    X = StandardScaler().fit_transform(cust[["total_sales", "orders", "avg_discount"]])
    cust["cluster"] = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(X)
    fig, ax = plt.subplots(figsize=(7, 4.2))
    for k, col in zip(sorted(cust["cluster"].unique()), [ACCENT, PURPLE, MINT]):
        sub = cust[cust["cluster"] == k]
        ax.scatter(sub["orders"], sub["total_sales"] / 1e3, s=18, alpha=0.55,
                   color=col, edgecolors="none", label=f"cluster {k}")
    ax.set_title("Clustering — customer segments (K-Means, k=3)")
    ax.set_xlabel("orders per customer"); ax.set_ylabel("lifetime sales ($K)")
    ax.legend()
    save(fig, "pred-clusters")


# ── Chapter 2 — train/test split & overfitting ───────────────────────────────
def overfit():
    rng = np.random.default_rng(0)
    x = np.linspace(0, 1, 60)
    y = np.sin(2 * np.pi * x) + rng.normal(0, 0.25, x.size)   # true signal + noise
    xtr, xte, ytr, yte = train_test_split(x, y, test_size=0.4, random_state=1)
    degrees = range(1, 16)
    tr_err, te_err = [], []
    for d in degrees:
        coef = np.polyfit(xtr, ytr, d)
        tr_err.append(np.sqrt(np.mean((np.polyval(coef, xtr) - ytr) ** 2)))
        te_err.append(np.sqrt(np.mean((np.polyval(coef, xte) - yte) ** 2)))
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ax.plot(list(degrees), tr_err, color=MINT, marker="o", label="Training error")
    ax.plot(list(degrees), te_err, color=ROSE, marker="s", label="Test error")
    best = list(degrees)[int(np.argmin(te_err))]
    ax.axvline(best, color=AMBER, linestyle="--", alpha=0.8)
    ax.text(best + 0.2, max(te_err) * 0.9, "overfitting →", color=AMBER, fontsize=9)
    ax.set_title("Overfitting — training vs test error by model complexity")
    ax.set_xlabel("polynomial degree (complexity)"); ax.set_ylabel("RMSE")
    ax.set_ylim(0, min(2.0, max(te_err) * 1.1))
    ax.legend()
    save(fig, "pred-overfit")


# ── Chapter 3 — regression ───────────────────────────────────────────────────
def _fit_regression():
    X, y = cust[FEATURES], cust["total_sales"]
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)
    model = RandomForestRegressor(n_estimators=200, random_state=42).fit(Xtr, ytr)
    pred = model.predict(Xte)
    return model, yte, pred


def regression_pred_actual():
    model, yte, pred = _fit_regression()
    r2 = r2_score(yte, pred); mae = mean_absolute_error(yte, pred)
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.scatter(yte / 1e3, pred / 1e3, s=14, alpha=0.4, color=ACCENT, edgecolors="none")
    lim = [0, max(yte.max(), pred.max()) / 1e3 * 1.02]
    ax.plot(lim, lim, color=ROSE, linestyle="--", label="perfect prediction")
    ax.set_title(f"Regression — predicted vs actual  (R^2 = {r2:.2f})")
    ax.set_xlabel("actual lifetime sales ($K)")
    ax.set_ylabel("predicted ($K)")
    ax.legend(loc="upper left")
    save(fig, "pred-pred-actual")
    return r2, mae


def regression_importance():
    model, _, _ = _fit_regression()
    imp = pd.Series(model.feature_importances_, index=FEATURES).sort_values()
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.barh(imp.index, imp.values, color=PURPLE)
    for y, v in enumerate(imp.values):
        ax.text(v + 0.01, y, f"{v:.2f}", va="center", color=TEXT, fontsize=9)
    ax.set_title("Regression — feature importance")
    ax.set_xlabel("importance"); ax.set_xlim(0, imp.max() * 1.18)
    ax.grid(axis="y", visible=False)
    save(fig, "pred-feature-importance")


# ── Chapter 4 — classification (constructed churn label) ─────────────────────
def _fit_classifier():
    c = cust.copy()
    z = StandardScaler().fit_transform(
        c[["avg_discount", "orders", "tenure_days", "avg_quantity"]])
    # latent churn propensity: high discount & low engagement -> churn
    logit = 0.9 * z[:, 0] - 1.1 * z[:, 1] - 0.7 * z[:, 2] + 0.2 * z[:, 3]
    rng = np.random.default_rng(7)
    prob = 1 / (1 + np.exp(-logit))
    c["churn"] = (rng.random(len(c)) < prob).astype(int)
    X, y = c[FEATURES], c["churn"]
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42,
                                          stratify=y)
    clf = RandomForestClassifier(n_estimators=250, random_state=42).fit(Xtr, ytr)
    return clf, Xte, yte


def confusion():
    clf, Xte, yte = _fit_classifier()
    pred = clf.predict(Xte)
    cm = confusion_matrix(yte, pred)
    fig, ax = plt.subplots(figsize=(5.2, 4.4))
    im = ax.imshow(cm, cmap=CMAP)
    labels = ["Retained", "Churned"]
    ax.set_xticks([0, 1], labels); ax.set_yticks([0, 1], labels)
    ax.set_xlabel("predicted"); ax.set_ylabel("actual")
    for i in range(2):
        for j in range(2):
            ax.text(j, i, f"{cm[i, j]:,}", ha="center", va="center",
                    color="#fff", fontsize=13, fontweight="bold")
    ax.set_title("Classification — confusion matrix")
    ax.grid(False)
    save(fig, "pred-confusion")


def roc():
    clf, Xte, yte = _fit_classifier()
    proba = clf.predict_proba(Xte)[:, 1]
    fpr, tpr, _ = roc_curve(yte, proba)
    a = auc(fpr, tpr)
    fig, ax = plt.subplots(figsize=(5.6, 4.4))
    ax.plot(fpr, tpr, color=ACCENT, linewidth=2.4, label=f"model (AUC = {a:.2f})")
    ax.plot([0, 1], [0, 1], color=MUTED, linestyle="--", label="random")
    ax.set_title("Classification — ROC curve")
    ax.set_xlabel("false positive rate"); ax.set_ylabel("true positive rate")
    ax.legend(loc="lower right")
    save(fig, "pred-roc")


if __name__ == "__main__":
    print("Predictive charts ->")
    clusters(); overfit()
    r2, mae = regression_pred_actual(); regression_importance()
    confusion(); roc()
    print(f"  (regression R^2={r2:.3f}, MAE={mae:,.0f})")
    print("done.")
