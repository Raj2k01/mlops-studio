from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA = PROJECT_ROOT / "data" / "raw" / "redwinequality.csv"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"

#models
MODEL_DIR = PROJECT_ROOT / "models"
MODEL_FILE = MODEL_DIR / "xgboost_model.pkl"

#outputs
OUTPUT_DIR = PROJECT_ROOT / "outputs"

# Random Seed
RANDOM_STATE = 45

# Target Column
TARGET_COLUMN = "quality"