import requests

def test_frontend_backend_integration():
    frontend_url = "http://<minikube-ip>:30000"
    response = requests.get(frontend_url)
    assert response.status_code == 200
    assert "Hello from backend" in response.text
