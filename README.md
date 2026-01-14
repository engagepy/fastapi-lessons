# FastAPI Tinker and Learn

A structured FastAPI playground designed to learn by doing, without spinning up multiple servers or rewriting boilerplate for every experiment.

Each lesson is implemented as an isolated router and automatically discovered by the main application. One server, many lessons, clean documentation.

---

## What this project covers

This project incrementally explores FastAPI concepts, including:

1. Parameter selection using Enums
2. Path and query parameters
3. Conditional logic based on query parameters
4. Request bodies using Pydantic models
5. Validation using Query and type hints
6. Combining path, query, and body parameters

Each concept lives in its own lesson module and appears neatly in the interactive API documentation.

---

## Project structure

    .
    ├── main.py
    ├── lessons/
    │   ├── __init__.py
    │   ├── lesson_1/
    │   │   ├── __init__.py
    │   │   └── router.py
    │   ├── lesson_2/
    │   │   ├── __init__.py
    │   │   └── router.py
    │   ├── lesson_3/
    │   │   ├── __init__.py
    │   │   └── router.py
    │   └── ...
    ├── requirements.txt
    └── README.md

- main.py defines the single FastAPI application
- Each lesson exposes an APIRouter
- Lessons are auto discovered and mounted at startup
- No per lesson servers
- No manual wiring when adding new lessons

---

## Getting started

### Create and activate a virtual environment (recommended)

    python -m venv venv

Activate it:

macOS or Linux:

    source venv/bin/activate

Windows:

    venv\Scripts\activate

---

### Install dependencies

    pip install -r requirements.txt

---

### Run the application

From the project root:

    uvicorn main:app --reload --app-dir .

One command. Always.

---

## Accessing the application

API root:

    http://localhost:8000

Swagger UI:

    http://localhost:8000/docs

ReDoc:

    http://localhost:8000/redoc

Each lesson is available under its own URL prefix, for example:

- /lesson-1/...
- /lesson-2/...
- /lesson-3/...

---

## Adding a new lesson

1. Create a new folder under lessons, for example lesson_7
2. Add __init__.py
3. Add router.py and define:

    router = APIRouter(prefix="/lesson-7", tags=["Lesson 7"])

4. Add endpoints to the router

No changes are required in main.py. The lesson will be picked up automatically.

---

## Design philosophy

- One FastAPI application
- Modular routers
- Convention over configuration
- Deterministic auto loading
- Clean, readable API documentation

This structure scales from learning experiments to real world APIs without rewrites.

---

## Notes

- Always run Uvicorn from the project root
- Do not use uvicorn lessons.lesson_x.main:app
- Lessons are routers, not standalone applications

---

FastAPI is easiest to learn when structure is boring and behaviour is predictable.  
This project keeps it that way.