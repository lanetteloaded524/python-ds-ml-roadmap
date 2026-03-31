"""API tests using httpx AsyncClient with ASGITransport."""

import pytest
import httpx
from app.main import app, lifespan

BASE_URL = "http://testserver"


@pytest.fixture
async def client():
    async with lifespan(app):
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(transport=transport, base_url=BASE_URL) as c:
            yield c


@pytest.mark.anyio
async def test_root(client):
    resp = await client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert "message" in data


@pytest.mark.anyio
async def test_health(client):
    resp = await client.get("/health")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "healthy"
    assert data["model_loaded"] is True
    assert data["metadata"] is not None
    assert "accuracy" in data["metadata"]


@pytest.mark.anyio
async def test_predict_valid(client):
    payload = {"features": [0.1, -0.5, 1.2, 0.3, -0.8, 0.7, 0.0, 1.1, -0.2, 0.4]}
    resp = await client.post("/predict", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert "prediction" in data
    assert data["prediction"] in (0, 1)
    assert 0.0 <= data["probability"] <= 1.0
    assert len(data["probabilities"]) == 2


@pytest.mark.anyio
async def test_predict_invalid_feature_count(client):
    payload = {"features": [0.1, 0.2]}  # wrong number of features
    resp = await client.post("/predict", json=payload)
    assert resp.status_code == 422


@pytest.mark.anyio
async def test_predict_empty_features(client):
    payload = {"features": []}
    resp = await client.post("/predict", json=payload)
    assert resp.status_code == 422


@pytest.mark.anyio
async def test_batch_predict(client):
    payload = {
        "samples": [
            [0.1, -0.5, 1.2, 0.3, -0.8, 0.7, 0.0, 1.1, -0.2, 0.4],
            [1.0, 0.5, -0.3, 0.8, 0.2, -0.1, 0.9, -0.7, 0.6, -0.4],
        ]
    }
    resp = await client.post("/predict/batch", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["predictions"]) == 2
    for pred in data["predictions"]:
        assert pred["prediction"] in (0, 1)
        assert 0.0 <= pred["probability"] <= 1.0


@pytest.mark.anyio
async def test_batch_predict_empty(client):
    resp = await client.post("/predict/batch", json={"samples": []})
    assert resp.status_code == 422
