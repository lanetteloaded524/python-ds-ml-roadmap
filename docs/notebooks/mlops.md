---
title: MLOps & Deployment
---

# 🚢 MLOps & Deployment

Ship a trained model as a production-ready REST API using FastAPI and Docker. This project demonstrates the complete ML deployment lifecycle — from model training to containerized serving with automated tests.

[![View on GitHub](https://img.shields.io/badge/View-GitHub-blue?logo=github)](https://github.com/djordjeperovic/python-ds-ml-roadmap/tree/main/projects/06_mlops_deployment)

## Topics Covered

- Training and serializing ML models with joblib
- Building a FastAPI REST API with prediction endpoints
- Single and batch prediction endpoints
- Health check and model metadata endpoints
- Pydantic request/response validation
- Docker containerization for reproducible deployment
- Docker Compose for service orchestration
- Automated testing with pytest and httpx

## Prerequisites

- Completion of the ML Fundamentals notebook
- Basic understanding of REST APIs and HTTP
- Familiarity with the command line
- Docker installed (for containerization)

## Key Takeaways

- Train and save ML models for production serving
- Build a complete REST API with FastAPI for model predictions
- Containerize ML applications with Docker for reproducible deployment
- Write automated tests for ML APIs using pytest
- Understand the end-to-end MLOps workflow from training to serving

## Project Structure

```
06_mlops_deployment/
├── train.py              # Training pipeline (synthetic data + RandomForest)
├── app/
│   ├── main.py           # FastAPI application with lifespan model loading
│   ├── model.py          # Model/metadata loading utilities
│   └── schemas.py        # Pydantic request/response models
├── models/               # Saved model artifacts (created by train.py)
├── tests/
│   └── test_api.py       # Async API tests (httpx + pytest)
├── Dockerfile            # Python 3.11-slim container
├── docker-compose.yml    # Single-service compose config
└── requirements.txt      # Python dependencies
```

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

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message |
| `GET` | `/health` | Health check with model metadata |
| `POST` | `/predict` | Single prediction |
| `POST` | `/predict/batch` | Batch predictions |
