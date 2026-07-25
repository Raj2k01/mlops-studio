import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from config import RAW_DATA, RANDOM_STATE, TARGET_COLUMN, TEST_SIZE




def load_data():

    df = pd.read_csv(RAW_DATA)

    print(f"Dataset Shape: {df.shape}")

    return df


def validate_data(df):

    print("\nMissing Values")
    print(df.isnull().sum())

    print("\nDuplicate Rows")
    print(df.duplicated().sum())

    print("\nData Types")
    print(df.dtypes)


def split_features_target(df):

    X = df.drop(columns=[TARGET_COLUMN])

    y = df[TARGET_COLUMN]

    encoder = LabelEncoder()

    y = encoder.fit_transform(y)

    return X, y


def train_test_data(X, y):

    return train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )


def main():

    df = load_data()

    validate_data(df)

    X, y = split_features_target(df)

    X_train, X_test, y_train, y_test = train_test_data(X, y)

    print("\nTraining Set:", X_train.shape)
    print("Testing Set :", X_test.shape)


if __name__ == "__main__":
    main()