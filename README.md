**Delivery Order Management System** :-

I built a Delivery Order Management System using Flask, SQLAlchemy, and SQLite.

The application supports creating orders, listing orders, updating order status, deleting orders, and retrieving order details.

The project follows a clean MVC structure:

Controllers handle the API routes

Services contain business logic

Models define the database structure

App.py initializes Flask and the database

I initially built the system with in-memory storage, then upgraded it to a full database-backed system using SQLite so that data persists even after restart.

The project includes REST APIs for Create, Read, Update, and Delete (CRUD).

I also built automated tests for services and controllers, ensuring reliability and maintainability.

Tools used: Flask, SQLAlchemy, SQLite, Thunder Client for API testing, and PyTest for automation.
