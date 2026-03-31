# Copilot Instructions for python-ds-ml-roadmap

## Project Overview
This is an educational repository providing a structured learning path for Data Science and Machine Learning using Python. It contains Jupyter notebook tutorials, exercises with solutions, a FastAPI model deployment project, cheat sheets, a portfolio guide, and a full documentation site.

## Repository Structure
- `projects/00_math_and_stats/` — Statistics, distributions, hypothesis testing, Bayes, linear algebra
- `projects/01_data_fundamentals/` — NumPy, Pandas, Matplotlib, Seaborn tutorial
- `projects/01b_eda_case_study/` — Exploratory data analysis on a messy dataset
- `projects/02_ml_fundamentals/` — scikit-learn ML (regression, classification, clustering)
- `projects/03_deep_learning/` — PyTorch deep learning (tensors, MLP, CNN)
- `projects/03b_computer_vision/` — Image classification with PyTorch CNN
- `projects/04_advanced_ml/` — XGBoost, LightGBM, pipelines, imbalanced data
- `projects/05_nlp/` — NLP text processing, TF-IDF, sentiment analysis
- `projects/06_mlops_deployment/` — FastAPI + Docker model serving project
- `projects/07_portfolio/` — Portfolio building and career guide
- `exercises/` — Practice exercises with solutions for each notebook
- `cheat_sheets/` — Quick-reference markdown guides (NumPy, Pandas, scikit-learn, PyTorch)
- `docs/` — mkdocs-material documentation site source
- `ROADMAP.md` — Full 10-phase learning roadmap with resources
- `PROGRESS.md` — Fork-friendly learning progress tracker

## Key Conventions
- All notebooks use **synthetic data** — no external downloads required
- Notebooks are created programmatically via `nbformat` and validated with `jupyter nbconvert --execute`
- Notebook outputs are stripped via `nbstripout` (configured in `.gitattributes`)
- The MLOps project uses FastAPI with Pydantic schemas and async test patterns
- Python 3.10+ is required; PyTorch is CPU-only by default
- Random seeds are set for reproducibility (`np.random.seed(42)`, `torch.manual_seed(42)`)
- CI validates notebooks via GitHub Actions (`.github/workflows/validate-notebooks.yml`)

## When Helping Users
- Suggest notebook-style code with markdown explanations between cells
- Prefer synthetic data generation over downloading datasets
- Use scikit-learn for classical ML, PyTorch for deep learning
- Follow PEP 8 style, use type hints where practical
- For deployment, prefer FastAPI over Flask
- Exercise solutions should include both code and explanatory markdown
