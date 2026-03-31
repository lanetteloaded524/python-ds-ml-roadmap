# 🐍 Python Data Science & ML Roadmap

**A structured, hands-on learning path from Python basics to production ML.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/github/license/djordjeperovic/python-ds-ml-roadmap?color=green)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?logo=github)
![Stars](https://img.shields.io/github/stars/djordjeperovic/python-ds-ml-roadmap?style=social)

---

## 📖 Overview

This repository is a comprehensive, open-source learning roadmap for Python Data Science and Machine Learning. It includes hands-on tutorial notebooks, a production-ready deployment project, and quick-reference cheat sheets — everything you need to go from beginner to job-ready. Whether you're a self-taught learner, a career switcher, or a student looking for structured practice, this roadmap has you covered.

---

## 📦 What's Inside

| # | Project | Phase | Topics | Notebook | Colab |
|---|---------|-------|--------|----------|-------|
| 1 | **Data Fundamentals** | Data Wrangling | NumPy, Pandas, Matplotlib, Seaborn | [`data_fundamentals.ipynb`](projects/01_data_fundamentals/data_fundamentals.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/01_data_fundamentals/data_fundamentals.ipynb) |
| 2 | **ML Fundamentals** | Classical ML | Regression, Classification, Clustering (scikit-learn) | [`ml_fundamentals.ipynb`](projects/02_ml_fundamentals/ml_fundamentals.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/02_ml_fundamentals/ml_fundamentals.ipynb) |
| 3 | **Deep Learning** | Neural Networks | PyTorch Tensors, MLP, CNN | [`deep_learning.ipynb`](projects/03_deep_learning/deep_learning.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/03_deep_learning/deep_learning.ipynb) |
| 4 | **Advanced ML** | Production ML | XGBoost, LightGBM, Pipelines, SMOTE | [`advanced_ml.ipynb`](projects/04_advanced_ml/advanced_ml.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/04_advanced_ml/advanced_ml.ipynb) |
| 5 | **NLP** | Text & Language | TF-IDF, Sentiment Analysis, Text Preprocessing | [`nlp_fundamentals.ipynb`](projects/05_nlp/nlp_fundamentals.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/05_nlp/nlp_fundamentals.ipynb) |
| 6 | **MLOps & Deployment** | Serving Models | FastAPI, Docker, Testing, CI/CD | [`06_mlops_deployment/`](projects/06_mlops_deployment/) | — |
| 📄 | **Cheat Sheets** | Reference | NumPy, Pandas, scikit-learn, PyTorch | [`cheat_sheets/`](cheat_sheets/) | — |

---

## 🗺️ Learning Roadmap

```
Phase 1    Phase 2    Phase 3      Phase 4      Phase 5
Python ──▶ Math &  ──▶ Data     ──▶ Classical ──▶ Deep
Basics     Stats      Wrangling    ML           Learning
                                                   │
Phase 10   Phase 9    Phase 8      Phase 7      Phase 6
Portfolio◀── Career ◀── MLOps & ◀── Computer ◀── NLP &
& Resume    Prep      Deployment   Vision       Text
```

> 📘 See [`ROADMAP.md`](ROADMAP.md) for the full 10-phase roadmap with curated resources, project ideas, and milestones.

---

## 🚀 Quick Start

```bash
git clone https://github.com/djordjeperovic/python-ds-ml-roadmap.git
cd python-ds-ml-roadmap
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
jupyter notebook
```

---

## 🔬 Project Details

### 📊 01 — Data Fundamentals

Master the core data stack: NumPy for numerical computing, Pandas for data manipulation, and Matplotlib/Seaborn for visualization. This notebook walks you through real-world data wrangling workflows.

- Array operations, broadcasting, and linear algebra with **NumPy**
- DataFrames, groupby, merging, and time series with **Pandas**
- Statistical plots, heatmaps, and custom styling with **Matplotlib & Seaborn**

### 🤖 02 — ML Fundamentals

Build, evaluate, and compare classical machine learning models using scikit-learn. Covers the full modeling lifecycle from preprocessing to evaluation.

- Linear & logistic regression, decision trees, SVMs
- K-Means clustering and dimensionality reduction
- Cross-validation, hyperparameter tuning, and metrics

### 🧠 03 — Deep Learning

Dive into neural networks with PyTorch — from tensor basics to training convolutional networks. Designed for learners transitioning from classical ML.

- Tensor operations, autograd, and GPU acceleration
- Multi-layer perceptrons (MLP) for tabular data
- Convolutional Neural Networks (CNN) for image tasks

### ⚡ 04 — Advanced ML

Level up with gradient boosting, imbalanced-data techniques, and production-grade pipelines. Covers the tools used in real-world ML competitions and teams.

- **XGBoost** and **LightGBM** for high-performance modeling
- Handling class imbalance with **SMOTE**
- End-to-end scikit-learn **Pipelines** and feature engineering

### 💬 05 — NLP

Explore Natural Language Processing from text preprocessing to sentiment analysis. Learn how to transform raw text into features for machine learning.

- Tokenization, stopwords, stemming, and lemmatization
- Bag-of-Words and **TF-IDF** vectorization
- Sentiment analysis on real-world datasets

### 🚢 06 — MLOps & Deployment

Ship a trained model as a REST API using FastAPI and Docker. This project includes tests, a Dockerfile, and a clean project structure ready for production.

- **FastAPI** application with prediction endpoints
- **Docker** containerization for reproducible deployment
- Automated testing with **pytest**

---

## 📝 Cheat Sheets

Quick-reference guides for the most-used libraries:

| Cheat Sheet | Link |
|-------------|------|
| NumPy | [`numpy_cheatsheet.md`](cheat_sheets/numpy_cheatsheet.md) |
| Pandas | [`pandas_cheatsheet.md`](cheat_sheets/pandas_cheatsheet.md) |
| scikit-learn | [`sklearn_cheatsheet.md`](cheat_sheets/sklearn_cheatsheet.md) |
| PyTorch | [`pytorch_cheatsheet.md`](cheat_sheets/pytorch_cheatsheet.md) |

---

## ✅ Prerequisites

- Basic Python knowledge (variables, loops, functions, file I/O)
- A working Python 3.10+ installation
- Familiarity with the command line

---

## 🤝 Contributing

Contributions are welcome! Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for guidelines on how to get involved.

---

## 📄 License

This project is licensed under the MIT License — see the [`LICENSE`](LICENSE) file for details.

---

## 👤 Author

Made by [@djordjeperovic](https://github.com/djordjeperovic)

---

If this roadmap helped you, consider giving it a ⭐ — it helps others find it too!
