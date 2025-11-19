**Delivery Order Management System** :-

A clean and testable backend application built using Python, Flask, SQLAlchemy, and SQLite.  This project manages customer orders with functionality to create, view, update, and delete orders.

**The project follows a clean MVC structure:**

"Controllers handle the API routes"

"Services contain business logic"

"Models define the database structure"

"App.py initializes Flask and the database"

I initially built the system with in-memory storage, then upgraded it to a full database-backed system using SQLite so that data persists even after restart.

The project includes REST APIs for Create, Read, Update, and Delete (CRUD).

I also built automated tests for services and controllers, ensuring reliability and maintainability.

Tools used: Flask, SQLAlchemy, SQLite, Thunder Client for API testing, and PyTest for automation.

**Features :**

✔ **Create a new order**

-> Customer Name

-> Item

-> Quantity

✔ **Get all orders**

Returns a list of all orders stored in the database.

✔ **Get a specific order**

View the details of a single order using its order ID.

✔**Update order data**

Update an existing order's details (e.g. Data).

✔ **Delete an order**

Remove an order permanently.

✔ **Persistent Storage**

All data is stored permanently in orders.db using SQLite.

✔ **Clean Project Architecture**

**Controller Layer** → handles HTTP requests

**Service Layer** → business logic

**Model Layer** → database structure

**App Layer** → application initialization

**Project Structure**

delivery_app/
│ app.py
│ orders.db
│
├── controllers/
│     └── order_controller.py
│
├── models/
│     └── order_model.py
│
├── services/
│     └── order_service.py
│
└── tests/
      └── test_order_controller.py
