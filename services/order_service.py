from extensions import db
from models.order_model import Order

class OrderService:

    def add_order(self, customer_name, item, quantity):
        order = Order(
            customer_name=customer_name,
            item=item,
            quantity=quantity
        )
        db.session.add(order)
        db.session.commit()
        return order

    def get_all_orders(self):
        return Order.query.all()

    def get_order_by_id(self, order_id):
        return Order.query.get(order_id)

    def save(self, order):
        db.session.commit()

    def delete(self, order):
        db.session.delete(order)
        db.session.commit()
