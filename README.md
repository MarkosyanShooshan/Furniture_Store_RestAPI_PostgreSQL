# Furniture Store - Django REST API & Web Application

A full-featured Django web application and RESTful API for a modern Furniture Store catalog. The project supports dynamic catalog navigation, detailed product views, full administrative management, and PostgreSQL database integration.

---

## 🚀 Features

- **Product & Category Management:** Organized catalog structure with slugified URLs.
- **REST API Endpoints:** Complete API serialized via Django REST Framework (DRF) for integration with frontend applications.
- **PostgreSQL Backend:** Production-ready relational database setup replacing local development databases.
- **Interactive UI:** Responsive product catalog with category filtering and interactive product inquiry actions.
- **Environment Security:** Sensitive configurations (secret keys, credentials, host settings) managed securely via `.env` environment variables.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Django, Django REST Framework
- **Database:** PostgreSQL
- **Environment Configuration:** `python-dotenv`
- **Frontend:** HTML5, CSS3, JavaScript (Django Templates)

---

## ⚙️ Local Setup Instructions

Follow these steps to run the project locally on your machine:

### 1. Clone the Repository

git clone https://https://github.com/MarkosyanShooshan/Furniture_Store_RESTAPI_PostgreSQL.git

cd Furniture_Store_RESTAPI_PostgreSQL



2. Create and Activate Virtual EnvironmentBash# On Windows
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Environment Variables Setup
Create a .env file in the root directory based on the .env.example template:
DJANGO_SECRET_KEY=your-secret-key-here
DJANGO_DEBUG=True
DB_NAME=furniture_db
DB_USER=postgres
DB_PASSWORD=your_postgres_password
DB_HOST=127.0.0.1
DB_PORT=5432

5. Run Database Migrations
Make sure your local PostgreSQL service is running and furniture_db exists, then execute:
python manage.py migrate

6. Create Superuser (Admin Access)
python manage.py createsuperuser

7. Run the Development Server
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.

📡 API Endpoints
Resource,        Endpoint,          Method,          Description
Products,       /api/products/,      GET,      List all furniture products
Product Detail, /api/products/{id}/, GET,      Retrieve specific product details
Categories,     /api/categories/,    GET,      List all furniture categories
Admin Panel,    /admin/,             GET,      Manage catalog data via Django Admin
