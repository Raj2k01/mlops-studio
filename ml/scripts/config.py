from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA = PROJECT_ROOT / "data" / "raw" / "redwinequality.csv"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"

# Models
MODEL_DIR = PROJECT_ROOT / "models"
MODEL_FILE = MODEL_DIR / "xgboost_model.pkl"

# Prediction Input/Output Files
INPUT_FILE = PROJECT_ROOT / "data" / "prediction_input.json"
OUTPUT_FILE = PROJECT_ROOT / "data" / "prediction_output.json"

# Outputs
OUTPUT_DIR = PROJECT_ROOT / "outputs"

# Random seed
RANDOM_STATE = 42

# Target column
TARGET_COLUMN = "quality"

# Train/Test Split
TEST_SIZE = 0.2

# XGBoost Parameters
N_ESTIMATORS = 100
MAX_DEPTH = 6
LEARNING_RATE = 0.1

