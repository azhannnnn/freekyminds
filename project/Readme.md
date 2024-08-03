# Restaurant Review Platform

## Overview

This project is a simple restaurant review platform built with Django. Users can sign up, log in, and post reviews for restaurants. The project includes user authentication, CRUD operations for restaurants and reviews, and a basic API using Django REST Framework.

## Features

- User authentication (sign up, login, logout)
- Restaurant management (create, view, update, delete)
- Review management (add reviews to restaurants)
- RESTful API for restaurants and reviews

## Requirements

- Python 3.8 or higher
- Django 5.0.7
- Django REST Framework

## Installation

### Clone the Repository

```bash
git clone https://github.com/azhannnnn/freekyminds.git
cd freekyminds
```

### Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Set Up the Database

Run migrations to set up the database:

```bash
python manage.py migrate
```

### Create a Superuser (Optional)

Create a superuser to access the Django admin:

```bash
python manage.py createsuperuser
```

### Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your web browser to access the application.

## Usage

- **Home Page:** Displays a welcome message.
- **Sign Up:** Create a new user account.
- **Login:** Access your account.
- **Logout:** Sign out of your account.
- **Restaurants:** View the list of restaurants, create new ones, and manage existing ones.
- **Reviews:** Add and view reviews for each restaurant.

### API Endpoints

- **List Restaurants:** `GET /api/restaurants/`
- **Restaurant Detail:** `GET /api/restaurants/<int:pk>/`
- **List Reviews:** `GET /api/reviews/`

## Troubleshooting

- **CSRF Token Issues:** Ensure `{% csrf_token %}` is included in all POST forms and verify the CSRF middleware is enabled in `settings.py`.
- **Database Errors:** Run `python manage.py migrate` to apply database migrations.

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This `README.md` file provides clear instructions for setting up and running your project, with the correct GitHub repository URL included. Make sure to update or add additional sections if there are specific instructions or requirements for your project.