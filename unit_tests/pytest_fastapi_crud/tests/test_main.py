import pytest
from colorama import Fore
from fastapi.testclient import TestClient
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) #Guarda la ruta del proyecto
sys.path.insert(0, project_root) #Establece la ruta del proyecto

from app.main import app
from app.main import app, users_db, User

client = TestClient(app) #Instancia el TestClient de FastAPI

#Endpoint para leer a todos los usuarios
def test_read_users():
    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(users_db)
    print(f"\n{Fore.CYAN}[+] {data}")

#Endpoint para leer a un usuario
def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "user1"
    print(f"\n{Fore.CYAN}[+] {data}")

#Endpoint para crear usuarios
def test_create_user():
    # Limpiar base de datos para evitar conflictos de ID
    users_db.clear()

    # No incluir el campo ID en la solicitud de creación, será asignado por la aplicación
    new_user = {"username": "newuser", "email": "newuser@example.com", "full_name": "New User"}
    response = client.post("/users/", json=new_user)
    
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["username"] == new_user["username"]
    assert data["email"] == new_user["email"]
    assert data["full_name"] == new_user["full_name"]

    # Verificar que el usuario se ha añadido a la base de datos
    response = client.get(f"/users/{data['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "newuser"
    print(f"\n{Fore.CYAN}[+] {data}")

#Endpoint para actualizar a un usuario
def test_update_user():
    # Preparar el entorno de prueba
    users_db.clear()
    test_user = User(id=1, username="testuser", email="test@example.com", full_name="Test User")
    users_db.append(test_user)

    updated_user = {"username": "updateduser", "email": "updateduser@example.com", "full_name": "Updated User"}
    response = client.put("/users/1", json=updated_user)
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["username"] == updated_user["username"]
    assert data["email"] == updated_user["email"]
    assert data["full_name"] == updated_user["full_name"]
    print(f"\n{Fore.CYAN}[+] {data}")

#Endpoint para eliminar a un usuario
def test_delete_user():
    # Preparar el entorno de prueba
    users_db.clear()
    test_user = User(id=1, username="user1", email="user1@example.com", full_name="User One")
    users_db.append(test_user)

    response = client.delete("/users/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "user1"

    # Verificar que el usuario ha sido eliminado de la base de datos
    response = client.get("/users/1")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"
    print(f"\n{Fore.CYAN}[+] {data}")

#Endpoint para comprobar que un usuario no existe
def test_read_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "User not found"
    print(f"\n{Fore.CYAN}[+] {data}")
