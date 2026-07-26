import json
import joblib
import pandas as pd

from config import (
    MODEL_FILE,
    INPUT_FILE,
    OUTPUT_FILE
)


def load_model():
    return joblib.load(MODEL_FILE)


def load_input():
    with open(INPUT_FILE, "r") as file:
        return json.load(file)


def predict(model, input_data):

    mapped_input = map_input(input_data)

    input_df = pd.DataFrame([mapped_input])

    prediction = model.predict(input_df)

    return int(prediction[0])


def save_output(prediction):

    result = {
        "prediction": prediction
    }

    with open(OUTPUT_FILE, "w") as file:
        json.dump(result, file, indent=4)


def main():

    model = load_model()

    input_data = load_input()

    prediction = predict(model, input_data)

    save_output(prediction)

    print(f"Prediction saved to {OUTPUT_FILE}")

def map_input(input_data):

    return {
        "fixed acidity": input_data["fixedAcidity"],
        "volatile acidity": input_data["volatileAcidity"],
        "citric acid": input_data["citricAcid"],
        "residual sugar": input_data["residualSugar"],
        "chlorides": input_data["chlorides"],
        "free sulfur dioxide": input_data["freeSulfurDioxide"],
        "total sulfur dioxide": input_data["totalSulfurDioxide"],
        "density": input_data["density"],
        "pH": input_data["pH"],
        "sulphates": input_data["sulphates"],
        "alcohol": input_data["alcohol"]
    }


if __name__ == "__main__":
    main()