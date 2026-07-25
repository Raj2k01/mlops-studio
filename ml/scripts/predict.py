import joblib
import pandas as pd

from config import MODEL_FILE

def load_model():

    model = joblib.load(MODEL_FILE)

    return model

def predict_quality(model, input_data):

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)

    return int(prediction[0])

def main():

    model = load_model()

    sample = {
        "fixed acidity": 7.4,
        "volatile acidity": 0.70,
        "citric acid": 0.00,
        "residual sugar": 1.9,
        "chlorides": 0.076,
        "free sulfur dioxide": 11,
        "total sulfur dioxide": 34,
        "density": 0.9978,
        "pH": 3.51,
        "sulphates": 0.56,
        "alcohol": 9.4
    }

    prediction = predict_quality(
        model,
        sample
    )

    print(f"Predicted Wine Quality: {prediction}")


if __name__ == "__main__":
    main()