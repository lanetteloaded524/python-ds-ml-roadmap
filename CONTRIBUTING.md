# Contributing to python-ds-ml-roadmap

Welcome! 👋 We're glad you're interested in contributing to this project. Whether you're fixing a typo, adding an exercise, or proposing an entirely new notebook — every contribution helps learners on their Data Science & ML journey.

## Ways to Contribute

- **Fix typos or grammar** in notebooks and markdown files
- **Add exercises** to existing notebooks
- **Improve explanations** — make concepts clearer or add visualizations
- **Create new notebooks** covering additional topics
- **Translate** content into other languages
- **Report bugs** or issues with notebook execution

## How to Contribute

1. **Fork** the repository on GitHub.

2. **Create a feature branch** from `main`:
   ```bash
   git checkout -b feature/your-feature
   ```

3. **Make your changes.** Follow the style guidelines below.

4. **Test that notebooks run** end-to-end:
   ```bash
   jupyter nbconvert --execute --to notebook your_notebook.ipynb
   ```

5. **Commit** with a clear, descriptive message:
   ```bash
   git commit -m "Add clustering exercises to ML fundamentals notebook"
   ```

6. **Push** your branch and **open a Pull Request** against `main`.

## Code Style Guidelines

- Follow **PEP 8** for all Python code.
- Use **clear, concise markdown** in notebook cells — explain *why*, not just *what*.
- Add **docstrings** to functions and classes.
- Use **type hints** where practical.
- Keep notebooks focused — one major topic per notebook.
- Prefer **synthetic data** so notebooks run without external downloads.

## Reporting Issues

Found a bug or have a suggestion? [Open an issue](../../issues) with:
- A clear title and description
- Steps to reproduce (if applicable)
- Your Python version and OS

## Code of Conduct

Please be respectful and constructive in all interactions. We are committed to providing a welcoming and inclusive experience for everyone. Harassment or disrespectful behavior will not be tolerated.

---

Thank you for helping make this roadmap better for everyone! 🚀
