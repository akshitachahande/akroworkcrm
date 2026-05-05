# WorkCRM 🧑‍💼

A simple CRM web app built with Django to help manage customers and keep track of interactions without overcomplicating things.

This project started as a hands-on way to build and deploy a real-world Django application.

---

## 🚀 What it does

* Store and manage customer details
* Track interactions/activities
* Use Django admin for quick management
* Keeps things minimal and easy to use

---

## 🛠️ Built with

* Django (Python)
* Gunicorn
* WhiteNoise (for static files)
* Deployed on Render
* GitHub for version control

---

## 📦 Running locally

### 1. Clone the repo

```bash id="h7q9yq"
git clone https://github.com/YOUR_USERNAME/workcrm.git
cd workcrm
```

### 2. Set up environment

```bash id="y7q5u0"
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies

```bash id="v1rqqt"
pip install -r requirements.txt
```

### 4. Run migrations

```bash id="qmqz9k"
python manage.py migrate
```

### 5. Start server

```bash id="kqg63y"
python manage.py runserver
```

Open: http://127.0.0.1:8000/

---

## 🔐 Admin access

Create an admin user:

```bash id="s0m4gl"
python manage.py createsuperuser
```

Login here:
http://127.0.0.1:8000/admin/

---

## 🔁 Change password

```bash id="4u2aeh"
python manage.py changepassword <username>
```

---

## ☁️ Deployment (Render)

This app is deployed using Render.

**Build Command**

```bash id="3k6t2p"
pip install -r requirements.txt && python manage.py collectstatic --noinput
```

**Start Command**

```bash id="c9t7mx"
gunicorn workcrm.wsgi
```

---

## ⚙️ Important settings

Make sure in `settings.py`:

```python id="9r2d1s"
import os

ALLOWED_HOSTS = ['*']

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

WhiteNoise middleware should be enabled.

---

## 🧠 Notes

* Uses SQLite for now
* Meant as a learning + practical project
* Can be extended with more features easily

---

## 👩‍💻 About

Built by Akshita as part of learning, building, and actually shipping a real project 🚀
