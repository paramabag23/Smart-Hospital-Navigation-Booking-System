# 🏥 LifeLine+ — Smart Hospital Management System

LifeLine+ is a Flask-based web application for managing common hospital
services: doctor appointments, bed bookings, ambulance requests, medicine
orders, blood requests, emergency alerts, payments, indoor navigation, a
basic symptom-checker, and a GPS distance estimator — all from a single
patient dashboard.

## ✨ Features

| Module | Description |
|---|---|
| 🔐 Auth | Signup/login with SHA-256 password hashing, session-based access control |
| 👨‍⚕️ Doctor Booking | Pick a department, doctor, date & time slot; conflict checking prevents double-booking |
| 🛏️ Bed Booking | Reserve General/Semi-Private/Private/ICU/Emergency beds |
| 🚑 Ambulance Booking | Request pickup with patient & contact details |
| 💊 Medicine Ordering | Browse a small in-app pharmacy catalog with live total calculation |
| 🩸 Blood Requests | Request blood units by type from a chosen blood bank |
| 🚨 Emergency | One-tap emergency dispatch alert, logged with timestamp |
| 📋 My Appointments | View & cancel appointments |
| 💰 Payments | Pay for pending appointments, view payment history & totals |
| 🤖 AI Assistant | Keyword-based symptom checker that suggests a department |
| 📍 GPS Calculator | Estimated distance/time/fare to the hospital |
| 🗺️ Navigation | Simple indoor wayfinding between hospital locations |

## 🛠️ Tech Stack

- **Backend:** Python, Flask 2.2.3
- **Database:** SQLite (`hospital.db`)
- **Frontend:** Jinja2 templates, vanilla CSS/JS
- **Deployment:** Configured for Vercel (`vercel.json`, `@vercel/python`)

## 📁 Expected Project Structure

Flask expects templates and static assets in specific folders. Arrange the
uploaded files like this before running:

```
lifeline-plus/
├── main.py
├── requirements.txt
├── vercel.json
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── doctor_booking.html
│   ├── bed_booking.html
│   ├── ambulance_booking.html
│   ├── medicine_booking.html
│   ├── blood_booking.html
│   ├── navigation.html
│   ├── emergency.html
│   ├── appointments.html
│   ├── payment.html
│   ├── payment_history.html
│   ├── ai_assistant.html
│   └── gps_calculator.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
└── hospital.db        # auto-created on first run
```

## 🚀 Getting Started

```bash
# 1. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python main.py
```

The app runs at **http://localhost:5001**.

On first run, the database is created automatically along with a test account:

- **Email:** `test@test.com`
- **Password:** `test123`

## 🗄️ Database Schema

| Table | Key Columns |
|---|---|
| `users` | id, name, email (unique), phone, password (hashed), user_type |
| `appointments` | id, user_id, doctor_name, department, appointment_date, appointment_time, status |
| `emergencies` | id, user_id, location, emergency_type, created_at |
| `payments` | id, user_id, appointment_id, amount, payment_method, status, created_at |

## 🔗 Routes

| Route | Methods | Purpose |
|---|---|---|
| `/` | GET | Redirects to login |
| `/login` | GET, POST | User login |
| `/signup` | GET, POST | User registration |
| `/logout` | GET | Clear session |
| `/dashboard` | GET | Overview + stats |
| `/book-doctor` | GET, POST | Book a doctor appointment |
| `/book-bed` | GET, POST | Book a hospital bed |
| `/book-ambulance` | GET, POST | Request an ambulance |
| `/book-medicine` | GET, POST | Order medicine |
| `/book-blood` | GET, POST | Request blood units |
| `/navigation` | GET, POST | Indoor directions |
| `/emergency` | GET, POST | Trigger emergency dispatch |
| `/my-appointments` | GET | List appointments |
| `/cancel-appointment/<id>` | POST | Cancel an appointment |
| `/payment` | GET, POST | Pay for a pending appointment |
| `/payment-history` | GET | View past payments |
| `/ai-assistant` | GET, POST | Symptom → department suggestion |
| `/gps-calculator` | GET, POST | Estimate distance/fare to hospital |
| `/get-doctors/<department>` | GET | JSON list of doctors (used by booking form) |

## ☁️ Deploying to Vercel

`vercel.json` currently points to `api/index.py`, but the Flask app lives in
`main.py` at the project root. To deploy as-is on Vercel, either:

- move/rename `main.py` to `api/index.py`, **or**
- update `vercel.json`'s `src`/`dest` paths to point at `main.py`.

Also note Vercel's filesystem is read-only at runtime, so the SQLite file
(`hospital.db`) will not persist between deployments/requests — a hosted
database (e.g. Postgres, Turso, PlanetScale) is recommended for production.

## ⚠️ Known Limitations / Before Production Use

- **Hardcoded secret key** (`app.secret_key`) — replace with an environment
  variable.
- **Password hashing** uses unsalted SHA-256 — consider `werkzeug.security`
  (`generate_password_hash`/`check_password_hash`) or `bcrypt`.
- **AI Assistant** is a simple keyword-matching lookup, not a real ML/AI model.
- **GPS Calculator** returns randomized mock distances, not real geolocation data.
- Doctors, departments, medicines, blood banks, and time slots are hardcoded
  in `main.py` rather than stored in the database.
- `main.py` contains large blocks of commented-out legacy code (an earlier
  Tkinter desktop version and an earlier Flask draft) — safe to delete for
  a cleaner codebase; only the final Flask app (bottom of the file) is
  actually used.
- No file storage is currently used, though an `uploads/` folder is
  referenced in earlier drafts for prescription uploads — not implemented
  in the live app.
