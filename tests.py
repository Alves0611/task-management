import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
tasks = []


def test_create_task():
    new_task_data = {"title": "new task", "description": "task description"}
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json 
    assert "id" in response_json 
    tasks.append(response_json["id"])
