# from fastapi import FastAPI
# from app.lessons import build_lessons_router

# app = FastAPI(
#     title="FastAPI Lessons",
#     description="One server, many lessons. Each lesson is a router.",
#     version="0.1.0",
# )

# app.include_router(build_lessons_router())

# @app.get("/", tags=["Index"])
# def index():
#     return {
#         "message": "FastAPI lessons hub",
#         "docs": "/docs",
#         "redoc": "/redoc",
#         "health": "/health",
#     }

# @app.get("/health", tags=["Index"])
# def health():
#     return {"ok": True}

from fastapi import FastAPI

from lessons import build_lessons_router

app = FastAPI(
    title="FastAPI Lessons",
    version="1.0.0",
    description="One server, many lessons. Each lesson is an APIRouter.",
)

app.include_router(build_lessons_router())

@app.get("/", tags=["Index"], summary="Lessons hub")
def index():
    return {
        "message": "FastAPI lessons hub",
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/health",
    }

@app.get("/health", tags=["Index"], summary="Health check")
def health():
    return {"ok": True}