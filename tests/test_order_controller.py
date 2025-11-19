import json
from app import app    # ✅ FIX: Import the Flask app
from controllers.order_controller import order_controller
def test_create_order():
    client = app.test_client()
    response = client.post("/orders", json={
        "customer_name": "Alice",
        "item": "Phone",
        "quantity": 2
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["customer_name"] == "Alice"

def test_get_orders():
    client = app.test_client()
    client.post("/orders", json={
        "customer_name": "Alice",
        "item": "Phone",
        "quantity": 2
    })
    response = client.get("/orders")
    assert response.status_code == 200

def test_update_status():
    client = app.test_client()
    client.post("/orders", json={
        "customer_name": "Bob",
        "item": "Mouse",
        "quantity": 1
    })
    response = client.put("/orders/1/status", json={"status": "SHIPPED"})
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "SHIPPED"
