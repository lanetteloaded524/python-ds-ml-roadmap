---
title: Full Learning Roadmap
---
# How to Learn Data Science & Machine Learning Using Python: Beginner to Advanced

> **A comprehensive, step-by-step learning plan for someone who already knows basic Python.**

---

## Executive Summary

This guide provides a structured, 10-phase learning roadmap for mastering Data Science (DS) and Machine Learning (ML) using Python—starting from foundational math and data skills all the way through deep learning, NLP, computer vision, and production deployment (MLOps). Each phase includes specific topics to study, the best free and paid resources, recommended libraries, hands-on projects, and estimated effort. The plan assumes you already know basic Python (variables, loops, functions, file I/O) and is designed for self-paced learning over approximately 9–12 months of consistent study[^1][^2][^3].

---

## Learning Roadmap Overview

```
Phase 1: Python for DS/ML (2–3 weeks)
    │
Phase 2: Mathematics Foundations (4–6 weeks)
    │
Phase 3: Core Data Libraries — NumPy, Pandas, Matplotlib (3–4 weeks)
    │
Phase 4: Data Wrangling & EDA (2–3 weeks)
    │
Phase 5: Machine Learning Fundamentals with scikit-learn (6–8 weeks)
    │
Phase 6: Advanced ML & Feature Engineering (4–6 weeks)
    │
Phase 7: Deep Learning — Neural Networks, CNNs, RNNs (6–8 weeks)
    │
Phase 8: Specializations — NLP, Computer Vision, Time Series (6–8 weeks)
    │
Phase 9: MLOps & Model Deployment (3–4 weeks)
    │
Phase 10: Portfolio, Kaggle & Continuous Learning (Ongoing)
```

---

## Phase 1: Strengthen Python for Data Science & ML

**Goal:** Bridge the gap between "basic Python" and "Python for DS/ML."

### What to Learn

| Topic | Why It Matters |
|-------|---------------|
| List/dict comprehensions | Concise data transformations |
| Lambda functions, `map`, `filter` | Functional patterns used in data pipelines |
| Object-Oriented Programming (classes, inheritance) | Understanding ML library internals |
| File I/O (CSV, JSON, APIs) | Loading real-world data |
| Virtual environments (`venv`, `conda`) | Reproducible project setup |
| Jupyter Notebooks & VS Code | Standard DS development environments |
| Error handling & debugging | Production-quality code |

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [Python for Everybody](https://www.py4e.com/) by Charles Severance | Book (free online) | Free |
| [freeCodeCamp: Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) | Course + Certificate | Free |
| [Coursera: Python for Data Science, AI & Development (IBM)](https://www.coursera.org/learn/python-for-applied-data-science-ai) | Course | Free to audit |
| [Real Python](https://realpython.com/) | Tutorials | Free/Paid |

### Mini-Project
- Build a CLI tool that reads a CSV file, performs basic filtering/aggregation, and writes results to a new file.

---

## Phase 2: Mathematics Foundations

**Goal:** Build the mathematical intuition required to understand ML algorithms, not just use them.

> ⚠️ **You don't need a math degree.** Focus on *applied* understanding—enough to know what an algorithm does and why, and to debug when things go wrong.

### 2A: Statistics & Probability (Weeks 1–3)

| Topic | Application in ML |
|-------|-------------------|
| Descriptive statistics (mean, median, variance, std dev) | Data exploration, feature understanding |
| Probability rules, Bayes' theorem | Naive Bayes, probabilistic models |
| Distributions (Normal, Binomial, Poisson) | Assumptions of many models |
| Hypothesis testing, p-values, confidence intervals | A/B testing, model evaluation |
| Correlation & covariance | Feature selection |

### 2B: Linear Algebra (Weeks 3–4)

| Topic | Application in ML |
|-------|-------------------|
| Vectors and matrices, operations | Data representation, transformations |
| Dot product and norms | Similarity measures, SVM |
| Eigenvalues & eigenvectors | PCA, dimensionality reduction |
| Matrix decomposition (SVD) | Recommender systems, data compression |

### 2C: Calculus (Weeks 5–6)

| Topic | Application in ML |
|-------|-------------------|
| Derivatives & partial derivatives | Gradient computation |
| Chain rule | Backpropagation in neural networks |
| Gradient descent & optimization | Training any ML model |

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [Mathematics for Machine Learning](https://mml-book.github.io/) by Deisenroth et al. | Book (free PDF) | Free |
| [DeepLearning.AI: Mathematics for ML & DS Specialization](https://www.deeplearning.ai/courses/mathematics-for-machine-learning-and-data-science-specialization/) | Coursera course | Free to audit |
| [Coursera: Mathematics for Machine Learning (Imperial College)](https://www.coursera.org/specializations/mathematics-machine-learning) | Course | Free to audit |
| [Khan Academy — Statistics & Probability, Linear Algebra](https://www.khanacademy.org/) | Video lessons | Free |
| [3Blue1Brown: Essence of Linear Algebra (YouTube)](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab) | Video series | Free |
| [GitHub: dair-ai/Mathematics-for-ML](https://github.com/dair-ai/Mathematics-for-ML) | Curated resources | Free |

### Mini-Project
- Implement gradient descent from scratch in Python (no libraries) to minimize a simple quadratic function. Visualize the descent path with Matplotlib[^4][^5][^6].

---

## Phase 3: Core Data Science Libraries

**Goal:** Master the Python data stack—NumPy, Pandas, and visualization tools.

### 3A: NumPy (Week 1)

NumPy is the foundation of numerical computing in Python. Every other library builds on it[^7].

**Key topics:**
- ndarray creation, indexing, slicing
- Vectorized operations (avoid for-loops!)
- Broadcasting
- Linear algebra operations (`np.dot`, `np.linalg`)
- Random number generation

```python
import numpy as np

# Vectorized operations — 100x faster than loops
data = np.random.randn(1000000)
mean = np.mean(data)
std = np.std(data)
normalized = (data - mean) / std
```

### 3B: Pandas (Weeks 2–3)

Pandas is the workhorse for data manipulation in Python[^8].

**Key topics:**
- Series and DataFrame creation
- Reading data: `read_csv`, `read_excel`, `read_sql`
- Indexing: `.loc`, `.iloc`, boolean indexing
- Data cleaning: handling missing values, duplicates, type conversion
- GroupBy, aggregation, pivot tables
- Merging, joining, concatenating DataFrames
- Time series basics

```python
import pandas as pd

df = pd.read_csv("sales_data.csv")
# Clean, transform, analyze
monthly_revenue = (
    df.dropna(subset=["revenue"])
      .assign(month=lambda x: pd.to_datetime(x["date"]).dt.month)
      .groupby("month")["revenue"]
      .sum()
)
```

### 3C: Data Visualization — Matplotlib & Seaborn (Week 4)

**Key topics:**
- Matplotlib: line, bar, scatter, histogram, subplots
- Seaborn: heatmaps, pair plots, distribution plots, box plots
- Customization: labels, legends, styles, colors

```python
import matplotlib.pyplot as plt
import seaborn as sns

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.histplot(df["age"], kde=True, ax=axes[0])
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=axes[1])
plt.tight_layout()
plt.show()
```

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake VanderPlas | Book (free online) | Free |
| [Python for Data Analysis](https://wesmckinney.com/book/) by Wes McKinney (creator of Pandas) | Book | Free online (3rd ed.) |
| [Data School: Pandas in 30 Days](https://courses.dataschool.io/free-courses) | Course | Free |
| [Kaggle Micro-Courses: Pandas, Data Visualization](https://www.kaggle.com/learn) | Interactive course | Free |

### Mini-Project
- Load a real dataset (e.g., [Kaggle's "World Happiness Report"](https://www.kaggle.com/datasets)), clean it, perform EDA, and create a dashboard of 5+ visualizations telling a data story[^9][^10].

---

## Phase 4: Data Wrangling & Exploratory Data Analysis (EDA)

**Goal:** Develop the practical skill of transforming messy, real-world data into clean, analysis-ready datasets.

### What to Learn

- **Data acquisition**: APIs (`requests`), web scraping (`BeautifulSoup`), SQL databases (`sqlite3`, `sqlalchemy`)
- **Data cleaning**: handling missing values (imputation strategies), outlier detection & treatment, fixing data types
- **Feature engineering**: creating new features from existing data, binning, encoding categorical variables (one-hot, label, target encoding)
- **EDA process**: univariate → bivariate → multivariate analysis, correlation analysis, distribution checks

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [Kaggle Micro-Course: Data Cleaning](https://www.kaggle.com/learn/data-cleaning) | Interactive course | Free |
| [Kaggle Micro-Course: Feature Engineering](https://www.kaggle.com/learn/feature-engineering) | Interactive course | Free |
| [freeCodeCamp: Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) | Course + Certificate | Free |

### Mini-Project
- Download a messy dataset (e.g., [Kaggle's "Housing Prices"](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)), handle 10+ missing-value columns, engineer at least 5 new features, and document your EDA findings in a Jupyter notebook.

---

## Phase 5: Machine Learning Fundamentals with scikit-learn

**Goal:** Understand and implement the core ML algorithms. This is the heart of the learning path.

### 5A: The ML Workflow

```
Raw Data → Preprocessing → Feature Engineering → Model Training → Evaluation → Tuning → Deployment
                                                       ↑_________↓
                                                    (iterate & improve)
```

### 5B: Supervised Learning — Regression

| Algorithm | When to Use | Key Concept |
|-----------|-------------|-------------|
| Linear Regression | Continuous target, linear relationships | Least squares, coefficients |
| Ridge / Lasso Regression | When features are correlated or you need regularization | L2 / L1 penalty |
| Decision Tree Regressor | Non-linear relationships, interpretability | Splits, depth, pruning |
| Random Forest Regressor | Robust predictions, reduced overfitting | Ensemble of trees, bagging |
| Gradient Boosting (XGBoost, LightGBM) | Competition-level accuracy on tabular data | Sequential tree building |

### 5C: Supervised Learning — Classification

| Algorithm | When to Use | Key Concept |
|-----------|-------------|-------------|
| Logistic Regression | Binary classification, baseline model | Sigmoid function, log-odds |
| k-Nearest Neighbors (k-NN) | Small datasets, non-parametric | Distance metrics |
| Support Vector Machines (SVM) | High-dimensional spaces, clear margins | Hyperplanes, kernels |
| Decision Trees & Random Forests | Interpretable models, feature importance | Gini impurity, entropy |
| Gradient Boosting (XGBoost, LightGBM, CatBoost) | State-of-the-art tabular data performance | Boosting, learning rate |

### 5D: Unsupervised Learning

| Algorithm | When to Use | Key Concept |
|-----------|-------------|-------------|
| K-Means Clustering | Customer segmentation, grouping | Centroids, inertia |
| Hierarchical Clustering | When you need dendrograms, variable clusters | Agglomerative, linkage |
| DBSCAN | Irregular cluster shapes, noise detection | Density, epsilon |
| PCA (Principal Component Analysis) | Dimensionality reduction, visualization | Eigenvalues, variance explained |
| t-SNE / UMAP | High-dim data visualization | Non-linear embedding |

### 5E: Model Evaluation & Selection

| Concept | Details |
|---------|---------|
| Train/Test Split | `train_test_split()` — never evaluate on training data |
| Cross-Validation | k-fold CV for robust performance estimates |
| Metrics — Regression | MSE, RMSE, MAE, R² |
| Metrics — Classification | Accuracy, Precision, Recall, F1, AUC-ROC, Confusion Matrix |
| Hyperparameter Tuning | `GridSearchCV`, `RandomizedSearchCV`, Optuna |
| Bias-Variance Tradeoff | Underfitting vs. overfitting |

```python
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Cross-validation
cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring="f1")
print(f"CV F1: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")

# Test evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
```

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/) by Aurélien Géron (3rd ed.) | Book | ~$50 |
| [Kaggle Micro-Course: Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning) | Interactive course | Free |
| [Kaggle Micro-Course: Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning) | Interactive course | Free |
| [DataCamp: Machine Learning Scientist Track](https://www.datacamp.com/tracks/machine-learning-scientist-with-python) | Course track | Paid |
| [Springboard: Free ML in Python Course](https://www.springboard.com/resources/learning-paths/machine-learning-python/) | Course | Free |
| [Data School: Intro to ML with scikit-learn](https://courses.dataschool.io/free-courses) | Course | Free |
| [scikit-learn Official Documentation & Tutorials](https://scikit-learn.org/stable/tutorial/) | Documentation | Free |

### Portfolio Projects (Beginner)

| Project | Skills Practiced |
|---------|------------------|
| **Titanic Survival Prediction** | Classification, feature engineering, missing data |
| **House Price Prediction** | Regression, feature engineering, evaluation metrics |
| **Iris Flower Classification** | Multi-class classification, visualization |
| **Customer Segmentation** | K-Means clustering, EDA |
| **Spam/Ham SMS Classification** | Text preprocessing, Naive Bayes, NLP intro |

[^11][^12]

---

## Phase 6: Advanced Machine Learning & Feature Engineering

**Goal:** Go beyond basics — learn ensemble methods, advanced feature engineering, and competition-winning techniques.

### What to Learn

- **Ensemble Methods**: Bagging, Boosting, Stacking
- **Gradient Boosting Libraries**: XGBoost, LightGBM, CatBoost
- **Advanced Feature Engineering**: target encoding, feature interactions, polynomial features, time-based features
- **Handling Imbalanced Data**: SMOTE, class weights, threshold tuning
- **Pipelines**: `sklearn.pipeline.Pipeline` for reproducible workflows
- **Automated ML (AutoML)**: TPOT, Auto-sklearn (awareness, not dependency)

```python
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("model", XGBClassifier(n_estimators=500, learning_rate=0.05, max_depth=6))
])

pipeline.fit(X_train, y_train)
```

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [XGBoost Documentation](https://xgboost.readthedocs.io/) | Documentation | Free |
| [LightGBM Documentation](https://lightgbm.readthedocs.io/) | Documentation | Free |
| [Kaggle: Feature Engineering Micro-Course](https://www.kaggle.com/learn/feature-engineering) | Interactive | Free |
| [Machine Learning Mastery Blog](https://machinelearningmastery.com/) | Tutorials | Free |

### Portfolio Projects (Intermediate)

| Project | Skills Practiced |
|---------|------------------|
| **Sentiment Analysis** (Movie/Tweet Reviews) | NLP, text processing, TF-IDF |
| **Fake News Detection** | Ensemble models, NLP pipeline |
| **Customer Churn Prediction** | Imbalanced data, business metrics |
| **Credit Card Fraud Detection** | Extreme class imbalance, precision/recall |
| **Recommendation System** | Collaborative filtering, matrix factorization |
| **Time Series Forecasting** | ARIMA, Prophet, temporal features |

[^13][^14]

---

## Phase 7: Deep Learning — Neural Networks

**Goal:** Understand and implement neural networks using PyTorch and/or TensorFlow/Keras.

### 7A: Neural Network Fundamentals

- Perceptrons and multi-layer perceptrons (MLPs)
- Activation functions (ReLU, Sigmoid, Softmax)
- Loss functions (Cross-Entropy, MSE)
- Backpropagation and gradient descent
- Optimizers (SGD, Adam, AdamW)
- Regularization (Dropout, Batch Normalization, Early Stopping)

### 7B: PyTorch vs. TensorFlow — Which to Learn?

| Aspect | PyTorch | TensorFlow / Keras |
|--------|---------|-------------------|
| Learning curve | Pythonic, intuitive | High-level Keras API is easy |
| Research popularity | Dominant in academia | Strong in industry/production |
| Dynamic graphs | Yes (default) | Yes (eager mode, default since 2.x) |
| Deployment | TorchServe, ONNX | TF Serving, TFLite, TF.js |
| Recommendation | **Start here** for research & flexibility | Learn second for deployment skills |

> **Recommendation**: Learn **PyTorch first** (dominant in research and increasingly in industry), then pick up TensorFlow/Keras for deployment scenarios[^15][^16].

### 7C: Convolutional Neural Networks (CNNs) — Computer Vision

- Convolution, pooling, feature maps
- Architectures: LeNet, VGG, ResNet, EfficientNet
- Transfer learning (using pretrained models)
- Data augmentation

### 7D: Recurrent Neural Networks (RNNs) — Sequence Data

- Vanilla RNNs, vanishing gradient problem
- LSTM and GRU cells
- Sequence-to-sequence models
- (Largely superseded by Transformers for NLP, but important to understand)

```python
import torch
import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, output_dim)
        )
    
    def forward(self, x):
        return self.net(x)

model = SimpleNN(784, 256, 10)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
```

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [MIT 6.S191: Introduction to Deep Learning](https://introtodeeplearning.com/) | University course (free) | Free |
| [DeepLearning.AI: Deep Learning Specialization](https://www.deeplearning.ai/courses/deep-learning-specialization/) (Andrew Ng) | Coursera | Free to audit |
| [Dive into Deep Learning (d2l.ai)](https://d2l.ai/) | Interactive book (PyTorch/TF/JAX) | Free |
| [PyTorch Official Tutorials](https://pytorch.org/tutorials/) | Documentation | Free |
| [TensorFlow Official Tutorials](https://www.tensorflow.org/tutorials) | Documentation | Free |
| [Learning Deep Learning (LDL)](https://ldlbook.com/) | Book | ~$40 |

[^17][^18]

---

## Phase 8: Specializations

Choose one or more areas based on your interests and career goals.

### 8A: Natural Language Processing (NLP)

**Learning Path:**
1. Text preprocessing: tokenization, stemming, lemmatization
2. Bag of Words, TF-IDF
3. Word embeddings: Word2Vec, GloVe
4. Transformer architecture (self-attention, positional encoding)
5. Pre-trained models: BERT, GPT, RoBERTa, T5
6. Hugging Face `transformers` library
7. Fine-tuning LLMs, PEFT (LoRA, QLoRA)
8. Prompt engineering

```python
from transformers import pipeline

# Sentiment analysis with a pre-trained model — 3 lines of code
classifier = pipeline("sentiment-analysis")
result = classifier("I love learning machine learning with Python!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.9998}]
```

**Resources:**
- [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) (free lectures & materials)
- [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course) (free)
- [PyTorch NLP Tutorials](https://pytorch.org/tutorials/beginner/nlp/index.html) (free)
- [Codecademy: Neural Networks with PyTorch and Transformers](https://www.codecademy.com/learn/paths/engineer-neural-networks-with-py-torch-and-transformers)

### 8B: Computer Vision

**Learning Path:**
1. Image preprocessing, augmentation
2. CNN architectures (ResNet, EfficientNet, YOLO)
3. Object detection, segmentation
4. Transfer learning with pre-trained models
5. Vision Transformers (ViT)
6. Multimodal models (CLIP)

**Resources:**
- [Stanford CS231N: Convolutional Neural Networks](http://cs231n.stanford.edu/) (free lectures)
- [Coursera: Building Vision Workflows with TensorFlow](https://www.coursera.org/learn/building-vision-and-nlp-workflows-with-tensorflow-pipelines)
- OpenCV documentation and tutorials

### 8C: Time Series Analysis

**Learning Path:**
1. Time series decomposition (trend, seasonality, residual)
2. Stationarity, ACF/PACF
3. ARIMA, SARIMA
4. Facebook Prophet
5. Deep learning for time series (LSTM, Temporal Fusion Transformer)

### 8D: Generative AI & LLMs (2025+ Hot Topic)

**Learning Path:**
1. Understand transformer architecture deeply
2. GPT, Llama, Mistral model families
3. Fine-tuning with Hugging Face
4. Parameter-efficient fine-tuning (PEFT, LoRA, QLoRA)
5. Retrieval-Augmented Generation (RAG)
6. LangChain / LlamaIndex frameworks

[^19][^20][^21]

---

## Phase 9: MLOps & Model Deployment

**Goal:** Learn to take models from notebooks to production.

### Deployment Stack

```
┌─────────────────┐     ┌──────────────┐     ┌──────────────┐
│  Model Training │────▶│  API Server  │────▶│  Production  │
│  (Jupyter/Script)│     │ (FastAPI)    │     │  (Docker +   │
└─────────────────┘     └──────────────┘     │   Cloud)     │
        │                       │             └──────────────┘
        ▼                       ▼
┌─────────────────┐     ┌──────────────┐
│  Model Registry │     │  Monitoring  │
│  (MLflow)       │     │  & Logging   │
└─────────────────┘     └──────────────┘
```

### What to Learn

| Topic | Tools | Priority |
|-------|-------|----------|
| Version control | Git, GitHub | Essential |
| Model serialization | `pickle`, `joblib`, ONNX | Essential |
| REST API serving | **FastAPI** (preferred in 2025), Flask | Essential |
| Containerization | Docker, Docker Compose | Essential |
| Experiment tracking | MLflow, Weights & Biases | Important |
| CI/CD | GitHub Actions | Important |
| Cloud deployment | AWS (SageMaker, EC2), GCP, Azure | Nice-to-have |
| Orchestration | Kubernetes (awareness) | Advanced |

### FastAPI Example

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

class PredictionRequest(BaseModel):
    features: list[float]

@app.post("/predict")
def predict(request: PredictionRequest):
    prediction = model.predict([request.features])
    return {"prediction": prediction[0]}
```

### Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Resources

| Resource | Type | Cost |
|----------|------|------|
| [ML Mastery: Deploying with FastAPI & Docker](https://machinelearningmastery.com/step-by-step-guide-to-deploying-machine-learning-models-with-fastapi-and-docker/) | Tutorial | Free |
| [GeeksforGeeks: End-to-End MLOps Pipeline](https://www.geeksforgeeks.org/machine-learning/end-to-end-mlops-pipeline-a-comprehensive-project/) | Tutorial | Free |
| [GitHub: MLOps FastAPI Microservice Template](https://github.com/ivesfurtado/mlops-fastapi-microservice) | Repo template | Free |
| [MLflow Documentation](https://mlflow.org/docs/latest/) | Documentation | Free |
| [Docker Official Getting Started](https://docs.docker.com/get-started/) | Documentation | Free |

[^22][^23][^24]

---

## Phase 10: Portfolio Building, Kaggle & Continuous Learning

### Building Your Portfolio

**Structure each project with:**
1. **README.md** — Problem statement, approach, results, how to run
2. **Notebook** — Full EDA, modeling, and analysis
3. **Source code** — Clean, modular Python scripts
4. **Results** — Visualizations, metrics, business insights

**Portfolio progression:**

| Level | Projects | What It Demonstrates |
|-------|----------|---------------------|
| Beginner (3–4 projects) | Titanic, House Prices, Iris, Customer Segmentation | Core ML skills, data cleaning, EDA |
| Intermediate (2–3 projects) | Sentiment Analysis, Churn Prediction, Recommendation System | NLP, business problems, advanced models |
| Advanced (1–2 projects) | End-to-end deployed model, Fine-tuned LLM, Real-time system | Production skills, deep learning, MLOps |

### Kaggle Strategy for Beginners

1. **Start with "Getting Started" competitions** (Titanic, House Prices, Digit Recognizer)[^25]
2. **Complete Kaggle Micro-Courses** (Python, Pandas, ML, Feature Engineering)
3. **Study top notebooks** — learn from Kaggle Grandmasters
4. **Iterate**: Submit → Analyze leaderboard → Improve features → Resubmit
5. **Join discussions** — the community is incredibly helpful
6. **Progress to real competitions** once comfortable with the workflow

### Staying Current

| Activity | Frequency | Where |
|----------|-----------|-------|
| Read research summaries | Weekly | [Papers With Code](https://paperswithcode.com/), [arXiv Sanity](https://arxiv-sanity-lite.com/) |
| Follow ML blogs | Weekly | [Towards Data Science](https://towardsdatascience.com/), [Machine Learning Mastery](https://machinelearningmastery.com/) |
| Watch conference talks | Monthly | NeurIPS, ICML, PyData on YouTube |
| Build projects | Ongoing | GitHub portfolio |
| Contribute to open-source | When ready | scikit-learn, Hugging Face, PyTorch |

[^26][^27]

---

## Complete Library Reference

| Library | Purpose | Phase to Learn |
|---------|---------|---------------|
| **NumPy** | Numerical computing, arrays | Phase 3 |
| **Pandas** | Data manipulation, DataFrames | Phase 3 |
| **Matplotlib** | Basic plotting | Phase 3 |
| **Seaborn** | Statistical visualization | Phase 3 |
| **scikit-learn** | Classical ML algorithms | Phase 5 |
| **XGBoost / LightGBM / CatBoost** | Gradient boosting | Phase 6 |
| **PyTorch** | Deep learning (research-focused) | Phase 7 |
| **TensorFlow / Keras** | Deep learning (production-focused) | Phase 7 |
| **Hugging Face Transformers** | Pre-trained NLP/CV models | Phase 8 |
| **spaCy / NLTK** | NLP text processing | Phase 8 |
| **OpenCV** | Computer vision | Phase 8 |
| **FastAPI** | Model serving API | Phase 9 |
| **Docker** | Containerization | Phase 9 |
| **MLflow** | Experiment tracking | Phase 9 |
| **Optuna** | Hyperparameter optimization | Phase 6 |

---

## Recommended Learning Schedule

| Week | Phase | Focus |
|------|-------|-------|
| 1–3 | Phase 1 | Python for DS/ML |
| 4–9 | Phase 2 | Mathematics foundations |
| 10–13 | Phase 3 | NumPy, Pandas, Visualization |
| 14–16 | Phase 4 | Data wrangling & EDA |
| 17–24 | Phase 5 | ML fundamentals with scikit-learn |
| 25–30 | Phase 6 | Advanced ML & feature engineering |
| 31–38 | Phase 7 | Deep learning (PyTorch / TensorFlow) |
| 39–46 | Phase 8 | Specialization (NLP / CV / Time Series) |
| 47–50 | Phase 9 | MLOps & deployment |
| 51+ | Phase 10 | Portfolio, Kaggle, continuous learning |

> **Note:** This schedule assumes ~10–15 hours per week of study. Adjust based on your availability. Consistency matters more than intensity.

---

## Top 10 Free Resources (Summary)

| # | Resource | What It Covers | Link |
|---|----------|---------------|------|
| 1 | **Kaggle Learn** | Python, Pandas, ML, Feature Engineering, DL | [kaggle.com/learn](https://www.kaggle.com/learn) |
| 2 | **Python Data Science Handbook** | NumPy, Pandas, Matplotlib, scikit-learn | [jakevdp.github.io](https://jakevdp.github.io/PythonDataScienceHandbook/) |
| 3 | **Mathematics for Machine Learning** (book) | Linear Algebra, Calculus, Statistics for ML | [mml-book.github.io](https://mml-book.github.io/) |
| 4 | **freeCodeCamp** | Python, Scientific Computing, Data Analysis | [freecodecamp.org](https://www.freecodecamp.org/) |
| 5 | **MIT 6.S191** | Deep Learning (with code labs) | [introtodeeplearning.com](https://introtodeeplearning.com/) |
| 6 | **Dive into Deep Learning** | Neural Networks, CNNs, RNNs, Transformers | [d2l.ai](https://d2l.ai/) |
| 7 | **Stanford CS224N** | NLP with Deep Learning | [web.stanford.edu/class/cs224n](https://web.stanford.edu/class/cs224n/) |
| 8 | **Hugging Face NLP Course** | Transformers, fine-tuning, deployment | [huggingface.co/learn](https://huggingface.co/learn/nlp-course) |
| 9 | **scikit-learn Docs** | Official ML library documentation & tutorials | [scikit-learn.org](https://scikit-learn.org/stable/tutorial/) |
| 10 | **DeepLearning.AI Specializations** | ML, DL, Math (free to audit on Coursera) | [deeplearning.ai](https://www.deeplearning.ai/) |

---

## Confidence Assessment

| Aspect | Confidence | Notes |
|--------|------------|-------|
| Learning path structure | **High** | Consistent across 10+ authoritative sources |
| Library recommendations | **High** | NumPy/Pandas/scikit-learn/PyTorch/TF are undisputed pillars |
| Resource recommendations | **High** | Cross-referenced from multiple 2025–2026 curated lists |
| Time estimates | **Medium** | Varies widely based on prior experience and study hours |
| Career applicability | **High** | Aligns with current industry job requirements |

---

## Footnotes

[^1]: [Coursera: Comprehensive Python Learning Path](https://www.coursera.org/resources/python-learning-roadmap) — Full beginner-to-expert Python roadmap for data science
[^2]: [Machine Learning Mastery: Roadmap to Python in 2025](https://machinelearningmastery.com/roadmap-to-python-in-2025/) — Step-by-step learning plan with tool recommendations
[^3]: [Apponix: Step-by-Step Roadmap to Learn Data Science with Python](https://www.apponix.com/blog/step-by-step-roadmap-to-learn-data-science-with-python) — Detailed phase-by-phase DS learning guide
[^4]: [GeeksforGeeks: Maths for Machine Learning](https://www.geeksforgeeks.org/machine-learning/machine-learning-mathematics/) — Comprehensive math prerequisites guide
[^5]: [Mathematics for Machine Learning (free book)](https://mml-book.github.io/book/mml-book.pdf) — Deisenroth, Faisal, Ong — standard reference text
[^6]: [DeepLearning.AI: Mathematics for ML & DS Specialization](https://www.deeplearning.ai/courses/mathematics-for-machine-learning-and-data-science-specialization/) — Coursera specialization by Andrew Ng's team
[^7]: [Top Python Libraries for Data Science and AI in 2025](https://www.fyld.pt/blog/python-libraries-data-science-ai-in-2025/) — NumPy, Pandas as foundational pillars
[^8]: [Essential Python Libraries for Data Science 2025 (Nimap)](https://nimapinfotech.com/blog/popular-python-libraries-for-data-science/) — Pandas with Arrow support and GPU acceleration
[^9]: [Statology: 10 Free Must-Read Books for Python & Data Science](https://www.statology.org/10-free-must-read-books-for-python-programming-and-data-science/) — Curated free book list
[^10]: [Analytics Vidhya: Top 10 Free Data Science eBooks](https://www.analyticsvidhya.com/blog/2024/03/best-free-data-science-ebooks/) — Free ebook recommendations
[^11]: [Anaconda: 7 Must-Know ML Libraries in 2025](https://www.anaconda.com/guides/machine-learning-libraries) — scikit-learn, PyTorch, TensorFlow overview
[^12]: [Machine Learning Mastery: 10 Must-Know Python Libraries for ML](https://machinelearningmastery.com/10-must-know-python-libraries-for-machine-learning-in-2025/) — Complete library guide with use cases
[^13]: [Udacity: 10 Machine Learning Projects That Boost Your Portfolio](https://www.udacity.com/blog/2025/06/10-machine-learning-projects-that-will-boost-your-portfolio.html) — Portfolio project recommendations
[^14]: [365 Data Science: Top 10 ML Project Ideas](https://365datascience.com/tutorials/machine-learning-tutorials/machine-learning-project-ideas/) — Beginner to advanced project ideas
[^15]: [DeepLearning.AI: Deep Learning Specialization](https://learn.deeplearning.ai/specializations/deep-learning/information) — Andrew Ng's comprehensive DL course
[^16]: [Dive into Deep Learning (d2l.ai)](https://d2l.ai/) — Interactive textbook with PyTorch, TensorFlow, JAX
[^17]: [MIT 6.S191: Introduction to Deep Learning](https://introtodeeplearning.com/) — Free university course with labs
[^18]: [Scaler: Deep Learning Roadmap 2026](https://www.scaler.com/blog/deep-learning-roadmap/) — Month-by-month DL learning plan
[^19]: [Stanford CS224N: NLP with Deep Learning](https://web.stanford.edu/class/cs224n/) — Premier NLP course
[^20]: [PyTorch NLP Tutorials](https://docs.pytorch.org/tutorials/beginner/nlp/index.html) — Official PyTorch NLP getting started
[^21]: [Codecademy: Engineer Neural Networks with PyTorch and Transformers](https://www.codecademy.com/learn/paths/engineer-neural-networks-with-py-torch-and-transformers) — Hands-on BERT/GPT/CLIP labs
[^22]: [Machine Learning Mastery: Deploying ML Models with FastAPI & Docker](https://machinelearningmastery.com/step-by-step-guide-to-deploying-machine-learning-models-with-fastapi-and-docker/) — Step-by-step deployment guide
[^23]: [MLJourney: Best Practices for FastAPI & Docker ML Deployment](https://mljourney.com/best-practices-for-deploying-ml-models-with-docker-fastapi-in-production/) — Production best practices
[^24]: [GitHub: MLOps FastAPI Microservice Template](https://github.com/ivesfurtado/mlops-fastapi-microservice) — Complete template with CI/CD
[^25]: [Kaggle: Getting Started on Kaggle](https://www.kaggle.com/docs/competitions) — Official beginner competition guide
[^26]: [GitHub: Machine Learning Roadmap 2025 (FREE)](https://github.com/mlacademyai/Machine-Learning-Roadmap) — Community-maintained ML roadmap
[^27]: [freeCodeCamp: Learn Python for Data Science](https://www.freecodecamp.org/news/learn-python-for-data-science-full-course/) — 17-hour free video course
