# 🔗 Shrink Track Backend

A secure, authenticated URL shortener API built with Django REST Framework. It supports automatic short URL generation, redirection logic, and per-user rate limiting

---

## 🌐 Deployment

**Live API**: [https://shrink-track.onrender.com/](https://shrink-track.onrender.com/)

---

## 🧩 Features

- ✅ User Registration and Token Authentication
- 🔐 Per-user Rate Limiting (5 requests/minute)
- 🔗 Unique 6-character URL shortening
- ↩️ Automatic Redirection using short codes
- 🧼 Validation for duplicate email, username, and password confirmation
- 🧹 Secure deletion of user accounts

---

## 🚀 Endpoints

### 🔐 Auth & User

| Method | Endpoint                  | Description                    | Auth Required |
|--------|---------------------------|--------------------------------|----------------|
| POST   | `/user/create/`           | Create a new user              | ❌             |
| POST   | `/user/get-token/`        | Obtain auth token              | ❌             |
| DELETE | `/user/delete/`           | Delete current user account    | ✅             |

### 🔗 URL Shortener

| Method | Endpoint         | Description                           | Auth Required |
|--------|------------------|---------------------------------------|----------------|
| POST   | `/api/shrink/`   | Submit an original URL to shrink it  | ✅             |
| GET    | `/<code>/`       | Redirect to original URL using code  | ❌             |

---

## 🛠️ How It Works

### ▶️ URL Shortening Flow

1. A logged-in user sends a `POST` to `/api/shrink/` with their original URL.
2. The system:
   - Generates a **unique 6-character alphanumeric code**
   - Builds a **public short URL**
   - Stores the original + short URL pair along with the user
3. The response contains the shrinked URL.
4. The short URL can be used for redirection via `GET /<code>/`.

### 🔁 Redirection Logic

Handled in `shrinktrack/redirect.py`, the app fetches the matching `ShrinkInstanceModel` using the `shrinked_url` and redirects to the `original_url`.

---

## 🧪 Example Request

### 🔗 Shrink URL

```bash
POST /api/shrink/
Authorization: Token <your-token>
Content-Type: application/json

{
  "original_url": "https://example.com"
}
````

### 🔁 Redirect

Navigate to:

```
https://shrink-track.onrender.com/<code>/
```

---

## ⚙️ Tech Stack

* Python 3.10+
* Django 4.x
* Django REST Framework
* SQLite (default, can be switched)
* Token Authentication
* Render for Deployment
