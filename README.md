# **Subscription Management System**

This is a Flask-based Subscription Management System that allows users to manage their various subscriptions. The application provides user authentication, profile management, and subscription CRUD (Create, Read, Update, Delete) functionalities.

## **Table of Contents**

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## **Project Overview**

This project provides a system where users can:

- Sign up and log in to manage their subscriptions.
- Add, update, and delete subscriptions.
- View their user profile and update information such as name, email, and password.
- Filter subscriptions by name, category, date range, and billing cycle.
  
The backend is built using Flask with RESTful APIs and SQLAlchemy for the database.

## **Features**

- User authentication (Sign up, Log in, Log out, Check session).
- CRUD operations for subscriptions (Create, Read, Update, Delete).
- Secure password storage using `bcrypt`.
- Filters for subscriptions based on name, category, and payment date.
- Cross-Origin Resource Sharing (CORS) support for handling requests from various domains.

## **Technologies**

- **Backend**: Flask, Flask-RESTful, Flask-SQLAlchemy, Flask-Migrate, Flask-Bcrypt, Flask-CORS.
- **Database**: PostgreSQL.
- **Environment Variables**: Managed using `python-dotenv`.
- **Authentication**: Session-based authentication using Flask's `session`.
- **API Development**: Flask-RESTful.

## **Setup Instructions**

### **Prerequisites**

- Python 3.x
- PostgreSQL 14.x or higher
- Virtual environment tool (`venv` or `pipenv`)
- `pip` (Python package manager)

### **Clone the repository**

```bash
git clone <your-repository-url>
cd subscription-management-system
```

### **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **Install dependencies**

```bash
pip install -r requirements.txt
```

### **Configure the environment variables**

Create a `.env` file in the root of your project and add the following variables:

```
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<dbname>
SECRET_KEY=your-secret-key
```

### **Run the application**

1. Initialize the database and apply migrations:

```bash
flask db init
flask db migrate
flask db upgrade
```

2. Run the Flask development server:

```bash
python app.py
```

The application should now be running on `http://localhost:5000`.

## **Environment Variables**

- `DATABASE_URL`: The connection string to your PostgreSQL database.
- `SECRET_KEY`: The secret key for securely signing session data.

## **API Endpoints**

### **Authentication**

- **POST** `/sign_up`: Create a new user.
- **POST** `/login`: Log in as a user.
- **POST** `/logout`: Log out the user.
- **GET** `/check_session`: Check the current user's session.

### **User Profile**

- **GET** `/user/<user_id>`: Get user profile details.
- **PUT** `/user/<user_id>`: Update user profile information.

### **Subscriptions**

- **GET** `/user/<user_id>/subscriptions`: Get all subscriptions for the user.
- **POST** `/user/<user_id>/subscriptions`: Add a new subscription for the user.
- **DELETE** `/user/<user_id>/subscriptions/<subscription_id>`: Delete a specific subscription.
- **GET** `/subscriptions`: Get all subscriptions in the system (admin use).

## **Usage**

After running the application, you can interact with the API using tools like `Postman`, `cURL`, or directly integrating with a frontend client.

### **Example Request: Create a Subscription**

**POST** `/user/1/subscriptions`

```json
{
    "name": "Netflix",
    "category": "streaming",
    "cost": 12.99,
    "billing_cycle": "Monthly",
    "date_of_payment": "2024-10-15"
}
```

**Response**

```json
{
    "id": 1,
    "name": "Netflix",
    "category": "streaming",
    "cost": 12.99,
    "billing_cycle": "Monthly",
    "date_of_payment": "2024-10-15"
}
```

## **Contributing**

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.


# this is the backend.
to set up the database url do this:
    make a .env file locally and have it like this:
            DATABASE_URL= 'the url without quotations'
            SECRET_KEY='i'll share this'


this is currently working for signup, signin and logout.

# set up
--make a virtual environment
--pip install requirements.txt
--uncomment the code on app.py to run local development and comment it when you push because of render



