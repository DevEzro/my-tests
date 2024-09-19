import pytest
from fastapi.testclient import TestClient
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) 
sys.path.insert(0, project_root)

from app.main import app

client = TestClient(app)

def test_get_prueba():
    response = client.get("/Get-Prueba")
    data = response.json()
    print(data)

def test_put_prueba():
    response = client.put("/Put-Prueba")
    data = response.json()
    print(data)

def test_post_prueba():
    response = client.post("/Post-Prueba")
    data = response.json()
    print(data)
    
def test_delte_prueba():
    response = client.delete("/Delete-Prueba")
    data = response.json()
    print(data)