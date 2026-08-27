










from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import datetime
import sqlite3
import hashlib
import os
import random
from functools import wraps


# =========================================================
# APP CONFIGURATION
# =========================================================

app = Flask(__name__)

# Use environment variable on Vercel
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "lifeline-secret-key-change-this"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Vercel serverless environment:
# /tmp is writable.
# Local computer:
# project folder is used.
if os.environ.get("VERCEL"):
    DATABASE_PATH = "/tmp/hospital.db"
else:
    DATABASE_PATH = os.path.join(BASE_DIR, "hospital.db")


# =========================================================
# DATABASE
# =========================================================

def get_db():
    """Create and return SQLite database connection."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def hash_password(password):
    """Hash password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()


def init_database():
    """Create all required database tables."""

    conn = get_db()
    cursor = conn.cursor()

    # -------------------------
    # USERS
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL,
            password TEXT NOT NULL,
            user_type TEXT DEFAULT 'patient'
        )
    """)

    # -------------------------
    # APPOINTMENTS
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            doctor_name TEXT NOT NULL,
            department TEXT NOT NULL,
            appointment_date TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            status TEXT DEFAULT 'pending'
        )
    """)

    # -------------------------
    # EMERGENCIES
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emergencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            location TEXT,
            emergency_type TEXT,
            created_at TEXT
        )
    """)

    # -------------------------
    # PAYMENTS
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            appointment_id INTEGER,
            amount REAL NOT NULL,
            payment_method TEXT,
            status TEXT DEFAULT 'pending',
            created_at TEXT
        )
    """)

    conn.commit()

    # -------------------------
    # TEST USER
    # -------------------------
    cursor.execute(
        "SELECT id FROM users WHERE email=?",
        ("test@test.com",)
    )

    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO users
            (name, email, phone, password, user_type)
            VALUES (?, ?, ?, ?, ?)
        """, (
            "Test User",
            "test@test.com",
            "9876543210",
            hash_password("test123"),
            "patient"
        ))

        conn.commit()
        print("Test user created.")

    conn.close()

    print("Database initialized successfully!")


# =========================================================
# LOGIN REQUIRED
# =========================================================

def login_required(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):

        if "user_id" not in session:
            flash("Please login to access this page", "warning")
            return redirect(url_for("login"))

        return function(*args, **kwargs)

    return decorated_function


# =========================================================
# HOME
# =========================================================

@app.route("/")
def index():
    return redirect(url_for("login"))


# =========================================================
# LOGIN
# =========================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Please enter email and password", "danger")
            return render_template("login.html")

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, name, email, user_type
            FROM users
            WHERE email=? AND password=?
        """, (
            email,
            hash_password(password)
        ))

        user = cursor.fetchone()

        conn.close()

        if user:

            session["user_id"] = user["id"]
            session["user_name"] = user["name"]
            session["user_type"] = user["user_type"]

            flash(
                f'Welcome back, {user["name"]}!',
                "success"
            )

            return redirect(url_for("dashboard"))

        flash("Invalid email or password!", "danger")

    return render_template("login.html")


# =========================================================
# SIGNUP
# =========================================================

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")
        user_type = request.form.get("user_type", "patient")

        if not all([name, email, phone, password]):

            flash(
                "All fields are required!",
                "danger"
            )

            return render_template("login.html")

        if password != confirm_password:

            flash(
                "Passwords do not match!",
                "danger"
            )

            return render_template("login.html")

        if len(password) < 6:

            flash(
                "Password must be at least 6 characters!",
                "danger"
            )

            return render_template("login.html")

        conn = get_db()
        cursor = conn.cursor()

        try:

            cursor.execute("""
                INSERT INTO users
                (name, email, phone, password, user_type)
                VALUES (?, ?, ?, ?, ?)
            """, (
                name,
                email,
                phone,
                hash_password(password),
                user_type
            ))

            conn.commit()

            flash(
                "Registration successful! Please login.",
                "success"
            )

            return redirect(url_for("login"))

        except sqlite3.IntegrityError:

            flash(
                "Email already registered!",
                "danger"
            )

        finally:
            conn.close()

    return render_template("login.html")


# =========================================================
# LOGOUT
# =========================================================

@app.route("/logout")
def logout():

    session.clear()

    flash(
        "Logged out successfully",
        "info"
    )

    return redirect(url_for("login"))


# =========================================================
# DASHBOARD
# =========================================================

@app.route("/dashboard")
@login_required
def dashboard():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM appointments
        WHERE user_id=?
    """, (
        session["user_id"],
    ))

    appointment_count = cursor.fetchone()[0]

    cursor.execute("""
        SELECT
            id,
            doctor_name,
            department,
            appointment_date,
            appointment_time,
            status
        FROM appointments
        WHERE user_id=?
        ORDER BY id DESC
        LIMIT 5
    """, (
        session["user_id"],
    ))

    recent_appointments = cursor.fetchall()

    conn.close()

    return render_template(
        "dashboard.html",
        user_name=session.get("user_name"),
        user_type=session.get("user_type"),
        appointment_count=appointment_count,
        recent_appointments=recent_appointments
    )


# =========================================================
# DOCTOR APPOINTMENT
# =========================================================

@app.route("/book-doctor", methods=["GET", "POST"])
@login_required
def book_doctor():

    doctors = {
        "Cardiology": [
            "Dr. Smith",
            "Dr. Johnson",
            "Dr. Williams"
        ],
        "Neurology": [
            "Dr. Brown",
            "Dr. Jones",
            "Dr. Garcia"
        ],
        "Pediatrics": [
            "Dr. Miller",
            "Dr. Davis",
            "Dr. Rodriguez"
        ],
        "Orthopedics": [
            "Dr. Wilson",
            "Dr. Martinez",
            "Dr. Anderson"
        ],
        "General Medicine": [
            "Dr. Taylor",
            "Dr. Thomas",
            "Dr. Moore"
        ]
    }

    time_slots = [
        "09:00 AM",
        "10:00 AM",
        "11:00 AM",
        "02:00 PM",
        "03:00 PM",
        "04:00 PM"
    ]

    if request.method == "POST":

        department = request.form.get("department")
        doctor = request.form.get("doctor")
        date = request.form.get("date")
        time_slot = request.form.get("time")

        if not all([
            department,
            doctor,
            date,
            time_slot
        ]):

            flash(
                "Please fill all fields!",
                "danger"
            )

            return render_template(
                "doctor_booking.html",
                doctors=doctors,
                time_slots=time_slots
            )

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM appointments
            WHERE doctor_name=?
            AND appointment_date=?
            AND appointment_time=?
            AND status != 'cancelled'
        """, (
            doctor,
            date,
            time_slot
        ))

        existing = cursor.fetchone()

        if existing:

            conn.close()

            flash(
                "This time slot is already booked!",
                "danger"
            )

            return render_template(
                "doctor_booking.html",
                doctors=doctors,
                time_slots=time_slots
            )

        cursor.execute("""
            INSERT INTO appointments
            (
                user_id,
                doctor_name,
                department,
                appointment_date,
                appointment_time,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            session["user_id"],
            doctor,
            department,
            date,
            time_slot,
            "pending"
        ))

        conn.commit()

        appointment_id = cursor.lastrowid

        conn.close()

        flash(
            f"Appointment booked successfully! ID: {appointment_id}",
            "success"
        )

        return redirect(url_for("dashboard"))

    return render_template(
        "doctor_booking.html",
        doctors=doctors,
        time_slots=time_slots
    )


# =========================================================
# BED BOOKING
# =========================================================

@app.route("/book-bed", methods=["GET", "POST"])
@login_required
def book_bed():

    bed_types = [
        "General Ward",
        "Semi-Private",
        "Private Room",
        "ICU",
        "Emergency"
    ]

    if request.method == "POST":

        bed_type = request.form.get("bed_type")
        patient_name = request.form.get("patient_name")
        date = request.form.get("date")

        if not all([
            bed_type,
            patient_name,
            date
        ]):

            flash(
                "Please fill all required fields!",
                "danger"
            )

            return render_template(
                "bed_booking.html",
                bed_types=bed_types
            )

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO appointments
            (
                user_id,
                doctor_name,
                department,
                appointment_date,
                appointment_time,
                status
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            session["user_id"],
            "Bed Service",
            f"Bed: {bed_type}",
            date,
            "Bed Booking",
            "pending"
        ))

        conn.commit()
        conn.close()

        flash(
            f"Bed booked successfully! Type: {bed_type}",
            "success"
        )

        return redirect(url_for("dashboard"))

    return render_template(
        "bed_booking.html",
        bed_types=bed_types
    )


# =========================================================
# AMBULANCE
# =========================================================

@app.route("/book-ambulance", methods=["GET", "POST"])
@login_required
def book_ambulance():

    if request.method == "POST":

        pickup_location = request.form.get("pickup_location")
        patient_name = request.form.get("patient_name")
        contact = request.form.get("contact")
        date = request.form.get("date")
        time = request.form.get("time")

        if not all([
            pickup_location,
            patient_name,
            contact,
            date,
            time
        ]):

            flash(
                "Please fill all required fields!",
                "danger"
            )

            return render_template(
                "ambulance_booking.html"
            )

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO emergencies
            (
                user_id,
                location,
                emergency_type,
                created_at
            )
            VALUES (?, ?, ?, ?)
        """, (
            session["user_id"],
            pickup_location,
            f"Ambulance: {patient_name}",
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ))

        conn.commit()
        conn.close()

        flash(
            "Ambulance booked successfully! Estimated arrival: 10-15 minutes.",
            "success"
        )

        return redirect(url_for("dashboard"))

    return render_template(
        "ambulance_booking.html"
    )


# =========================================================
# MEDICINE
# =========================================================

@app.route("/book-medicine", methods=["GET", "POST"])
@login_required
def book_medicine():

    medicines = {
        "Paracetamol": {
            "price": 25,
            "category": "Pain Relief"
        },
        "Aspirin": {
            "price": 30,
            "category": "Pain Relief"
        },
        "Amoxicillin": {
            "price": 45,
            "category": "Antibiotic"
        },
        "Cetirizine": {
            "price": 35,
            "category": "Antihistamine"
        },
        "Omeprazole": {
            "price": 40,
            "category": "Gastric"
        },
        "Vitamin C": {
            "price": 20,
            "category": "Vitamin"
        },
        "Metformin": {
            "price": 50,
            "category": "Diabetes"
        },
        "Amlodipine": {
            "price": 55,
            "category": "Cardiac"
        }
    }

    if request.method == "POST":

        medicine = request.form.get("medicine")

        try:
            quantity = int(
                request.form.get("quantity", 1)
            )
        except ValueError:
            quantity = 1

        date = request.form.get("date")

        if (
            not medicine
            or medicine not in medicines
            or quantity < 1
            or not date
        ):

            flash(
                "Please fill all required fields!",
                "danger"
            )

            return render_template(
                "medicine_booking.html",
                medicines=medicines
            )

        amount = (
            medicines[medicine]["price"]
            * quantity
        )

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO payments
            (
                user_id,
                appointment_id,
                amount,
                payment_method,
                status,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            session["user_id"],
            0,
            amount,
            "Pharmacy",
            "pending",
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ))

        conn.commit()
        conn.close()

        flash(
            f"Medicine order placed for {medicine} x {quantity}. Total: ₹{amount}",
            "success"
        )

        return redirect(url_for("dashboard"))

    return render_template(
        "medicine_booking.html",
        medicines=medicines
    )


# =========================================================
# BLOOD BOOKING
# =========================================================

@app.route("/book-blood", methods=["GET", "POST"])
@login_required
def book_blood():

    blood_types = [
        "A+",
        "A-",
        "B+",
        "B-",
        "AB+",
        "AB-",
        "O+",
        "O-"
    ]

    blood_banks = [
        "City Blood Bank",
        "Red Cross Center",
        "Hospital Blood Bank",
        "Community Blood Center"
    ]

    if request.method == "POST":

        blood_type = request.form.get("blood_type")

        try:
            units = int(
                request.form.get("units", 1)
            )
        except ValueError:
            units = 1

        hospital = request.form.get("hospital")
        date = request.form.get("date")

        if (
            blood_type not in blood_types
            or units < 1
            or not hospital
            or not date
        ):

            flash(
                "Please fill all required fields!",
                "danger"
            )

            return render_template(
                "blood_booking.html",
                blood_types=blood_types,
                blood_banks=blood_banks
            )

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO emergencies
            (
                user_id,
                location,
                emergency_type,
                created_at
            )
            VALUES (?, ?, ?, ?)
        """, (
            session["user_id"],
            hospital,
            f"Blood Request: {blood_type} x {units} units",
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ))

        conn.commit()
        conn.close()

        flash(
            f"Blood request placed: {blood_type} x {units} units at {hospital}",
            "success"
        )

        return redirect(url_for("dashboard"))

    return render_template(
        "blood_booking.html",
        blood_types=blood_types,
        blood_banks=blood_banks
    )


# =========================================================
# INDOOR NAVIGATION
# =========================================================

@app.route("/navigation", methods=["GET", "POST"])
@login_required
def navigation():

    locations = [
        "Entrance",
        "Reception",
        "Cardiology",
        "Neurology",
        "Pediatrics",
        "Orthopedics",
        "Emergency",
        "Pharmacy",
        "Radiology",
        "Laboratory",
        "Cafeteria"
    ]

    directions = None

    if request.method == "POST":

        start = request.form.get("start")
        end = request.form.get("end")

        directions = get_directions(
            start,
            end
        )

    return render_template(
        "navigation.html",
        locations=locations,
        directions=directions
    )


def get_directions(start, end):

    hospital_map = {

        "Entrance": (0, 0),
        "Reception": (5, 0),
        "Cardiology": (10, 5),
        "Neurology": (10, 10),
        "Pediatrics": (5, 15),
        "Orthopedics": (15, 5),
        "Emergency": (0, 10),
        "Pharmacy": (20, 5),
        "Radiology": (5, 20),
        "Laboratory": (10, 20),
        "Cafeteria": (20, 15)

    }

    if (
        start not in hospital_map
        or end not in hospital_map
    ):
        return "Invalid location selected!"

    start_pos = hospital_map[start]
    end_pos = hospital_map[end]

    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]

    directions = []

    directions.append(
        f"📍 From {start} to {end}"
    )

    directions.append(
        "-" * 40
    )

    if dx > 0:
        directions.append(
            f"→ Walk {dx} meters East"
        )

    elif dx < 0:
        directions.append(
            f"← Walk {abs(dx)} meters West"
        )

    if dy > 0:
        directions.append(
            f"↓ Walk {dy} meters South"
        )

    elif dy < 0:
        directions.append(
            f"↑ Walk {abs(dy)} meters North"
        )

    distance = (
        (dx ** 2) +
        (dy ** 2)
    ) ** 0.5

    directions.append(
        f"\n📏 Total distance: {distance:.1f} meters"
    )

    directions.append(
        f"⏱️ Estimated time: {(distance / 60):.1f} minutes"
    )

    return "\n".join(directions)


# =========================================================
# EMERGENCY
# =========================================================

@app.route("/emergency", methods=["GET", "POST"])
@login_required
def emergency():

    if request.method == "POST":

        emergency_type = request.form.get(
            "emergency_type",
            "Medical Emergency"
        )

        location = request.form.get(
            "location",
            "Hospital"
        )

        conn = get_db()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO emergencies
            (
                user_id,
                location,
                emergency_type,
                created_at
            )
            VALUES (?, ?, ?, ?)
        """, (
            session["user_id"],
            location,
            emergency_type,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ))

        conn.commit()
        conn.close()

        flash(
            "🚨 Emergency team dispatched! Help is on the way.",
            "emergency"
        )

        return redirect(
            url_for("dashboard")
        )

    return render_template(
        "emergency.html"
    )


# =========================================================
# MY APPOINTMENTS
# =========================================================

@app.route("/my-appointments")
@login_required
def my_appointments():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            doctor_name,
            department,
            appointment_date,
            appointment_time,
            status
        FROM appointments
        WHERE user_id=?
        ORDER BY appointment_date DESC
    """, (
        session["user_id"],
    ))

    appointments = cursor.fetchall()

    conn.close()

    return render_template(
        "appointments.html",
        appointments=appointments
    )


# =========================================================
# CANCEL APPOINTMENT
# =========================================================

@app.route(
    "/cancel-appointment/<int:appointment_id>",
    methods=["POST"]
)
@login_required
def cancel_appointment(appointment_id):

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE appointments
        SET status='cancelled'
        WHERE id=?
        AND user_id=?
    """, (
        appointment_id,
        session["user_id"]
    ))

    conn.commit()
    conn.close()

    flash(
        "Appointment cancelled successfully",
        "info"
    )

    return redirect(
        url_for("my_appointments")
    )


# =========================================================
# PAYMENT
# =========================================================

@app.route("/payment", methods=["GET", "POST"])
@login_required
def payment():

    conn = get_db()
    cursor = conn.cursor()

    if request.method == "POST":

        appointment_id = request.form.get(
            "appointment_id"
        )

        try:
            amount = float(
                request.form.get(
                    "amount",
                    500
                )
            )
        except ValueError:
            amount = 500

        method = request.form.get(
            "method",
            "Cash"
        )

        cursor.execute("""
            INSERT INTO payments
            (
                user_id,
                appointment_id,
                amount,
                payment_method,
                status,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            session["user_id"],
            appointment_id,
            amount,
            method,
            "completed",
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ))

        cursor.execute("""
            UPDATE appointments
            SET status='confirmed'
            WHERE id=?
            AND user_id=?
        """, (
            appointment_id,
            session["user_id"]
        ))

        conn.commit()
        conn.close()

        flash(
            "Payment successful! Appointment confirmed.",
            "success"
        )

        return redirect(
            url_for("my_appointments")
        )

    cursor.execute("""
        SELECT
            id,
            doctor_name,
            appointment_date,
            appointment_time
        FROM appointments
        WHERE user_id=?
        AND status='pending'
    """, (
        session["user_id"],
    ))

    pending_apps = cursor.fetchall()

    conn.close()

    return render_template(
        "payment.html",
        pending_apps=pending_apps
    )


# =========================================================
# PAYMENT HISTORY
# =========================================================

@app.route("/payment-history")
@login_required
def payment_history():

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.id,
            p.appointment_id,
            p.amount,
            p.payment_method,
            p.status,
            p.created_at,
            a.doctor_name
        FROM payments p
        LEFT JOIN appointments a
        ON p.appointment_id = a.id
        WHERE p.user_id=?
        ORDER BY p.id DESC
    """, (
        session["user_id"],
    ))

    payments = cursor.fetchall()

    conn.close()

    total = sum(
        payment["amount"]
        for payment in payments
    )

    return render_template(
        "payment_history.html",
        payments=payments,
        total=total
    )


# =========================================================
# AI ASSISTANT
# =========================================================

@app.route(
    "/ai-assistant",
    methods=["GET", "POST"]
)
@login_required
def ai_assistant():

    analysis_result = None

    if request.method == "POST":

        symptoms = request.form.get(
            "symptoms",
            ""
        ).lower()

        advice = []
        departments = set()

        symptom_map = {

            "fever": (
                "🤒 Fever",
                "Rest and stay hydrated. Monitor temperature.",
                "General Medicine"
            ),

            "cough": (
                "🤧 Cough",
                "Use mask, avoid cold drinks, steam inhalation.",
                "General Medicine"
            ),

            "headache": (
                "🤕 Headache",
                "Rest in dark room, stay hydrated.",
                "Neurology"
            ),

            "chest": (
                "⚠️ Chest Pain",
                "SEEK IMMEDIATE MEDICAL ATTENTION!",
                "Cardiology"
            ),

            "back": (
                "💪 Back Pain",
                "Apply ice pack, gentle stretching.",
                "Orthopedics"
            ),

            "cold": (
                "😷 Cold",
                "Steam inhalation, drink warm fluids.",
                "General Medicine"
            ),

            "stomach": (
                "🍽️ Stomach Issue",
                "Avoid spicy food, drink ORS.",
                "Gastroenterology"
            ),

            "vomiting": (
                "🤢 Vomiting",
                "Stay hydrated, eat bland food.",
                "General Medicine"
            )

        }

        for key, value in symptom_map.items():

            title, text, department = value

            if key in symptoms:

                advice.append(
                    f"{title}\n{text}"
                )

                departments.add(
                    department
                )

        if advice:

            analysis_result = {

                "advice": advice,

                "departments": list(
                    departments
                )

            }

        else:

            analysis_result = {

                "advice": [
                    "No specific symptoms detected. Consider a general checkup."
                ],

                "departments": [
                    "General Medicine"
                ]

            }

    return render_template(
        "ai_assistant.html",
        analysis=analysis_result
    )


# =========================================================
# GPS CALCULATOR
# =========================================================

@app.route(
    "/gps-calculator",
    methods=["GET", "POST"]
)
@login_required
def gps_calculator():

    locations = [
        "Downtown",
        "North Side",
        "South Side",
        "East End",
        "West End"
    ]

    result = None

    if request.method == "POST":

        location = request.form.get(
            "location"
        )

        if location:

            distance = round(
                random.uniform(
                    0.5,
                    15.0
                ),
                1
            )

            result = {

                "location": location,

                "distance": distance,

                "driving": int(
                    distance * 2
                ),

                "walking": int(
                    distance * 12
                ),

                "fare": int(
                    distance * 15
                )

            }

    return render_template(
        "gps_calculator.html",
        locations=locations,
        result=result
    )


# =========================================================
# GET DOCTORS API
# =========================================================

@app.route(
    "/get-doctors/<department>"
)
@login_required
def get_doctors(department):

    doctors = {

        "Cardiology": [
            "Dr. Smith",
            "Dr. Johnson",
            "Dr. Williams"
        ],

        "Neurology": [
            "Dr. Brown",
            "Dr. Jones",
            "Dr. Garcia"
        ],

        "Pediatrics": [
            "Dr. Miller",
            "Dr. Davis",
            "Dr. Rodriguez"
        ],

        "Orthopedics": [
            "Dr. Wilson",
            "Dr. Martinez",
            "Dr. Anderson"
        ],

        "General Medicine": [
            "Dr. Taylor",
            "Dr. Thomas",
            "Dr. Moore"
        ]

    }

    return jsonify(
        doctors.get(
            department,
            []
        )
    )


# =========================================================
# INITIALIZE DATABASE FOR VERCEL
# =========================================================

try:
    init_database()
except Exception as error:
    print(
        "Database initialization warning:",
        error
    )


# =========================================================
# LOCAL DEVELOPMENT
# =========================================================

if __name__ == "__main__":

    app.run(
        debug=True,
        port=5001
    )