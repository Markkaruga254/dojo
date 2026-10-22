"""Lab 03: Notes API. Implement the TODOs, then run: pytest -q"""
from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Notes API")
_DB: dict[int, dict] = {}
_NEXT_ID = 1


class NoteIn(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    body: str = ""


# TODO POST   /notes        -> 201 {"id", "title", "body"}  (422 on invalid input is automatic)
# TODO GET    /notes/{id}   -> 200 note, or 404
# TODO GET    /notes        -> 200 list of notes ordered by id
# TODO DELETE /notes/{id}   -> 204 (no body), or 404
