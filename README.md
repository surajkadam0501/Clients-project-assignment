---

# Django Client-Project Management System

This Django application manages clients, projects, and user assignments to projects. It also includes user management APIs for creating, updating, and deleting users.

## Features

1. **User Management**: CRUD operations for users via API Or Uses Django's built-in User model.
2. **Client Management**: CRUD operations for clients.
3. **Project Management**: Create and assign users to projects.
4. **Retrieve Assigned Projects**: Fetch projects assigned to the logged-in user.

## Tech Stack

- Django 4.x
- Django REST Framework
- MySQL

## Setup Instructions

### Prerequisites

- Python 3.8+
- MySQL Server
- Virtualenv (optional but recommended)

### Steps

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

#### 2. Set up Virtual Environment

It's recommended to use a virtual environment for your Python project:

```bash
virtualenv env
env\Scripts\activate  # On Windows
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. MySQL Database Configuration

1. Create a MySQL database named `client`:

```sql
CREATE DATABASE client;
```

2. Set up your MySQL credentials in `settings.py`:

```python
# settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'client',
        'USER': 'root',
        'PASSWORD': 'root@123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### 5. Apply Migrations

Run the following commands to create the necessary database tables:

```bash
python manage.py migrate
```

#### 6. Create a Superuser

Create a superuser to access Django's admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser.

#### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Access the admin panel at: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## API Endpoints

### 1. User Management APIs

These endpoints allow CRUD operations on users.

#### List All Users

**URL**: `GET /api/users/`

**Response**:
```json
[
  { "id": 1, "username": "admin" },
  { "id": 2, "username": "prasad" }
]
```

#### Retrieve a Specific User

**URL**: `GET /api/users/<id>/`

**Response**:
```json
{
  "id": 1,
  "username": "prasha"
}
```

#### Create a New User

**URL**: `POST /api/users/`

**Request**:
```json
{
  "username": "new_user",
  "password": "password123",
  "email": "new_user@example.com"
}
```

**Response**:
```json
{
  "id": 3,
  "username": "new_user",
  "email": "new_user@example.com"
}
```

#### Update a User

**URL**: `PUT /api/users/<id>/`

**Request**:
```json
{
  "username": "updated_user",
  "email": "updated_user@example.com"
}
```

#### Delete a User

**URL**: `DELETE /api/users/<id>/`

**Response**: Status 204 (No Content)

### 2. Client Management APIs

#### List All Clients

**URL**: `GET /clients/`

**Response**:
```json
[
  {
    "id": 1,
    "client_name": "Nimap",
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "admin"
  },
  {
    "id": 2,
    "client_name": "Infotech",
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "admin"
  }
]
```

#### Create a New Client

**URL**: `POST /clients/`

**Request**:
```json
{
  "client_name": "Company A"
}
```

**Response**:
```json
{
  "id": 3,
  "client_name": "Company A",
  "created_at": "2019-12-24T11:03:55.931739+05:30",
  "created_by": "admin"
}
```

#### Retrieve Client Info with Projects

**URL**: `GET /clients/<id>/`

**Response**:
```json
{
  "id": 2,
  "client_name": "Infotech",
  "projects": [
    {
      "id": 1,
      "name": "Project A"
    }
  ],
  "created_at": "2019-12-24T11:03:55.931739+05:30",
  "created_by": "admin",
  "updated_at": "2019-12-24T11:03:55.931739+05:30"
}
```

#### Update Client Info

**URL**: `PUT /clients/<id>/`

**Request**:
```json
{
  "client_name": "Updated Company A"
}
```

**Response**:
```json
{
  "id": 3,
  "client_name": "Updated Company A",
  "created_at": "2019-12-24T11:03:55.931739+05:30",
  "created_by": "admin",
  "updated_at": "2019-12-24T11:03:55.931739+05:30"
}
```

#### Delete a Client

**URL**: `DELETE /clients/<id>/`

**Response**: Status 204 (No Content)

---

### 3. Project Management APIs

#### Create a New Project and Assign Users

**URL**: `POST /clients/<client_id>/projects/`

**Request**:
```json
{
  "project_name": "Project A",
  "users": [1, 2]
}
```

**Response**:
```json
{
  "id": 3,
  "project_name": "Project A",
  "client": "Nimap",
  "users": [
    {
      "id": 1,
      "name": "prasha"
    },
    {
      "id": 2,
      "name": "vishal"
    }
  ],
  "created_at": "2019-12-24T11:03:55.931739+05:30",
  "created_by": "admin"
}
```

#### List Projects Assigned to Logged-in User

**URL**: `GET /projects/`

**Response**:
```json
[
  {
    "id": 1,
    "project_name": "Project A",
    "created_at": "2019-12-24T11:03:55.931739+05:30",
    "created_by": "admin"
  }
]
```

---

## Example Flow

1. **Create a Client**:
   ```bash
   POST /clients/ 
   Request: { "client_name": "Company A" }
   Response: { "id": 3, "client_name": "Company A", ... }
   ```

2. **Create a Project and Assign Users**:
   ```bash
   POST /clients/3/projects/
   Request: { "project_name": "Project A", "users": [1, 2] }
   Response: { "id": 3, "project_name": "Project A", ... }
   ```

3. **Retrieve Projects Assigned to Logged-in User**:
   ```bash
   GET /projects/
   Response: [{ "id": 1, "project_name": "Project A", ... }]
   ```

---

## Running Tests

Run the following command to execute the tests:

```bash
python manage.py test
```