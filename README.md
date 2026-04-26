# Leave Management System

Full stack leave management system built with FastAPI and JavaScript.

## Features
- Create leave requests
- Approve / reject requests
- Admin panel
- Search and filtering
- Error handling

## Tech Stack
- Backend: FastAPI (Python)
- Frontend: HTML, Bootstrap, JavaScript
- Data Storage: JSON

## Project Structure
backend/
  main.py
  db.json
frontend/
  index.html
  admin.html

## Installation

### Backend
cd backend
python -m uvicorn main:app --reload

### Frontend
cd frontend
python -m http.server 5500

## Usage
Open: http://127.0.0.1:5500  
Admin Panel: http://127.0.0.1:5500/admin.html

## API Endpoints
- POST /izin-talep
- GET /izinler
- PUT /izin-durum/{id}

  ## Author
Meriç Düzel
