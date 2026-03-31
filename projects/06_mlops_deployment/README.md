# MLOps Model Deployment

Production-ready ML model serving pipeline: train a RandomForestClassifier on synthetic data and serve predictions via a FastAPI REST API, with Docker support.

## Quick Start

```bash
# 1. Train the model
python train.py

# 2. Start the API server
uvicorn app.main:app --reload

# 3. Run tests
python -m pytest tests/ -v
```

## API Endpoints

### `GET /` — Welcome

```bash
curl http://localhost:8000/
```

### `GET /health` — Health Check

Returns model status and training metadata.

```bash
curl http://localhost:8000/health
```

### `POST /predict` — Single Prediction

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [0.1, -0.5, 1.2, 0.3, -0.8, 0.7, 0.0, 1.1, -0.2, 0.4]}'
```

Response:

```json
{
  "prediction": 1,
  "probability": 0.92,
  "probabilities": [0.08, 0.92]
}
```

### `POST /predict/batch` — Batch Predictions

```bash
curl -X POST http://localhost:8000/predict/batch \
  -H "Content-Type: application/json" \
  -d '{"samples": [[0.1,-0.5,1.2,0.3,-0.8,0.7,0.0,1.1,-0.2,0.4],[1.0,0.5,-0.3,0.8,0.2,-0.1,0.9,-0.7,0.6,-0.4]]}'
```

## Docker

```bash
# Train the model first (model must exist before building)
python train.py

# Build and run
docker compose up --build -d

# Check health
curl http://localhost:8000/health

# Stop
docker compose down
```

## Project Structure

```
├── train.py              # Training pipeline (synthetic data + RandomForest)
├── app/
│   ├── main.py           # FastAPI application with lifespan model loading
│   ├── model.py          # Model/metadata loading utilities
│   └── schemas.py        # Pydantic request/response models
├── models/               # Saved model artifacts (created by train.py)
│   ├── model.pkl
│   └── metadata.json
├── tests/
│   └── test_api.py       # Async API tests (httpx + pytest)
├── Dockerfile            # Python 3.11-slim container
├── docker-compose.yml    # Single-service compose config
├── requirements.txt      # Python dependencies
└── .dockerignore
```

## Training Details

- **Data**: 2 000 synthetic samples, 10 features, binary classification (`sklearn.make_classification`)
- **Model**: `RandomForestClassifier` with cross-validated hyperparameter search
- **Artifacts**: serialised model (`joblib`) + JSON metadata (accuracy, params, date)
