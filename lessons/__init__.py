from __future__ import annotations

import importlib
import pkgutil
import re
from fastapi import APIRouter


_LESSON_NUMBER_RE = re.compile(r"(\d+)")


def _lesson_sort_key(name: str) -> tuple[int, str]:
    """
    Sort lessons like lesson_1, lesson_2, lesson_10 correctly.

    Returns:
      (number, name) if a number exists, else (very_large_number, name)
    """
    match = _LESSON_NUMBER_RE.search(name)
    if match:
        return (int(match.group(1)), name)
    return (10**9, name)


def build_lessons_router() -> APIRouter:
    root = APIRouter()

    package_name = __name__  # "lessons"
    package = importlib.import_module(package_name)

    discovered: list[str] = []

    for module_info in pkgutil.iter_modules(package.__path__):
        if module_info.ispkg and module_info.name.startswith("lesson_"):
            discovered.append(module_info.name)

    for lesson_name in sorted(discovered, key=_lesson_sort_key):
        lesson_pkg = f"{package_name}.{lesson_name}"
        router_module_name = f"{lesson_pkg}.router"

        try:
            mod = importlib.import_module(router_module_name)
        except ModuleNotFoundError:
            continue

        lesson_router = getattr(mod, "router", None)
        if lesson_router is not None:
            root.include_router(lesson_router)

    return root