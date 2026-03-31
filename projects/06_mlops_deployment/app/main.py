"""FastAPI application for serving ML predictions."""

from contextlib import asynccontextmanager
from typing import Any

import numpy as np
from fastapi import FastAPI, HTTPException

from app.model import load_model, get_metadata
from app.schemas import (
    BatchPredictionRequest,
    BatchPredictionResponse,
    HealthResponse,
    PredictionRequest,
    PredictionResponse,
)

_model: Any = None
_metadata: dict = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load the model once at startup."""
    global _model, _metadata
    try:
        _model = load_model()
        _metadata = get_metadata()
        print("Model loaded successfully")
    except FileNotFoundError:
        print("WARNING: No model found – run train.py first")
    yield


app = FastAPI(
    title="MLOps Prediction API",
    description="Serves predictions from a trained RandomForestClassifier",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/")
def root():
    return {"message": "MLOps Prediction API", "docs": "/docs"}


@app.get("/health", response_model=HealthResponse)
def health():
    return HealthResponse(
        status="healthy",
        model_loaded=_model is not None,
        metadata=_metadata if _metadata else None,
    )


def _predict_single(features: list[float]) -> PredictionResponse:
    if _model is None:
        raise HTTPException(status_code=503, detail="Model not loaded. Run train.py first.")

    expected = _metadata.get("n_features")
    if expected and len(features) != expected:
        raise HTTPException(
            status_code=422,
            detail=f"Expected {expected} features, got {len(features)}",
        )

    X = np.array(features).reshape(1, -1)
    prediction = int(_model.predict(X)[0])
    probabilities = _model.predict_proba(X)[0].tolist()
    probability = float(max(probabilities))
    return PredictionResponse(
        prediction=prediction,
        probability=probability,
        probabilities=probabilities,
    )


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    return _predict_single(request.features)


@app.post("/predict/batch", response_model=BatchPredictionResponse)
def predict_batch(request: BatchPredictionRequest):
    if not request.samples:
        raise HTTPException(status_code=422, detail="samples list must not be empty")
    results = [_predict_single(sample) for sample in request.samples]
    return BatchPredictionResponse(predictions=results)
