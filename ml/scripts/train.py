import joblib

from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

from config import (
    MODEL_DIR,
    MODEL_FILE,
    RANDOM_STATE,
    N_ESTIMATORS,
    MAX_DEPTH,
    LEARNING_RATE
)

from preprocess import (
    load_data,
    split_features_target,
    train_test_data
)

from evaluate import (
    evaluate_model,
    save_metrics,
    save_classification_report,
    save_confusion_matrix,
)

from visualize import (
    plot_confusion_matrix,
    plot_feature_importance,
)

from explain import (
    generate_shap_summary,
    generate_shap_bar,
)

def build_model():

    model = XGBClassifier(
        random_state=RANDOM_STATE,
        n_estimators=N_ESTIMATORS,
        max_depth=MAX_DEPTH,
        learning_rate=LEARNING_RATE
    )

    return model

def train(model, X_train, y_train):

    model.fit(X_train, y_train)

    return model

def evaluate(model, X_test, y_test):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"\nAccuracy: {accuracy:.4f}")

def save_model(model):

    MODEL_DIR.mkdir(exist_ok=True)

    joblib.dump(model, MODEL_FILE)

    print(f"\nModel saved to:\n{MODEL_FILE}")

def main():

    df = load_data()

    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = train_test_data(X, y)

    model = build_model()

    model = train(model, X_train, y_train)

    metrics, predictions = evaluate_model(
    model,
    X_test,
    y_test)

    save_metrics(metrics)

    save_classification_report(
    y_test,
    predictions,
    )

    save_confusion_matrix(
    y_test,
    predictions
    )

    plot_confusion_matrix(
    model,
    X_test,
    y_test
    )

    plot_feature_importance(model)

    generate_shap_summary(
    model,
    X_train
)

    generate_shap_bar(
    model,
    X_train
    )

    save_model(model)


if __name__ == "__main__":
    main()