# Troubleshooting

Common issues and their solutions. If your issue isn't listed here, [open a question](https://github.com/djordjeperovic/python-ds-ml-roadmap/issues/new?template=question.yml).

---

## 🐍 Python & Environment

### "Python not found" or wrong version

```bash
# Check your Python version (need 3.10+)
python --version

# On some systems, use python3
python3 --version
```

**Fix:** Install Python 3.10+ from [python.org](https://www.python.org/downloads/) or use [pyenv](https://github.com/pyenv/pyenv).

### Virtual environment won't activate

**Windows:**
```powershell
# If you get "running scripts is disabled"
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### `pip install` fails with dependency conflicts

```bash
# Upgrade pip first
pip install --upgrade pip

# Install with verbose output to see what's failing
pip install -r requirements.txt -v

# If a specific package fails, try installing it alone
pip install numpy
```

---

## 🔥 PyTorch Installation

### PyTorch is too large / takes forever to download

The default PyTorch includes CUDA support (~2 GB). For this roadmap, CPU-only is sufficient:

```bash
# CPU-only PyTorch (much smaller, ~200 MB)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### "No module named 'torch'" after installing

Make sure you're in the correct virtual environment:

```bash
# Check which Python is active
which python    # macOS/Linux
where python    # Windows

# Should point to .venv, not system Python
```

### CUDA/GPU errors

This roadmap works entirely on CPU. If you see CUDA errors:

```python
# Force CPU in your code
device = torch.device('cpu')
model = model.to(device)
```

---

## 📓 Jupyter Notebooks

### "No kernel found" or kernel not matching

```bash
# Install the kernel for your venv
pip install ipykernel
python -m ipykernel install --user --name=ds-ml-roadmap --display-name "DS & ML Roadmap"
```

Then select "DS & ML Roadmap" kernel in Jupyter.

### Notebook won't render on GitHub

GitHub has a file size limit for notebook rendering. If outputs are large:

```bash
# Strip outputs (already configured via .gitattributes)
nbstripout notebook.ipynb

# Or clear outputs in Jupyter: Kernel → Restart & Clear Output
```

### Plots not showing in Jupyter

```python
# Add this at the top of your notebook
%matplotlib inline
```

If using VS Code:
- Install the "Jupyter" extension
- Select the correct Python interpreter (bottom-left corner)

---

## 🐳 Docker (MLOps Project)

### "Docker daemon is not running"

- **Windows/Mac:** Start Docker Desktop
- **Linux:** `sudo systemctl start docker`

### Port 8000 already in use

```bash
# Find what's using port 8000
# Windows
netstat -ano | findstr :8000
# macOS/Linux
lsof -i :8000

# Use a different port
docker run -p 8001:8000 mlops-app
```

### Docker build fails

```bash
# Clean Docker cache and rebuild
docker system prune -f
docker build --no-cache -t mlops-app .
```

---

## 📦 Package-Specific Issues

### XGBoost / LightGBM won't install

**macOS (Apple Silicon):**
```bash
# Install via conda if pip fails
conda install -c conda-forge xgboost lightgbm
```

**Windows:**
```bash
# Make sure you have Visual C++ Build Tools
pip install xgboost lightgbm
```

### imbalanced-learn version conflict

```bash
# imbalanced-learn requires specific scikit-learn versions
pip install imbalanced-learn --upgrade
pip install scikit-learn --upgrade
```

### NLTK data download issues

The NLP notebook in this repo uses pure Python tokenization and doesn't require NLTK data downloads. If you want to use NLTK elsewhere:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

---

## ☁️ Google Colab

### "Module not found" in Colab

Colab has most packages pre-installed, but some may need manual installation:

```python
!pip install xgboost lightgbm imbalanced-learn
```

### Notebook won't open in Colab

1. Make sure the notebook is on the `main` branch
2. Use the Colab badge links in the README
3. Or manually: `https://colab.research.google.com/github/djordjeperovic/python-ds-ml-roadmap/blob/main/path/to/notebook.ipynb`

---

## 🧪 Tests

### Tests fail with "no module named 'app'"

Run tests from the project root:

```bash
# From the repo root directory
pytest projects/06_mlops_deployment/tests/
```

### pytest not found

```bash
pip install pytest pytest-anyio
```

---

## 📚 MkDocs Site

### `mkdocs serve` fails

```bash
pip install mkdocs-material
mkdocs serve
```

### "Config value 'theme' error"

Make sure you have mkdocs-material installed (not just mkdocs):

```bash
pip install mkdocs-material
```

---

## Still stuck?

1. Search [existing issues](https://github.com/djordjeperovic/python-ds-ml-roadmap/issues)
2. Open a [question](https://github.com/djordjeperovic/python-ds-ml-roadmap/issues/new?template=question.yml) with:
   - Your OS and Python version
   - The exact error message
   - What you've already tried
