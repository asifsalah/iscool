# iScool - School Management System

A comprehensive school management system built with Django, Next.js, and Supabase.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: Next.js
- **Database**: Supabase
- **Authentication**: Supabase Auth

## Features (Planned)

- User Management (Admin, Teachers, Students, Parents)
- Class/Course Management
- Attendance Management
- Grade Management
- Schedule/Timetable Management
- Communication Portal
- Reports and Analytics
- Fee Management

## Project Structure

```
iscool/
├── backend/         # Django backend
│   ├── core/       # Core Django app
│   ├── api/        # REST API endpoints
│   └── manage.py
├── frontend/        # Next.js frontend
└── README.md
```

## Setup Instructions

### Backend Setup
1. Create a virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver`

### Frontend Setup
1. Install dependencies: `npm install`
2. Run development server: `npm run dev`

## Environment Variables

Create `.env` files in both backend and frontend directories with the following variables:

### Backend (.env)
```
DEBUG=True
SECRET_KEY=your_django_secret_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

### Frontend (.env.local)
```
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
```
