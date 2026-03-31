"""Train a RandomForestClassifier on synthetic data and save artifacts."""

import json
import os
from datetime import datetime, timezone

import joblib
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, classification_report

MODELS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")


def train() -> None:
    print("=" * 60)
    print("MLOps Model Training Pipeline")
    print("=" * 60)

    # Generate synthetic classification data
    n_features = 10
    X, y = make_classification(
        n_samples=2000,
        n_features=n_features,
        n_informative=6,
        n_redundant=2,
        n_classes=2,
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y,
    )

    print(f"\nDataset: {X.shape[0]} samples, {n_features} features")
    print(f"  Train: {X_train.shape[0]}  |  Test: {X_test.shape[0]}")

    # Basic hyperparameter tuning via cross-validation
    best_score = -1.0
    best_params: dict = {}
    param_grid = [
        {"n_estimators": 50, "max_depth": 5},
        {"n_estimators": 100, "max_depth": 10},
        {"n_estimators": 100, "max_depth": None},
        {"n_estimators": 200, "max_depth": 10},
    ]

    print("\nHyperparameter search …")
    for params in param_grid:
        clf = RandomForestClassifier(**params, random_state=42, n_jobs=-1)
        scores = cross_val_score(clf, X_train, y_train, cv=5, scoring="accuracy")
        mean_score = float(np.mean(scores))
        print(f"  {params} → CV accuracy: {mean_score:.4f}")
        if mean_score > best_score:
            best_score = mean_score
            best_params = params

    print(f"\nBest params: {best_params}  (CV accuracy: {best_score:.4f})")

    # Train final model with best params
    model = RandomForestClassifier(**best_params, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    test_accuracy = float(accuracy_score(y_test, y_pred))

    print(f"\nTest accuracy: {test_accuracy:.4f}")
    print("\nClassification report:")
    print(classification_report(y_test, y_pred))

    # Save artifacts
    os.makedirs(MODELS_DIR, exist_ok=True)

    model_path = os.path.join(MODELS_DIR, "model.pkl")
    joblib.dump(model, model_path)
    print(f"Model saved → {model_path}")

    metadata = {
        "accuracy": round(test_accuracy, 4),
        "cv_accuracy": round(best_score, 4),
        "n_features": n_features,
        "best_params": best_params,
        "training_date": datetime.now(timezone.utc).isoformat(),
        "n_train_samples": X_train.shape[0],
        "n_test_samples": X_test.shape[0],
    }
    meta_path = os.path.join(MODELS_DIR, "metadata.json")
    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=2)
    print(f"Metadata saved → {meta_path}")

    print("\n" + "=" * 60)
    print("Training complete!")
    print("=" * 60)


if __name__ == "__main__":
    train()
