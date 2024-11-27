# Django Authentication System

This project implements a simple Django-based authentication system with features like user login, signup, password reset, profile management, and dashboard. The application allows users to securely sign up, log in, change passwords, and reset passwords. It also includes a profile page where users can view and update their details.

## Features

- **User Authentication**:
  - Sign Up: Users can register with a username, email, and password.
  - Login: Users can log in using their username/email and password.
  - Forgot Password: Users can reset their password by receiving a reset link via email.
  - Change Password: Authenticated users can change their password.

- **Dashboard**:
  - A user-friendly dashboard displaying a welcome message and links to profile and password change pages.
  - Logout functionality to end the session.

- **Profile Page**:
  - Displays user information like username, email, date joined, and last updated.
  - Allows users to update their details.

## Installation

### Prerequisites

Before you start, make sure you have the following installed on your local machine:

- [Python 3.x](https://www.python.org/downloads/)
- [Django](https://www.djangoproject.com/)
- [Git](https://git-scm.com/)

## Steps to Install


**Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   ```
 Create a Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
cd your-repository-name
python -m venv .venv
```
Activate the Virtual Environment

For Windows:
```
bash
Copy code
.\.venv\Scripts\activate
```
For macOS/Linux:

``` bash
Copy code
source .venv/bin/activate
Install Dependencies
```

Install the required dependencies:

``` bash
Copy code
pip install -r requirements.txt
```

### Database Migrations

Run the database migrations to set up the necessary tables:
```
bash

python manage.py migrate

```

Create a Superuser

### Create a superuser account to manage the application:
```
bash

python manage.py createsuperuser

```
Follow the prompts to set up the superuser.

Run the Development Server

### Start the Django development server:

``` bash
Copy code
python manage.py runserver
```

### Access the Application

Open your browser and navigate to:

```bash
http://127.0.0.1:8000/
```

