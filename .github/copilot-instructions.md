# Copilot Instructions for python-ds-ml-roadmap

## Project Overview
This is an educational repository providing a structured learning path for Data Science and Machine Learning using Python. It contains Jupyter notebook tutorials, a FastAPI model deployment project, and quick-reference cheat sheets.

## Repository Structure
- `projects/01_data_fundamentals/` — NumPy, Pandas, Matplotlib, Seaborn tutorial notebook
- `projects/02_ml_fundamentals/` — scikit-learn ML tutorial (regression, classification, clustering)
- `projects/03_deep_learning/` — PyTorch deep learning tutorial (tensors, MLP, CNN)
- `projects/04_advanced_ml/` — XGBoost, LightGBM, pipelines, imbalanced data tutorial
- `projects/05_nlp/` — NLP text processing, TF-IDF, sentiment analysis tutorial
- `projects/06_mlops_deployment/` — FastAPI + Docker model serving project
- `cheat_sheets/` — Quick-reference markdown guides for NumPy, Pandas, scikit-learn, PyTorch
- `ROADMAP.md` — Full 10-phase learning roadmap with resources

## Key Conventions
- All notebooks use **synthetic data** — no external downloads required
- Notebooks are created programmatically via `nbformat` and validated with `jupyter nbconvert --execute`
- The MLOps project uses FastAPI with Pydantic schemas and async test patterns
- Python 3.10+ is required; PyTorch is CPU-only by default
- Random seeds are set for reproducibility (`np.random.seed(42)`, `torch.manual_seed(42)`)

## When Helping Users
- Suggest notebook-style code with markdown explanations between cells
- Prefer synthetic data generation over downloading datasets
- Use scikit-learn for classical ML, PyTorch for deep learning
- Follow PEP 8 style, use type hints where practical
- For deployment, prefer FastAPI over Flask
