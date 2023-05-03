# Minlibxx

SHORT DES

## Requirements

### Code Style

- Refactor. When you're done, refactor.
- Rename. When name can be  shorter while descriptive, shorten.
- Module name is a context. Don't repeat it.
- Avoid comments. Unless unavoidable.
- Avoid docstrings like you avoid comments.
- Do not format code. Use black to do it for you.
- Respect linters when they are right. Otherwise ignore.

### Setup

1. Install pyenv, python 3.9 & activate

```sh
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
pip install -r requirements_dev.txt
pre-commit install
```

## Development

4. Run tests w. coverage


```sh
pytest
```

5.2. Install hooks

```sh
pre-commit install
```

5.3. Run all hooks

```sh
pre-commit run --all-files
```
