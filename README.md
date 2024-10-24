# Subscriptly Backend

Subscriptly is a subscription management API built with Flask, SQLAlchemy, and Flask-RESTful. It provides user authentication and management features, allowing users to create, list, update, and delete subscriptions.

## Features

- User registration and authentication
- Subscription management (create, list, delete)
- Secure password handling using Flask-Bcrypt
- API documentation with Swagger

## Technologies Used

- Python 3.x
- Flask
- Flask-SQLAlchemy
- Flask-RESTful
- Flask-Migrate
- Flask-CORS
- Flask-Bcrypt
- Flasgger (for API documentation)
- PostgreSQL (for database)

## Setup

### Prerequisites

- Python 3.x
- PostgreSQL
- Virtual environment (recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone <your-repo-url>
   cd subscriptly-backend

2. Create a virtual environment:

    ```bash
    Copy code
    python -m venv .venv
    source .venv/bin/activate  # On Windows use .venv\Scripts\activate

3. Install the required packages:

    ```bash
    Copy code
    pip install -r requirements.txt
    Set up your environment variables:

4. Create a .env file in the root directory and add the following:

    DATABASE_URL=<your-database-url>
    SECRET_KEY=<your-secret-key>`

5. Initialize the database:

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade

6. Running the Application
    To run the application locally, use the following command:

    ```bash
    python app.py
    The API will be accessible at http://localhost:5000.

# API Documentation
    API documentation is available at:
    http://localhost:5000/apidocs/ -- local test
    https://test-backend-e4ae.onrender.com/apidocs/
    You can use a dummy user ID 86 for some tests


# Endpoints
1. User Management

    POST /users - Register a new user
    POST /login - Log in a user
    GET /user/{user_id} - Get user profile
    PUT /user/{user_id} - Update user profile

2. Subscription Management

    GET /user/{user_id}/subscriptions - List user subscriptions
    POST /user/{user_id}/subscriptions - Create a new subscription
    DELETE /user/{user_id}/subscriptions/{subscription_id} - Delete a subscription

### Contributing
Contributions are welcome! Please fork the repository and create a pull request.

