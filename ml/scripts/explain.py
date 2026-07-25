import shap
import matplotlib.pyplot as plt

from config import OUTPUT_DIR

def generate_shap_summary(model, X_train):

    OUTPUT_DIR.mkdir(exist_ok=True)

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X_train)

    plt.figure(figsize=(10, 6))

    shap.summary_plot(
        shap_values,
        X_train,
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "shap_summary.png",
        dpi=300
    )

    plt.close()

    print("✓ SHAP summary saved.")

def generate_shap_bar(model, X_train):

    OUTPUT_DIR.mkdir(exist_ok=True)

    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X_train)

    plt.figure(figsize=(10, 6))

    shap.summary_plot(
        shap_values,
        X_train,
        plot_type="bar",
        show=False
    )

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "shap_bar.png",
        dpi=300
    )

    plt.close()

    print("✓ SHAP bar chart saved.")