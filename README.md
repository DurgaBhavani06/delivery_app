**Delivery Order Management System** :-

Delivery Order Management System is a backend application built using Python, Flask, SQLAlchemy, and SQLite to manage customer orders efficiently.
The system provides REST APIs to create, view, update, and delete delivery orders with persistent database storage.

This project was originally built using in-memory storage, but later upgraded to a full database architecture using SQLite + SQLAlchemy, ensuring that all order data is stored permanently and does not disappear after restarting the server.

**The project follows a clean MVC structure:**

"Controllers handle the API routes"

"Services contain business logic"

"Models define the database structure"

"App.py initializes Flask and the database"

I initially built the system with in-memory storage, then upgraded it to a full database-backed system using SQLite so that data persists even after restart.

The project includes REST APIs for Create, Read, Update, and Delete (CRUD).

I also built automated tests for services and controllers, ensuring reliability and maintainability.

**The application follows a clean Controller → Service → Model architecture:**

**Controllers** handle HTTP requests and route definitions.

**Services** contain business logic such as creating orders, retrieving orders, updating statuses, and deleting entries.

**Models** define the database schema using SQLAlchemy ORM.

**app.py** initializes the application, sets up the database, registers blueprints, and auto-creates database tables.

Tools used: Flask, SQLAlchemy, SQLite, Thunder Client for API testing, and PyTest for automation.

**Features :**

✔ **Create a new order**

**->** Customer Name

**->** Item

**->** Quantity

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

├── controllers/

          └── order_controller.py

├── models/

          └── order_model.py

├── services/

          └── order_service.py

└── tests/

           └── test_order_controller.py

**Installation**

1️⃣ **Create a virtual environment**

**1.** python -m venv .venv

**2.** .venv\Scripts\activate

2️⃣ **Install all dependencies**

pip install -r requirements.txt

▶️ **Running the Application**

python app.py

**Server runs at:**

http://127.0.0.1:5000

**🧪 API Endpoints**

**➤ Create Order**

POST /orders

**Body:**

{

  "customer_name": "Alice",
  
  "item": "Phone",
  
  "quantity": 2

}

**➤ Get All Orders**

GET /orders

**➤ Get Order by ID**

GET /orders/<order_id>

**➤ Update Order data**

PUT /orders/<order_id>

**Body:**

{

  "customer_name": "vibha",
  
  "item": "iPhone",
  
  "quantity": 1

}

**➤ Delete Order**

DELETE /orders/<order_id>

**🧪 Running Tests**

pytest -q

**Expected result :**

6 passed in 0.46s

All controller and service functionalities are test-verified.

**🎯 Learning Highlights**

**->** REST API design

**->** Controller-Service-Model architecture

**->** Clean, maintainable code

**->** Unit and integration testing

**->** SQLite + SQLAlchemy ORM

**->** Error handling and validations

**->** Thunder Client API testing

**->** Python virtual environment management

**⭐ Future Enhancements**

**->** Add pagination

**->** Add frontend UI (HTML/React)

**->** Add authentication

**->** Add filtering (by status)

**->** Deploy on Render/Heroku

**->** Containerize with Docker

**🎉 Conclusion :**

This project demonstrates strong backend engineering concepts, clean design patterns, REST API development, and database integration.
