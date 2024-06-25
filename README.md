A game to simulate recycle everything down to create a sustainable society.

# Building

```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

# Testing

```bash
source .env/bin/activate
pytest
```

## Individual test files
```bash
source .env/bin/activate
PYTHONPATH=. python3 tests/disassembly_tests.py
```
