# 🎮 GameBacklog API

Track the games you want to play, are currently playing, or have already finished.

---

## ⚙️ Setup Instructions

### 1. Create & activate a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run migrations
```bash
python manage.py migrate
```

### 4. Start the development server
```bash
python manage.py runserver
```

---

## 🌐 API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/api/v1/games/` | List all games |
| POST | `/api/v1/games/` | Add a new game |
| GET | `/api/v1/games/{id}/` | Get a specific game |
| PUT | `/api/v1/games/{id}/` | Update a game (all fields) |
| PATCH | `/api/v1/games/{id}/` | Partially update a game |
| DELETE | `/api/v1/games/{id}/` | Delete a game |

### Swagger UI
Open: [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)

---

## ✅ Validation Rules

1. **`hours_played` cannot be negative.**
2. **If `status` is `"Finished"`, `hours_played` must be greater than 0.**

### Example — Valid POST
```json
POST /api/v1/games/
{
  "title": "Elden Ring",
  "platform": "PC",
  "status": "Playing",
  "hours_played": 120
}
```

### Example — Invalid POST (Finished with 0 hours)
```json
POST /api/v1/games/
{
  "title": "God of War",
  "platform": "PS4",
  "status": "Finished",
  "hours_played": 0
}
// Response 400: A game marked as 'Finished' must have hours_played greater than 0.
```

---

## 🧪 Running Automated Tests

```bash
python manage.py test
```

Expected output:
```
Ran 7 tests in X.XXXs
OK
```

---

## 🗂 Git Workflow

```bash
# Initialize Git
git init
git add .
git commit -m "Initial model setup – Game model with title, platform, status, hours_played"

git add games/serializers.py
git commit -m "Added serializer validation – negative hours and Finished with 0 hours"

git add games/views.py games/urls.py gamebacklog_project/urls.py gamebacklog_project/settings.py
git commit -m "Implemented versioned REST API /api/v1/games/ with DefaultRouter"

git add .
git commit -m "Implemented Swagger documentation via drf-spectacular"

git add games/tests.py
git commit -m "Added automated tests – POST 201, validation errors, CRUD operations"
```

---

## 🗂 Project Structure

```
gamebacklog_project/
├── manage.py
├── requirements.txt
├── README.md
├── gamebacklog_project/
│   ├── __init__.py
│   ├── settings.py       ← REST_FRAMEWORK versioning + drf-spectacular config
│   ├── urls.py           ← /api/<version>/ + /api/docs/
│   └── wsgi.py
└── games/
    ├── __init__.py
    ├── admin.py
    ├── models.py         ← Game model
    ├── serializers.py    ← Validation logic
    ├── views.py          ← GameViewSet (ModelViewSet)
    ├── urls.py           ← DefaultRouter
    ├── tests.py          ← 7 automated tests
    └── migrations/
        ├── __init__.py
        └── 0001_initial.py
```

---

## 👥 Team Members
<!-- Add your names here -->
- Member 1 – Model & Admin
- Member 2 – Serializer & Validation
- Member 3 – Views, URLs & Versioning
- Member 4 – Swagger & Tests
