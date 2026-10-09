# Django REST Framework Model Mixins API

## Project Overview

This project is a REST API developed using Python, Django, and Django REST Framework. It demonstrates CRUD operations for social media status posts using generic class-based views, model mixins, and serializers.

The API manages user information and status posts, including titles, descriptions, social media platforms, upload timestamps, and images.

## Features

- Retrieve all status posts
- Create new status posts
- Retrieve individual status details
- Update existing status posts
- Delete status posts
- Manage user information
- Display related user details using nested serializers
- Support image uploads for status posts
- Use Django REST Framework generic class-based views and mixins

## Technologies Used

- Python
- Django
- Django REST Framework
- Django Models
- ModelSerializer
- Generic Class-Based Views
- Model Mixins
- SQLite / Configured Database
- HTML and JSON

## API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Retrieve all status posts |
| POST | `/` | Create a new status post |
| GET | `/<int:pk>` | Retrieve a status by ID |
| PUT | `/<int:pk>` | Update a status by ID |
| DELETE | `/<int:pk>` | Delete a status by ID |

## Project Structure

```text
project/
├── config/
│   ├── settings.py
│   └── urls.py
├── modelmixapp/
│   ├── migrations/
│   ├── models.py
│   ├── serializer.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── manage.py
└── README.md
```

## Installation and Setup

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework pillow
```

### 4. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open the following URL in your browser:

`http://127.0.0.1:8000/`

## Model Details

### User Model

Stores user information, including:

- Username
- Age
- Phone number
- Email
- Address

### Status Model

Stores social media status information, including:

- Title
- Subtitle
- Social media platform
- Description
- Upload time
- Image
- Related user

Supported social media platforms include Facebook, Instagram, WhatsApp, Snapchat, Twitter, and TikTok.

## Key Concepts Demonstrated

- Django models and relationships
- Django REST Framework serializers
- Nested serializers
- Generic class-based views
- Create, update, and delete model mixins
- REST API endpoint design
- Image field configuration

## Learning Outcome

This project demonstrates how to build a REST API using Django REST Framework generic views and mixins to manage status records and related user information.

## Author

**Azad Hussain**

GitHub: https://github.com/azadhussain92
