"""Model loading utilities."""

import json
import os
from typing import Any

import joblib

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(_BASE_DIR, "models")
MODEL_PATH = os.path.join(MODELS_DIR, "model.pkl")
METADATA_PATH = os.path.join(MODELS_DIR, "metadata.json")


def load_model() -> Any:
    """Load the trained model from disk. Raises FileNotFoundError if missing."""
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)


def get_metadata() -> dict:
    """Read model metadata. Returns empty dict if the file is missing."""
    if not os.path.exists(METADATA_PATH):
        return {}
    with open(METADATA_PATH) as f:
        return json.load(f)
