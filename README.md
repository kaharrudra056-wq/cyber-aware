# 🛡️ Cybersecurity Awareness Training Website

A full-stack web application built with **Python Flask + PostgreSQL/SQLite** for B.Sc. IT mini project.

## Tech Stack
| Part | Technology |
|------|------------|
| Frontend | HTML5 + Bootstrap 5 |
| Backend | Python + Flask |
| Database | PostgreSQL (external) / SQLite (local) |
| ORM | SQLAlchemy |
| Auth | Flask-Login + Werkzeug |
| Templates | Jinja2 |

## Features
- ✅ User Registration & Login
- 📚 8 Cybersecurity Topics with rich content
- 🧩 Quiz System with score tracking
- 📊 User Dashboard with progress tracking
- 🎣 Phishing Awareness Simulator
- ⚙️ Admin Panel (manage questions, view scores)
- 🗄️ PostgreSQL external database support

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure database
Copy `.env.example` to `.env` and set your values:
```bash
copy .env.example .env
```
For **PostgreSQL** (external): Set `DATABASE_URL=postgresql://user:pass@host:5432/dbname`  
For **SQLite** (local): Leave `DATABASE_URL` empty

### 3. Initialize and seed database
```bash
python seed_data.py
```

### 4. Run the application
```bash
python app.py
```

Visit: http://localhost:5000

## Default Admin Login
- Email: `admin@cybersec.com`
- Password: `Admin@1234`

## Free PostgreSQL Hosting
- [Supabase](https://supabase.com) - Free tier, 500MB
- [Railway](https://railway.app) - Free tier PostgreSQL
- [Render](https://render.com) - Free PostgreSQL
- [Neon](https://neon.tech) - Serverless PostgreSQL, generous free tier
