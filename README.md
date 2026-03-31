# 🐍 Python Data Science & ML Roadmap

**A structured, hands-on learning path from Python basics to production ML.**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/github/license/djordjeperovic/python-ds-ml-roadmap?color=green)
![CI](https://img.shields.io/github/actions/workflow/status/djordjeperovic/python-ds-ml-roadmap/validate-notebooks.yml?label=CI&logo=github)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?logo=github)
![Stars](https://img.shields.io/github/stars/djordjeperovic/python-ds-ml-roadmap?style=social)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/djordjeperovic/python-ds-ml-roadmap)

---

## 📖 Overview

This repository is a comprehensive, open-source learning roadmap for Python Data Science and Machine Learning. It includes hands-on tutorial notebooks, a production-ready deployment project, and quick-reference cheat sheets — everything you need to go from beginner to job-ready. Whether you're a self-taught learner, a career switcher, or a student looking for structured practice, this roadmap has you covered.

---

## 📦 What's Inside

| # | Project | Phase | Topics | Notebook | Colab |
|---|---------|-------|--------|----------|-------|
| 0 | **Math & Statistics** | Foundations | Distributions, Hypothesis Testing, Bayes, Linear Algebra | [`statistics_for_ml.ipynb`](projects/00_math_and_stats/statistics_for_ml.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/00_math_and_stats/statistics_for_ml.ipynb) |
| 1 | **Data Fundamentals** | Data Wrangling | NumPy, Pandas, Matplotlib, Seaborn | [`data_fundamentals.ipynb`](projects/01_data_fundamentals/data_fundamentals.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/01_data_fundamentals/data_fundamentals.ipynb) |
| 1b | **EDA Case Study** | Exploratory Analysis | Missing Values, Outliers, Feature Engineering | [`eda_case_study.ipynb`](projects/01b_eda_case_study/eda_case_study.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/01b_eda_case_study/eda_case_study.ipynb) |
| 2 | **ML Fundamentals** | Classical ML | Regression, Classification, Clustering (scikit-learn) | [`ml_fundamentals.ipynb`](projects/02_ml_fundamentals/ml_fundamentals.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/02_ml_fundamentals/ml_fundamentals.ipynb) |
| 3 | **Deep Learning** | Neural Networks | PyTorch Tensors, MLP, CNN | [`deep_learning.ipynb`](projects/03_deep_learning/deep_learning.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/03_deep_learning/deep_learning.ipynb) |
| 3b | **Computer Vision** | Image Classification | Convolutions, Feature Maps, CNN Training | [`computer_vision.ipynb`](projects/03b_computer_vision/computer_vision.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/03b_computer_vision/computer_vision.ipynb) |
| 4 | **Advanced ML** | Production ML | XGBoost, LightGBM, Pipelines, SMOTE | [`advanced_ml.ipynb`](projects/04_advanced_ml/advanced_ml.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/04_advanced_ml/advanced_ml.ipynb) |
| 5 | **NLP** | Text & Language | TF-IDF, Sentiment Analysis, Text Preprocessing | [`nlp_fundamentals.ipynb`](projects/05_nlp/nlp_fundamentals.ipynb) | [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/projects/05_nlp/nlp_fundamentals.ipynb) |
| 6 | **MLOps & Deployment** | Serving Models | FastAPI, Docker, Testing, CI/CD | [`06_mlops_deployment/`](projects/06_mlops_deployment/) | — |
| 7 | **Portfolio Guide** | Career | GitHub Profile, Resume, Interviews | [`portfolio_guide.md`](projects/07_portfolio/portfolio_guide.md) | — |
| 📄 | **Cheat Sheets** | Reference | NumPy, Pandas, scikit-learn, PyTorch | [`cheat_sheets/`](cheat_sheets/) | — |
| 🏋️ | **Exercises** | Practice | 22 exercises with solutions | [`exercises/`](exercises/) | — |
| 📋 | **Progress Tracker** | Self-paced | Fork & track your learning | [`PROGRESS.md`](PROGRESS.md) | — |

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

### 📐 00 — Math & Statistics for ML

Build the mathematical foundation every ML practitioner needs. Covers the core concepts with intuitive explanations and visual demonstrations.

- Descriptive statistics, probability distributions, and the **Central Limit Theorem**
- Hypothesis testing (t-test, chi-square) and **p-values**
- **Bayes' theorem** and its connection to Naive Bayes
- Linear algebra essentials (vectors, matrices, eigenvalues)

### 📊 01 — Data Fundamentals

Master the core data stack: NumPy for numerical computing, Pandas for data manipulation, and Matplotlib/Seaborn for visualization. This notebook walks you through real-world data wrangling workflows.

- Array operations, broadcasting, and linear algebra with **NumPy**
- DataFrames, groupby, merging, and time series with **Pandas**
- Statistical plots, heatmaps, and custom styling with **Matplotlib & Seaborn**

### 🔍 01b — EDA Case Study

Practice real-world exploratory data analysis on a deliberately messy dataset. Learn the detective mindset of data cleaning and insight discovery.

- Data quality assessment: missing values, outliers, duplicates, inconsistent categories
- Univariate and bivariate analysis with publication-quality visualizations
- **Feature engineering** from raw data to ML-ready features

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

### 👁️ 03b — Computer Vision

Apply deep learning to image classification with PyTorch. Build, train, and evaluate CNNs on synthetic geometric shape data.

- Image fundamentals: tensors, channels, and **torchvision transforms**
- Convolutional operations: kernels, feature maps, pooling
- End-to-end CNN training with evaluation and prediction visualization

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

### 🎯 07 — Portfolio Guide

A comprehensive guide to building your data science portfolio and launching your career. Covers GitHub profile, project selection, resume tips, and interview prep.

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

## 📚 Recommended Resources

**YouTube Channels:**
- [3Blue1Brown](https://www.youtube.com/c/3blue1brown) — Visual math & linear algebra intuition
- [StatQuest](https://www.youtube.com/c/joshstarmer) — Statistics & ML concepts explained clearly
- [Sentdex](https://www.youtube.com/c/sentdex) — Hands-on Python ML tutorials

**Free Books:**
- [An Introduction to Statistical Learning (ISLR)](https://www.statlearning.com/) — The ML textbook
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) — NumPy, Pandas, Matplotlib, scikit-learn
- [Deep Learning (Goodfellow)](https://www.deeplearningbook.org/) — Comprehensive deep learning theory

**Practice Platforms:**
- [Kaggle](https://www.kaggle.com/) — Competitions, datasets, and community notebooks
- [LeetCode](https://leetcode.com/) — Coding interview preparation
- [StrataScratch](https://www.stratascratch.com/) — Real DS interview questions

> 📘 See [`ROADMAP.md`](ROADMAP.md) for a complete resource list organized by phase.

---

## 🧭 What Should I Learn Next?

Not sure where to go after the basics? Use this guide:

```
Completed ML Fundamentals (Phase 5)?
│
├── 🖼️  Interested in images?
│   └── Computer Vision notebook → Deep Learning
│
├── 💬  Interested in text?
│   └── NLP notebook → (LLM notebook coming soon)
│
├── 📊  Interested in tabular data / competitions?
│   └── Advanced ML → EDA Case Study → Kaggle
│
├── 🚀  Want to deploy models?
│   └── MLOps & Deployment project → Docker → CI/CD
│
├── 📈  Interested in forecasting?
│   └── Time Series (coming soon)
│
└── 💼  Want to get hired?
    └── Portfolio Guide → Resume → Interview Prep
```

> 💡 **Tip:** You don't need to follow a strict order. Pick what excites you — motivation beats sequence every time.

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
