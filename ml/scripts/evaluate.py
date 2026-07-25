import json
from pathlib import Path

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)

from config import OUTPUT_DIR

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    metrics = {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0,
        ),
        "recall": recall_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0,
        ),
        "f1_score": f1_score(
            y_test,
            predictions,
            average="weighted",
            zero_division=0,
        ),
    }

    print("\nModel Metrics")

    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

    return metrics, predictions

def save_metrics(metrics):

    OUTPUT_DIR.mkdir(exist_ok=True)

    with open(
        OUTPUT_DIR / "metrics.json",
        "w"
    ) as file:

        json.dump(metrics, file, indent=4)

    print("\nMetrics saved successfully.")

def save_classification_report(y_test, predictions):

    report = classification_report(
        y_test,
        predictions,
        zero_division=0
    )

    with open(
        OUTPUT_DIR / "classification_report.txt",
        "w"
    ) as file:

        file.write(report)

    print("Classification report saved.")

def save_confusion_matrix(y_test, predictions):

    matrix = confusion_matrix(
        y_test,
        predictions
    )

    with open(
        OUTPUT_DIR / "confusion_matrix.txt",
        "w"
    ) as file:

        file.write(str(matrix))

    print("Confusion matrix saved.")