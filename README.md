# Python CI Validation Sample

A minimal Python project for demonstrating GitHub Actions CI validation.

## Project structure

```text
.
├── .github/
│   └── workflows/
│       └── ci-validation.yml
├── src/
│   ├── __init__.py
│   └── calculator.py
├── tests/
│   ├── __init__.py
│   └── test_calculator.py
└── requirements.txt
```

## Run tests locally

Requires Python 3.10+.

```bash
python -m venv .venv
```

Activate the environment:
- macOS/Linux: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`

Install dependencies and run tests:

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## Use with GitHub Actions

1. Create an empty repository on GitHub.
2. Extract this project and open its folder in Visual Studio Code.
3. Initialize Git if needed, commit the files, and push to the `main` branch.
4. Open the repository's **Actions** tab.
5. Confirm **Python CI Validation** completes successfully.

The workflow runs on pushes to `main` and pull requests targeting `main`.
