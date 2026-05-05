# WorkCRM 🧑‍💼

A lightweight CRM (Customer Relationship Management) web application built with Django to manage customers, track interactions, and streamline business workflows.

---

## 🚀 Features

* 📇 Manage customer records
* 📝 Track interactions and activities
* 🔐 Admin dashboard for easy control
* ⚡ Lightweight and fast
* 🧱 Scalable Django backend

---

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Server:** Gunicorn
* **Static Files:** WhiteNoise
* **Deployment:** Render
* **Version Control:** Git & GitHub

---

## 📦 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/workcrm.git
cd workcrm
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the server

```bash
python manage.py runserver
```

App runs at:
👉 http://127.0.0.1:8000/

---

## 🔐 Admin User & Password Setup

### Create Admin User

```bash
python manage.py createsuperuser
```

Enter:

* Username
* Email (optional)
* Password

---

### Access Admin Panel

👉 http://127.0.0.1:8000/admin/

---

### Change Password

```bash
python manage.py changepassword <username>
```

Example:

```bash
python manage.py changepassword admin
```

---

### Reset Password (if forgotten)

```bash
python manage.py shell
```

```python
from django.contrib.auth.models import User
user = User.objects.get(username='admin')
user.set_password('newpassword')
user.save()
```

---

## ☁️ Deployment (Render)

This project is configured for deployment on Render.

---

### 🚀 Steps to Deploy

1. Push code to GitHub
2. Go to Render Dashboard
3. Click **New → Web Service**
4. Connect your GitHub repository
5. Select your repo and branch

---

### ⚙️ Configuration

**Build Command**

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

**Start Command**

```bash
gunicorn workcrm.wsgi
```

---

### 🌍 Environment Variables

Add these in Render dashboard:

```env
PYTHON_VERSION=3.11.0
```

---

## 📁 Project Structure

```
workcrm/
├── manage.py
├── workcrm/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── requirements.txt
├── .gitignore
```

---

## ⚙️ Important Settings

Make sure these are set in `settings.py`:

```python
import os

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

WhiteNoise middleware:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
```

---

## 🧠 Notes

* SQLite is used for development
* Static files are served using WhiteNoise
* First deploy may take a few minutes
* If app crashes, check Render logs

---

## ✨ Future Improvements

* User authentication & role-based access
* Dashboard analytics
* REST API (Django REST Framework)
* PostgreSQL integration
* UI improvements

---

## 👩‍💻 Author

Akshita

---

## 📜 License

This project is licensed under the MIT License.
