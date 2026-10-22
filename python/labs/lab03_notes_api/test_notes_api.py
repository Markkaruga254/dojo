import app as notes_app
from fastapi.testclient import TestClient


def client():
    notes_app._DB.clear()
    notes_app._NEXT_ID = 1
    return TestClient(notes_app.app)


def test_create_and_get():
    c = client()
    r = c.post("/notes", json={"title": "hello", "body": "world"})
    assert r.status_code == 201
    note = r.json()
    assert note == {"id": 1, "title": "hello", "body": "world"}
    assert c.get("/notes/1").json() == note


def test_list_ordered():
    c = client()
    c.post("/notes", json={"title": "a"})
    c.post("/notes", json={"title": "b"})
    assert [n["title"] for n in c.get("/notes").json()] == ["a", "b"]


def test_404s():
    c = client()
    assert c.get("/notes/99").status_code == 404
    assert c.delete("/notes/99").status_code == 404


def test_delete():
    c = client()
    c.post("/notes", json={"title": "a"})
    r = c.delete("/notes/1")
    assert r.status_code == 204 and r.content == b""
    assert c.get("/notes/1").status_code == 404


def test_validation():
    c = client()
    assert c.post("/notes", json={"title": ""}).status_code == 422
    assert c.post("/notes", json={"title": "x" * 101}).status_code == 422
    assert c.post("/notes", json={}).status_code == 422
