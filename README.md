A game to simulate recycle everything down to create a sustainable society.

# Building

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Testing

```bash
source .venv/bin/activate
pytest
```

## Individual test files
```bash
source .venv/bin/activate
PYTHONPATH=. python3 tests/disassembly_tests.py
```
