import pytest
from services.order_service import OrderService


def test_add_order():
    service = OrderService()
    order = service.add_order("John", "Laptop", 1)
    assert order.order_id == 1
    assert order.status == "PENDING"

def test_update_order_status():
    service = OrderService()
    order = service.add_order("John", "Laptop", 1)
    updated = service.update_order_status(1, "DELIVERED")
    assert updated.status == "DELIVERED"

def test_update_invalid_order():
    service = OrderService()
    assert service.update_order_status(99, "CANCELLED") is None
