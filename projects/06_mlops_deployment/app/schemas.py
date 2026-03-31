"""Pydantic request / response models for the prediction API."""

from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    features: list[float] = Field(..., description="Feature vector for a single sample")

    model_config = {"json_schema_extra": {"examples": [{"features": [0.1, -0.5, 1.2, 0.3, -0.8, 0.7, 0.0, 1.1, -0.2, 0.4]}]}}


class PredictionResponse(BaseModel):
    prediction: int = Field(..., description="Predicted class label")
    probability: float = Field(..., description="Probability of the predicted class")
    probabilities: list[float] = Field(..., description="Probabilities for each class")


class BatchPredictionRequest(BaseModel):
    samples: list[list[float]] = Field(..., description="List of feature vectors")


class BatchPredictionResponse(BaseModel):
    predictions: list[PredictionResponse]


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    metadata: dict | None = None
