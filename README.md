# 📦 Thoughtful Package Sorter API

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green.svg)
![Tests](https://img.shields.io/badge/tests-pytest%20passing-brightgreen)

A Python-based API to classify packages as `STANDARD`, `SPECIAL`, or `REJECTED` based on their dimensions and mass. Built using **FastAPI** and tested with **pytest**.

---

## 💡 Problem Statement

Robotic systems must dispatch packages based on volume and mass.

### Rules:

- A package is **bulky** if:
  - Volume (width × height × length) ≥ 1,000,000 cm³
  - OR any single dimension ≥ 150 cm
- A package is **heavy** if:
  - Mass ≥ 20 kg

### Classification:

| Condition               | Stack      |
| ----------------------- | ---------- |
| Bulky **and** Heavy     | `REJECTED` |
| Bulky **or** Heavy      | `SPECIAL`  |
| Neither bulky nor heavy | `STANDARD` |

---

## 🚀 How to Run Locally (Replit or Terminal)

1. **Install dependencies**:

```bash
pip install fastapi uvicorn pydantic pytest
```

2. **Start the FastAPI server**:

```bash
uvicorn main:app --host=0.0.0.0 --port=8000
```

3. **Open your browser** at:

```
http://localhost:8000/docs
```

This will open Swagger UI where you can test the `/classify` endpoint interactively.

### Alternative: cURL Example

```bash
curl -X POST "http://localhost:8000/classify" -H "Content-Type: application/json" -d '{"width":100,"height":100,"length":100,"mass":25}'
```

Response:

```json
{ "classification": "SPECIAL" }
```

---

## 🧪 Running Tests

This project uses `pytest` for unit testing.

```bash
pytest test_package_sorter.py
```

✅ Tests cover:

- All classification scenarios
- Edge case: invalid input with negative values

---

## 🧼 Project Structure

```
.
├── main.py                  # FastAPI app entry point
├── package_sorter.py        # Core sorting logic (Package class & classification)
├── test_package_sorter.py   # Pytest unit tests
└── README.md                # This file
```

---

## 🛠️ Technologies Used

- Python 3.x
- FastAPI (API framework)
- Pydantic (data validation)
- Uvicorn (ASGI server)
- Pytest (unit testing)

---

## 🔗 Live API Demo (if using Replit)

Swagger UI:  
👉 For local use in docs → http://localhost:8000/docs

👉 For Replit/public README → https://<your-username>.<repl-name>.repl.co/docs

---

## 📄 License

MIT License – feel free to use and adapt.

---

## 🧠 Author Notes

This project:

- Demonstrates real-world API design using FastAPI
- Includes robust test coverage
- Validates inputs with custom error handling
- Is modular, clean, and Pythonic

Perfect for scaling or integration into automation systems.
