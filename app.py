from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orders.db"

    db.init_app(app)

    from controllers.order_controller import order_controller
    app.register_blueprint(order_controller)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
