import matplotlib.pyplot as plt

from sklearn.metrics import ConfusionMatrixDisplay

from config import OUTPUT_DIR

def plot_confusion_matrix(model, X_test, y_test):

    OUTPUT_DIR.mkdir(exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 6))

    ConfusionMatrixDisplay.from_estimator(
        model,
        X_test,
        y_test,
        cmap="Blues",
        ax=ax
    )

    ax.set_title("Confusion Matrix")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "confusion_matrix.png",
        dpi=300
    )

    plt.close(fig)

    print("✓ Confusion matrix saved.")

def plot_feature_importance(model):
    """
    Generate and save feature importance plot.
    """

    OUTPUT_DIR.mkdir(exist_ok=True)

    importance = model.feature_importances_

    feature_names = model.feature_names_in_

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(feature_names, importance)

    ax.set_xlabel("Importance")

    ax.set_ylabel("Feature")

    ax.set_title("XGBoost Feature Importance")

    plt.tight_layout()

    plt.savefig(
        OUTPUT_DIR / "feature_importance.png",
        dpi=300
    )

    plt.close(fig)

    print("✓ Feature importance saved.")