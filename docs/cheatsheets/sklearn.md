# scikit-learn Cheat Sheet

> **Quick Reference** — `import sklearn`

---

## 🔁 The API Pattern

Every scikit-learn estimator follows the same interface:

```python
from sklearn.some_module import SomeEstimator

model = SomeEstimator(hyperparam=value)
model.fit(X_train, y_train)         # learn from data
y_pred = model.predict(X_test)      # predict
score = model.score(X_test, y_test) # evaluate

# Transformers (scalers, encoders, etc.)
transformer.fit(X_train)
X_new = transformer.transform(X_test)
X_new = transformer.fit_transform(X_train)  # fit + transform in one step
```

---

## ✂️ Data Splitting

```python
from sklearn.model_selection import train_test_split, KFold, StratifiedKFold

# Simple split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# K-Fold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for train_idx, val_idx in kf.split(X):
    X_train, X_val = X[train_idx], X[val_idx]

# Stratified K-Fold (preserves class balance)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
for train_idx, val_idx in skf.split(X, y):
    X_train, X_val = X[train_idx], X[val_idx]

# Cross-val score shortcut
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
```

---

## 🔧 Preprocessing

| Class | Description | Example |
|---|---|---|
| `StandardScaler` | Zero mean, unit variance | `StandardScaler().fit_transform(X)` |
| `MinMaxScaler` | Scale to [0, 1] | `MinMaxScaler().fit_transform(X)` |
| `RobustScaler` | Robust to outliers | `RobustScaler().fit_transform(X)` |
| `LabelEncoder` | Encode target labels | `LabelEncoder().fit_transform(y)` |
| `OneHotEncoder` | One-hot encode categoricals | `OneHotEncoder(sparse_output=False).fit_transform(X)` |
| `OrdinalEncoder` | Encode categoricals as ints | `OrdinalEncoder().fit_transform(X)` |
| `SimpleImputer` | Fill missing values | `SimpleImputer(strategy='mean').fit_transform(X)` |
| `PolynomialFeatures` | Polynomial & interaction | `PolynomialFeatures(degree=2).fit_transform(X)` |

```python
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)  # use train statistics!
```

---

## 🎯 Feature Selection

```python
from sklearn.feature_selection import SelectKBest, f_classif, mutual_info_classif, RFE

# Select top k features by statistical test
selector = SelectKBest(f_classif, k=10)
X_new = selector.fit_transform(X, y)

# Mutual information
selector = SelectKBest(mutual_info_classif, k=10)

# Recursive feature elimination
from sklearn.ensemble import RandomForestClassifier
rfe = RFE(estimator=RandomForestClassifier(), n_features_to_select=10)
X_new = rfe.fit_transform(X, y)
print(rfe.support_)    # boolean mask of selected features
print(rfe.ranking_)    # feature ranking
```

---

## 📈 Regression Models

| Model | Import | Key Parameters |
|---|---|---|
| `LinearRegression` | `sklearn.linear_model` | `fit_intercept` |
| `Ridge` | `sklearn.linear_model` | `alpha` (L2 penalty) |
| `Lasso` | `sklearn.linear_model` | `alpha` (L1 penalty) |
| `ElasticNet` | `sklearn.linear_model` | `alpha`, `l1_ratio` |
| `DecisionTreeRegressor` | `sklearn.tree` | `max_depth`, `min_samples_split` |
| `RandomForestRegressor` | `sklearn.ensemble` | `n_estimators`, `max_depth` |
| `GradientBoostingRegressor` | `sklearn.ensemble` | `n_estimators`, `learning_rate`, `max_depth` |
| `SVR` | `sklearn.svm` | `C`, `kernel`, `epsilon` |

```python
from sklearn.linear_model import Ridge
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

---

## 🏷 Classification Models

| Model | Import | Key Parameters |
|---|---|---|
| `LogisticRegression` | `sklearn.linear_model` | `C`, `penalty`, `max_iter` |
| `KNeighborsClassifier` | `sklearn.neighbors` | `n_neighbors`, `weights` |
| `SVC` | `sklearn.svm` | `C`, `kernel`, `gamma` |
| `DecisionTreeClassifier` | `sklearn.tree` | `max_depth`, `min_samples_split` |
| `RandomForestClassifier` | `sklearn.ensemble` | `n_estimators`, `max_depth` |
| `GradientBoostingClassifier` | `sklearn.ensemble` | `n_estimators`, `learning_rate`, `max_depth` |
| `MLPClassifier` | `sklearn.neural_network` | `hidden_layer_sizes`, `activation` |

```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)  # class probabilities
```

---

## 🔵 Clustering

| Model | Import | Key Parameters |
|---|---|---|
| `KMeans` | `sklearn.cluster` | `n_clusters`, `init`, `n_init` |
| `DBSCAN` | `sklearn.cluster` | `eps`, `min_samples` |
| `AgglomerativeClustering` | `sklearn.cluster` | `n_clusters`, `linkage` |

```python
from sklearn.cluster import KMeans
km = KMeans(n_clusters=3, random_state=42, n_init=10)
labels = km.fit_predict(X)
centers = km.cluster_centers_
inertia = km.inertia_
```

---

## 📉 Dimensionality Reduction

```python
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# PCA — linear
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print(pca.explained_variance_ratio_)

# t-SNE — nonlinear (visualization only)
tsne = TSNE(n_components=2, perplexity=30, random_state=42)
X_tsne = tsne.fit_transform(X)
```

---

## 📏 Metrics — Regression

| Function | Import | Description |
|---|---|---|
| `mean_squared_error(y, ŷ)` | `sklearn.metrics` | MSE |
| `mean_absolute_error(y, ŷ)` | `sklearn.metrics` | MAE |
| `r2_score(y, ŷ)` | `sklearn.metrics` | R² (1 = perfect) |
| `mean_absolute_percentage_error` | `sklearn.metrics` | MAPE |

```python
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

---

## 📏 Metrics — Classification

| Function | Description |
|---|---|
| `accuracy_score(y, ŷ)` | Overall accuracy |
| `precision_score(y, ŷ)` | Precision (PPV) |
| `recall_score(y, ŷ)` | Recall (sensitivity) |
| `f1_score(y, ŷ)` | Harmonic mean of P & R |
| `classification_report(y, ŷ)` | Full per-class report |
| `confusion_matrix(y, ŷ)` | Confusion matrix |
| `roc_auc_score(y, ŷ_prob)` | ROC AUC |

```python
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score

print(classification_report(y_test, y_pred))
cm = confusion_matrix(y_test, y_pred)
auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])  # binary
```

---

## 🔧 Hyperparameter Tuning

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

# Grid Search (exhaustive)
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10, None],
    'min_samples_split': [2, 5, 10]
}
grid = GridSearchCV(
    RandomForestClassifier(), param_grid,
    cv=5, scoring='f1', n_jobs=-1
)
grid.fit(X_train, y_train)
print(grid.best_params_)
print(grid.best_score_)
best_model = grid.best_estimator_

# Randomized Search (faster for large grids)
from scipy.stats import randint, uniform
param_dist = {
    'n_estimators': randint(50, 300),
    'max_depth': [3, 5, 10, None],
    'learning_rate': uniform(0.01, 0.3)
}
rs = RandomizedSearchCV(
    GradientBoostingClassifier(), param_dist,
    n_iter=50, cv=5, scoring='f1', random_state=42
)
rs.fit(X_train, y_train)
```

---

## 🔗 Pipelines

```python
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer

# Simple pipeline
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])
pipe.fit(X_train, y_train)
pipe.predict(X_test)

# make_pipeline (auto-names steps)
pipe = make_pipeline(StandardScaler(), LogisticRegression())

# ColumnTransformer — different transforms per column type
from sklearn.compose import ColumnTransformer
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), ['age', 'income']),
    ('cat', OneHotEncoder(), ['city', 'gender']),
])

full_pipe = Pipeline([
    ('prep', preprocessor),
    ('model', RandomForestClassifier())
])
full_pipe.fit(X_train, y_train)
```

---

## 💾 Model Persistence

```python
import joblib

# Save
joblib.dump(model, 'model.joblib')

# Load
model = joblib.load('model.joblib')

# Also works with full pipelines
joblib.dump(full_pipe, 'pipeline.joblib')
```

---

## 💡 Quick Tips

1. **Always scale features** before distance-based models (KNN, SVM, PCA) — use `StandardScaler` or `MinMaxScaler`.
2. **Use pipelines** to avoid data leakage — they ensure `fit` is only called on training data during cross-validation.
3. **Stratify splits:** Pass `stratify=y` to `train_test_split` for imbalanced classification to preserve class ratios.
4. **`n_jobs=-1`** on `GridSearchCV`, `RandomForest`, etc. parallelizes across all CPU cores.
5. **Check `cross_val_score` before tuning** — get a baseline with default hyperparameters first, then optimize.
