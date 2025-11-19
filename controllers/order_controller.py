from flask import Blueprint, request, jsonify
from services.order_service import OrderService

order_controller = Blueprint("order_controller", __name__)
order_service = OrderService()

# ------------------------
# CREATE ORDER
# ------------------------
@order_controller.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    order = order_service.add_order(
        data["customer_name"],
        data["item"],
        data["quantity"]
    )
    return jsonify(order.to_dict()), 201

# ------------------------
# GET ALL ORDERS
# ------------------------
@order_controller.route("/orders", methods=["GET"])
def get_orders():
    orders = order_service.get_all_orders()
    return jsonify([order.to_dict() for order in orders]), 200

# ------------------------
# GET ORDER BY ID
# ------------------------
@order_controller.route("/orders/<int:order_id>", methods=["GET"])
def get_order(order_id):
    order = order_service.get_order_by_id(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order.to_dict()), 200

# ------------------------
# UPDATE ORDER (PUT)
# ------------------------
@order_controller.route("/orders/<int:order_id>", methods=["PUT"])
def update_order(order_id):
    data = request.get_json()
    order = order_service.get_order_by_id(order_id)

    if not order:
        return jsonify({"error": "Order not found"}), 404

    order.customer_name = data.get("customer_name", order.customer_name)
    order.item = data.get("item", order.item)
    order.quantity = data.get("quantity", order.quantity)

    order_service.save(order)

    return jsonify(order.to_dict()), 200

# ------------------------
# DELETE ORDER
# ------------------------
@order_controller.route("/orders/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    order = order_service.get_order_by_id(order_id)

    if not order:
        return jsonify({"error": "Order not found"}), 404

    order_service.delete(order)
    return jsonify({"message": "Order deleted successfully"}), 200
