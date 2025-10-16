# HNG_13_Stage_Zero
HNG_13_Stage_Zero repo
# HNG Backend Wizards — Stage 0 Task

## 📌 Description
A simple RESTful API endpoint `/me` that returns my profile information and a random cat fact fetched dynamically from the [Cat Facts API](https://catfact.ninja/fact).

## 🚀 Technologies
- Python 3.x
- Django
- Django REST Framework
- Requests library

---

## 🚀 Features
- Returns structured JSON data with personal and technical details.
- Fetches a random cat fact dynamically from an external API.
- Includes timestamp in ISO 8601 format.
- Built using Django and Django REST Framework.
- Deployed live on [PythonAnywhere](https://12345678franklin.pythonanywhere.com/me).

---

## 🧠 Example JSON Response
```json
{
  "status": "success",
  "user": {
    "email": "okumborfranklin@gmail.com",
    "name": "Franklin07",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-15T23:50:05.726909+00:00",
  "fact": "Could not get cat facts at the moment"
}
```

## 🧩 Project Structure
```
HNG_13_Stage_Zero/
│
├── core/
├── profile_api/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

## ⚙️ Setup Instructions
## 1️⃣ Clone the Repository
```bash
git clone https://github.com/Abraham-Franklin/hng_stage0_backend.git
cd hng_stage0_backend
git clone https://github.com/Abraham-Franklin/HNG_13_Stage_Zero.git
cd HNG_13_Stage_Zero
```

## 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```

## Activate it:

## Windows:
```bash
venv\Scripts\activate
```

## Linux/Mac:
```bash
source venv/bin/activate
```

## 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 4️⃣ Run Migrations
```bash
python manage.py migrate
```

## 5️⃣ Run the Development Server
```bash
python manage.py runserver
```

## 🧰 Dependencies
All required packages are listed in requirements.txt, but here’s a quick overview:
```text
Django==5.1.1
djangorestframework==3.15.2
requests==2.32.3
```

## If you ever need to reinstall manually:
```bash
pip install Django djangorestframework requests
```

## 🔐 Environment Variables
there was no environment variable used















