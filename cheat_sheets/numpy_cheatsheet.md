# NumPy Cheat Sheet

> **Quick Reference** — `import numpy as np`

---

## 📦 Array Creation

| Function | Description | Example |
|---|---|---|
| `np.array()` | Create from list | `np.array([1, 2, 3])` |
| `np.zeros()` | All zeros | `np.zeros((3, 4))` |
| `np.ones()` | All ones | `np.ones((2, 3))` |
| `np.full()` | Fill with value | `np.full((2, 2), 7)` |
| `np.eye()` | Identity matrix | `np.eye(3)` |
| `np.arange()` | Range with step | `np.arange(0, 10, 2)` → `[0, 2, 4, 6, 8]` |
| `np.linspace()` | Evenly spaced | `np.linspace(0, 1, 5)` → `[0, 0.25, 0.5, 0.75, 1]` |
| `np.random.randn()` | Normal distribution | `np.random.randn(3, 3)` |
| `np.random.rand()` | Uniform [0, 1) | `np.random.rand(2, 4)` |
| `np.random.randint()` | Random integers | `np.random.randint(0, 10, (3, 3))` |
| `np.empty()` | Uninitialized | `np.empty((2, 3))` |

---

## 🔍 Array Attributes

| Attribute | Description | Example Output |
|---|---|---|
| `a.shape` | Dimensions | `(3, 4)` |
| `a.ndim` | Number of axes | `2` |
| `a.dtype` | Data type | `float64` |
| `a.size` | Total elements | `12` |
| `a.itemsize` | Bytes per element | `8` |
| `a.nbytes` | Total bytes | `96` |

---

## 🎯 Indexing & Slicing

### 1D Indexing

```python
a = np.array([10, 20, 30, 40, 50])
a[0]      # 10
a[-1]     # 50
a[1:4]    # [20, 30, 40]
a[::2]    # [10, 30, 50]
```

### 2D Indexing

```python
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a[0, 1]     # 2
a[1, :]     # [4, 5, 6]        — full row
a[:, 2]     # [3, 6, 9]        — full column
a[0:2, 1:]  # [[2, 3], [5, 6]] — subarray
```

### Boolean Indexing

```python
a = np.array([1, 2, 3, 4, 5])
a[a > 3]           # [4, 5]
a[(a > 1) & (a < 5)]  # [2, 3, 4]
```

### Fancy Indexing

```python
a = np.array([10, 20, 30, 40, 50])
a[[0, 2, 4]]  # [10, 30, 50] — index with array
```

---

## 🔄 Reshaping

| Function | Description | Example |
|---|---|---|
| `a.reshape(r, c)` | New shape (view) | `np.arange(6).reshape(2, 3)` |
| `a.ravel()` | Flatten to 1D (view) | `a.ravel()` |
| `a.flatten()` | Flatten to 1D (copy) | `a.flatten()` |
| `a.T` / `a.transpose()` | Transpose | `a.T` |
| `np.squeeze(a)` | Remove size-1 dims | `np.squeeze(a)` — `(1,3,1)` → `(3,)` |
| `np.expand_dims(a, axis)` | Add dimension | `np.expand_dims(a, 0)` — `(3,)` → `(1,3)` |
| `a.reshape(-1)` | Auto-compute dim | `a.reshape(3, -1)` |

---

## ➕ Math Operations

### Element-wise

```python
a + b    # addition
a - b    # subtraction
a * b    # multiplication (element-wise)
a / b    # division
a ** 2   # power
np.sqrt(a)
np.exp(a)
np.log(a)
np.sin(a)
```

### Aggregations

| Function | Description | Example |
|---|---|---|
| `a.sum()` | Sum of all elements | `a.sum()` or `a.sum(axis=0)` |
| `a.mean()` | Mean | `a.mean(axis=1)` |
| `a.std()` | Standard deviation | `a.std()` |
| `a.min()` / `a.max()` | Min / Max | `a.min(axis=0)` |
| `a.argmin()` / `a.argmax()` | Index of min / max | `a.argmax()` |
| `a.cumsum()` | Cumulative sum | `a.cumsum(axis=0)` |
| `np.median(a)` | Median | `np.median(a)` |
| `a.prod()` | Product of elements | `a.prod()` |

---

## 📐 Broadcasting Rules

Broadcasting allows NumPy to operate on arrays of different shapes.

**Rules (checked right-to-left):**
1. If dimensions differ in count, the smaller array is padded with 1s on the left.
2. Arrays with size 1 in a dimension act as if they had the size of the largest array in that dimension.
3. If sizes disagree and neither is 1 → error.

```python
a = np.array([[1], [2], [3]])   # shape (3, 1)
b = np.array([10, 20, 30])      # shape (3,) → broadcast to (1, 3)
a + b
# [[11, 21, 31],
#  [12, 22, 32],
#  [13, 23, 33]]                # result shape (3, 3)
```

---

## 🔢 Linear Algebra

| Function | Description | Example |
|---|---|---|
| `np.dot(a, b)` | Dot product | `np.dot(a, b)` |
| `a @ b` / `np.matmul(a, b)` | Matrix multiply | `a @ b` |
| `np.linalg.inv(a)` | Matrix inverse | `np.linalg.inv(a)` |
| `np.linalg.det(a)` | Determinant | `np.linalg.det(a)` |
| `np.linalg.eig(a)` | Eigenvalues & vectors | `vals, vecs = np.linalg.eig(a)` |
| `np.linalg.svd(a)` | SVD decomposition | `U, S, Vt = np.linalg.svd(a)` |
| `np.linalg.norm(a)` | Vector/matrix norm | `np.linalg.norm(a)` |
| `np.linalg.solve(A, b)` | Solve Ax = b | `np.linalg.solve(A, b)` |
| `np.linalg.matrix_rank(a)` | Matrix rank | `np.linalg.matrix_rank(a)` |

---

## 🛠 Useful Functions

| Function | Description | Example |
|---|---|---|
| `np.where(cond, x, y)` | Conditional select | `np.where(a > 0, a, 0)` |
| `np.concatenate()` | Join along axis | `np.concatenate([a, b], axis=0)` |
| `np.vstack()` / `np.hstack()` | Vertical / horizontal stack | `np.vstack([a, b])` |
| `np.stack()` | Stack along new axis | `np.stack([a, b], axis=0)` |
| `np.split()` | Split array | `np.split(a, 3)` |
| `np.unique()` | Unique values | `np.unique(a)` |
| `np.sort()` | Sort (copy) | `np.sort(a)` |
| `np.argsort()` | Indices that sort | `np.argsort(a)` |
| `np.clip()` | Clamp values | `np.clip(a, 0, 1)` |
| `np.searchsorted()` | Binary search | `np.searchsorted(sorted_a, v)` |
| `np.isin()` | Element membership | `np.isin(a, [1, 3, 5])` |
| `np.copy()` | Deep copy | `b = np.copy(a)` |

---

## 💡 Quick Tips

1. **Views vs copies:** Slicing returns a *view* (shared memory). Use `.copy()` if you need an independent array.
2. **Use `-1` in reshape:** Let NumPy infer one dimension — `a.reshape(-1, 3)`.
3. **Vectorize, don't loop:** Replace Python `for` loops with vectorized NumPy operations for 10–100× speedup.
4. **Set random seed:** Use `np.random.seed(42)` or `rng = np.random.default_rng(42)` for reproducibility.
5. **Check dtypes early:** Mismatched dtypes (`int` vs `float`) can cause subtle bugs. Cast with `a.astype(np.float32)`.
