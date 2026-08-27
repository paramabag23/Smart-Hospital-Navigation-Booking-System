# # # import tkinter as tk
# # # from tkinter import ttk, messagebox, Toplevel
# # # import sqlite3
# # # import hashlib
# # # from datetime import datetime
# # # import os

# # # class HospitalApp:
# # #     def __init__(self, root):
# # #         self.root = root
# # #         self.root.title("LifeLine+ Smart Hospital System")
# # #         self.root.geometry("1200x700")
# # #         self.root.configure(bg='#f0f0f0')
# # #         self.center_window()
# # #         self.init_database()
# # #         self.show_login()
    
# # #     def center_window(self):
# # #         self.root.update_idletasks()
# # #         width = self.root.winfo_width()
# # #         height = self.root.winfo_height()
# # #         x = (self.root.winfo_screenwidth() // 2) - (width // 2)
# # #         y = (self.root.winfo_screenheight() // 2) - (height // 2)
# # #         self.root.geometry(f'{width}x{height}+{x}+{y}')
    
# # #     def init_database(self):
# # #         """Create database with all tables"""
# # #         conn = sqlite3.connect('hospital.db')
# # #         c = conn.cursor()
        
# # #         # Users table
# # #         c.execute('''CREATE TABLE IF NOT EXISTS users (
# # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #             name TEXT NOT NULL,
# # #             email TEXT UNIQUE NOT NULL,
# # #             phone TEXT NOT NULL,
# # #             password TEXT NOT NULL,
# # #             user_type TEXT DEFAULT 'patient'
# # #         )''')
        
# # #         # Appointments table
# # #         c.execute('''CREATE TABLE IF NOT EXISTS appointments (
# # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #             user_id INTEGER NOT NULL,
# # #             doctor_name TEXT NOT NULL,
# # #             department TEXT NOT NULL,
# # #             appointment_date TEXT NOT NULL,
# # #             appointment_time TEXT NOT NULL,
# # #             status TEXT DEFAULT 'pending'
# # #         )''')
        
# # #         # Emergency table
# # #         c.execute('''CREATE TABLE IF NOT EXISTS emergencies (
# # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #             user_id INTEGER NOT NULL,
# # #             location TEXT,
# # #             emergency_type TEXT,
# # #             created_at TEXT
# # #         )''')
        
# # #         # Payments table
# # #         c.execute('''CREATE TABLE IF NOT EXISTS payments (
# # #             id INTEGER PRIMARY KEY AUTOINCREMENT,
# # #             user_id INTEGER NOT NULL,
# # #             appointment_id INTEGER,
# # #             amount REAL NOT NULL,
# # #             payment_method TEXT,
# # #             status TEXT DEFAULT 'pending',
# # #             payment_date TEXT
# # #         )''')
        
# # #         conn.commit()
# # #         conn.close()
        
# # #         if not os.path.exists('uploads'):
# # #             os.makedirs('uploads')
        
# # #         print("Database created successfully!")
    
# # #     def hash_password(self, pwd):
# # #         return hashlib.sha256(pwd.encode()).hexdigest()
    
# # #     def show_login(self):
# # #         for w in self.root.winfo_children():
# # #             w.destroy()
        
# # #         # Header
# # #         header = tk.Frame(self.root, bg='#2c3e50', height=120)
# # #         header.pack(fill='x')
# # #         tk.Label(header, text="🏥 LifeLine+", font=('Arial', 32, 'bold'), 
# # #                 bg='#2c3e50', fg='white').pack(pady=25)
# # #         tk.Label(header, text="Smart Hospital Navigation & Booking System", 
# # #                 font=('Arial', 12), bg='#2c3e50', fg='#bdc3c7').pack()
        
# # #         # Login Frame
# # #         frame = tk.Frame(self.root, bg='white', relief='ridge', bd=2)
# # #         frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=380)
        
# # #         tk.Label(frame, text="🔐 Login to Your Account", font=('Arial', 18, 'bold'), 
# # #                 bg='white', fg='#2c3e50').pack(pady=20)
        
# # #         tk.Label(frame, text="Email:", bg='white', font=('Arial', 11)).pack()
# # #         self.login_email = tk.Entry(frame, width=30, font=('Arial', 11))
# # #         self.login_email.pack(pady=5)
        
# # #         tk.Label(frame, text="Password:", bg='white', font=('Arial', 11)).pack()
# # #         self.login_pass = tk.Entry(frame, width=30, show='*', font=('Arial', 11))
# # #         self.login_pass.pack(pady=5)
        
# # #         tk.Button(frame, text="Login", command=self.do_login,
# # #                  bg='#3498db', fg='white', font=('Arial', 11, 'bold'), 
# # #                  width=20, height=1).pack(pady=10)
        
# # #         tk.Button(frame, text="Create New Account", command=self.show_signup,
# # #                  bg='#27ae60', fg='white', font=('Arial', 11), 
# # #                  width=20, height=1).pack()
    
# # #     def do_login(self):
# # #         email = self.login_email.get()
# # #         pwd = self.login_pass.get()
        
# # #         if not email or not pwd:
# # #             messagebox.showerror("Error", "Please enter email and password!")
# # #             return
        
# # #         conn = sqlite3.connect('hospital.db')
# # #         c = conn.cursor()
# # #         c.execute("SELECT id, name, email, user_type FROM users WHERE email=? AND password=?",
# # #                   (email, self.hash_password(pwd)))
# # #         user = c.fetchone()
# # #         conn.close()
        
# # #         if user:
# # #             self.current_user = user
# # #             messagebox.showinfo("Success", f"Welcome {user[1]}!")
# # #             self.show_dashboard()
# # #         else:
# # #             messagebox.showerror("Error", "Invalid credentials!")
    
# # #     def show_signup(self):
# # #         for w in self.root.winfo_children():
# # #             w.destroy()
        
# # #         header = tk.Frame(self.root, bg='#2c3e50', height=80)
# # #         header.pack(fill='x')
# # #         tk.Label(header, text="📝 Create New Account", font=('Arial', 24, 'bold'), 
# # #                 bg='#2c3e50', fg='white').pack(pady=20)
        
# # #         frame = tk.Frame(self.root, bg='white', relief='ridge', bd=2)
# # #         frame.place(relx=0.5, rely=0.5, anchor='center', width=500, height=550)
        
# # #         tk.Label(frame, text="Registration Form", font=('Arial', 18, 'bold'), 
# # #                 bg='white', fg='#2c3e50').pack(pady=15)
        
# # #         fields = ['Full Name', 'Email', 'Phone', 'Password', 'Confirm Password']
# # #         self.signup_entries = {}
        
# # #         for f in fields:
# # #             tk.Label(frame, text=f+':', bg='white', font=('Arial', 11)).pack()
# # #             e = tk.Entry(frame, width=35, font=('Arial', 11))
# # #             e.pack(pady=3)
# # #             if 'Password' in f:
# # #                 e.config(show='*')
# # #             self.signup_entries[f.lower()] = e
        
# # #         tk.Label(frame, text="User Type:", bg='white', font=('Arial', 11)).pack()
# # #         self.user_type = ttk.Combobox(frame, values=['Patient', 'Doctor'], width=33, font=('Arial', 11))
# # #         self.user_type.set('Patient')
# # #         self.user_type.pack(pady=5)
        
# # #         tk.Button(frame, text="Register", command=self.do_register,
# # #                  bg='#27ae60', fg='white', font=('Arial', 11, 'bold'), 
# # #                  width=20).pack(pady=15)
        
# # #         tk.Button(frame, text="Back to Login", command=self.show_login,
# # #                  bg='#95a5a6', fg='white', font=('Arial', 11), 
# # #                  width=20).pack()
    
# # #     def do_register(self):
# # #         name = self.signup_entries['full name'].get()
# # #         email = self.signup_entries['email'].get()
# # #         phone = self.signup_entries['phone'].get()
# # #         pwd = self.signup_entries['password'].get()
# # #         confirm = self.signup_entries['confirm password'].get()
# # #         utype = self.user_type.get().lower()
        
# # #         if not all([name, email, phone, pwd]):
# # #             messagebox.showerror("Error", "All fields required!")
# # #             return
        
# # #         if pwd != confirm:
# # #             messagebox.showerror("Error", "Passwords don't match!")
# # #             return
        
# # #         if len(pwd) < 6:
# # #             messagebox.showerror("Error", "Password must be at least 6 characters!")
# # #             return
        
# # #         conn = sqlite3.connect('hospital.db')
# # #         c = conn.cursor()
# # #         try:
# # #             c.execute("INSERT INTO users (name, email, phone, password, user_type) VALUES (?,?,?,?,?)",
# # #                       (name, email, phone, self.hash_password(pwd), utype))
# # #             conn.commit()
# # #             messagebox.showinfo("Success", "Registration successful! Please login.")
# # #             self.show_login()
# # #         except sqlite3.IntegrityError:
# # #             messagebox.showerror("Error", "Email already exists!")
# # #         conn.close()
    
# # #     def show_dashboard(self):
# # #         for w in self.root.winfo_children():
# # #             w.destroy()
        
# # #         # Sidebar
# # #         sidebar = tk.Frame(self.root, bg='#2c3e50', width=250)
# # #         sidebar.pack(side='left', fill='y')
        
# # #         tk.Label(sidebar, text=f"👤 {self.current_user[1]}", 
# # #                 font=('Arial', 14, 'bold'), bg='#2c3e50', fg='white').pack(pady=20)
# # #         tk.Label(sidebar, text=f"({self.current_user[3].upper()})", 
# # #                 font=('Arial', 10), bg='#2c3e50', fg='#bdc3c7').pack()
        
# # #         tk.Frame(sidebar, bg='#34495e', height=2).pack(fill='x', pady=20)
        
# # #         menus = [
# # #             ("🏠 Dashboard", self.show_welcome),
# # #             ("📅 Book Appointment", self.book_appointment),
# # #             ("📋 My Appointments", self.view_appointments),
# # #             ("🗺️ Indoor Navigation", self.show_navigation),
# # #             ("🚨 Emergency", self.emergency),
# # #             ("💰 Make Payment", self.show_payments),
# # #             ("📜 Payment History", self.payment_history),
# # #             ("🤖 AI Assistant", self.ai_assistant),
# # #             ("📍 GPS Distance", self.gps_calculator),
# # #             ("🚪 Logout", self.show_login)
# # #         ]
        
# # #         for text, cmd in menus:
# # #             btn = tk.Button(sidebar, text=text, command=cmd,
# # #                            bg='#2c3e50', fg='white', relief='flat',
# # #                            anchor='w', padx=20, pady=10, font=('Arial', 11))
# # #             btn.pack(fill='x')
        
# # #         self.main = tk.Frame(self.root, bg='#f0f0f0')
# # #         self.main.pack(side='left', expand=True, fill='both', padx=20, pady=20)
# # #         self.show_welcome()
    
# # #     def show_welcome(self):
# # #         self.clear_main()
        
# # #         welcome_frame = tk.Frame(self.main, bg='#f0f0f0')
# # #         welcome_frame.pack(expand=True)
        
# # #         tk.Label(welcome_frame, text=f"Welcome to LifeLine+, {self.current_user[1]}!", 
# # #                 font=('Arial', 28, 'bold'), bg='#f0f0f0', fg='#2c3e50').pack(pady=30)
        
# # #         tk.Label(welcome_frame, text="Your One-Stop Smart Hospital Management System", 
# # #                 font=('Arial', 14), bg='#f0f0f0', fg='#7f8c8d').pack()
        
# # #         # Stats
# # #         stats_frame = tk.Frame(welcome_frame, bg='#f0f0f0')
# # #         stats_frame.pack(pady=50)
        
# # #         conn = sqlite3.connect('hospital.db')
# # #         c = conn.cursor()
# # #         c.execute("SELECT COUNT(*) FROM appointments WHERE user_id=?", (self.current_user[0],))
# # #         appointments = c.fetchone()[0]
# # #         conn.close()
        
# # #         stats = [
# # #             ("📅 Appointments", appointments),
# # #             ("🏥 Departments", 5),
# # #             ("👨‍⚕️ Doctors", 12),
# # #             ("⭐ Rating", "4.8/5")
# # #         ]
        
# # #         for i, (label, value) in enumerate(stats):
# # #             frame = tk.Frame(stats_frame, bg='white', relief='ridge', bd=2)
# # #             frame.grid(row=0, column=i, padx=15, pady=10, ipadx=25, ipady=20)
# # #             tk.Label(frame, text=str(value), font=('Arial', 24, 'bold'), 
# # #                     bg='white', fg='#3498db').pack()
# # #             tk.Label(frame, text=label, font=('Arial', 12), 
# # #                     bg='white', fg='#7f8c8d').pack()
    
# # #     def book_appointment(self):
# # #         self.clear_main()
        
# # #         tk.Label(self.main, text="📅 Book Appointment", font=('Arial', 24, 'bold'),
# # #                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
# # #         # Create form frame
# # #         form_frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
# # #         form_frame.pack(pady=30, padx=50, ipadx=40, ipady=40)
        
# # #         doctors = {
# # #             'Cardiology': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams'],
# # #             'Neurology': ['Dr. Brown', 'Dr. Jones', 'Dr. Garcia'],
# # #             'Pediatrics': ['Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez'],
# # #             'Orthopedics': ['Dr. Wilson', 'Dr. Martinez', 'Dr. Anderson'],
# # #             'General Medicine': ['Dr. Taylor', 'Dr. Thomas', 'Dr. Moore']
# # #         }
        
# # #         time_slots = ['09:00 AM', '10:00 AM', '11:00 AM', '02:00 PM', '03:00 PM', '04:00 PM']
        
# # #         # Variables
# # #         dept_var = tk.StringVar()
# # #         doctor_var = tk.StringVar()
# # #         date_var = tk.StringVar(value=datetime.now().strftime('%Y-%m-%d'))
# # #         time_var = tk.StringVar()
        
# # #         # Department
# # #         tk.Label(form_frame, text="Select Department:", font=('Arial', 12, 'bold')).grid(row=0, column=0, pady=10, padx=10, sticky='w')
# # #         dept_combo = ttk.Combobox(form_frame, textvariable=dept_var, values=list(doctors.keys()), width=35, font=('Arial', 11))
# # #         dept_combo.grid(row=0, column=1, pady=10, padx=10)
        
# # #         # Doctor
# # #         tk.Label(form_frame, text="Select Doctor:", font=('Arial', 12, 'bold')).grid(row=1, column=0, pady=10, padx=10, sticky='w')
# # #         doctor_combo = ttk.Combobox(form_frame, textvariable=doctor_var, width=35, font=('Arial', 11))
# # #         doctor_combo.grid(row=1, column=1, pady=10, padx=10)
        
# # #         def update_doctors(*args):
# # #             dept = dept_var.get()
# # #             if dept in doctors:
# # #                 doctor_combo['values'] = doctors[dept]
# # #         dept_var.trace('w', update_doctors)
        
# # #         # Date
# # #         tk.Label(form_frame, text="Date (YYYY-MM-DD):", font=('Arial', 12, 'bold')).grid(row=2, column=0, pady=10, padx=10, sticky='w')
# # #         date_entry = tk.Entry(form_frame, textvariable=date_var, width=38, font=('Arial', 11))
# # #         date_entry.grid(row=2, column=1, pady=10, padx=10)
        
# # #         # Time
# # #         tk.Label(form_frame, text="Select Time:", font=('Arial', 12, 'bold')).grid(row=3, column=0, pady=10, padx=10, sticky='w')
# # #         time_combo = ttk.Combobox(form_frame, textvariable=time_var, values=time_slots, width=35, font=('Arial', 11))
# # #         time_combo.grid(row=3, column=1, pady=10, padx=10)
        
# # #         def save_booking():
# # #             dept = dept_var.get()
# # #             doctor = doctor_var.get()
# # #             date = date_var.get()
# # #             time_slot = time_var.get()
            
# # #             if not dept:
# # #                 messagebox.showerror("Error", "Please select a department!")
# # #                 return
# # #             if not doctor:
# # #                 messagebox.showerror("Error", "Please select a doctor!")
# # #                 return
# # #             if not date:
# # #                 messagebox.showerror("Error", "Please enter date!")
# # #                 return
# # #             if not time_slot:
# # #                 messagebox.showerror("Error", "Please select time!")
# # #                 return
            
# # #             # Save to database
# # #             conn = sqlite3.connect('hospital.db')
# # #             c = conn.cursor()
            
# # #             # Check if slot is available
# # #             c.execute("SELECT * FROM appointments WHERE doctor_name=? AND appointment_date=? AND appointment_time=? AND status != 'cancelled'",
# # #                      (doctor, date, time_slot))
# # #             existing = c.fetchone()
            
# # #             if existing:
# # #                 messagebox.showerror("Error", "This time slot is already booked!\nPlease choose another time.")
# # #                 conn.close()
# # #                 return
            
# # #             # Insert appointment
# # #             c.execute("INSERT INTO appointments (user_id, doctor_name, department, appointment_date, appointment_time, status) VALUES (?,?,?,?,?,?)",
# # #                      (self.current_user[0], doctor, dept, date, time_slot, 'pending'))
# # #             conn.commit()
# # #             app_id = c.lastrowid
# # #             conn.close()
            
# # #             messagebox.showinfo("Success", f"✅ Appointment Booked Successfully!\n\nBooking ID: {app_id}\nDoctor: {doctor}\nDate: {date}\nTime: {time_slot}\n\nPlease make payment to confirm.")
            
# # #             # Clear form
# # #             dept_var.set('')
# # #             doctor_var.set('')
# # #             time_var.set('')
            
# # #             # Ask for payment
# # #             if messagebox.askyesno("Payment", "Would you like to make payment now?"):
# # #                 self.show_payments()
        
# # #         tk.Button(form_frame, text="Book Appointment", command=save_booking,
# # #                  bg='#27ae60', fg='white', font=('Arial', 12, 'bold'), 
# # #                  width=25, height=1).grid(row=4, column=0, columnspan=2, pady=20)
    
# # #     def view_appointments(self):
# # #         self.clear_main()
        
# # #         tk.Label(self.main, text="📋 My Appointments", font=('Arial', 24, 'bold'),
# # #                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
# # #         # Get appointments from database
# # #         conn = sqlite3.connect('hospital.db')
# # #         c = conn.cursor()
# # #         c.execute("SELECT id, doctor_name, department, appointment_date, appointment_time, status FROM appointments WHERE user_id=? ORDER BY id DESC", 
# # #                   (self.current_user[0],))
# # #         appointments = c.fetchall()
# # #         conn.close()
        
# # #         if not appointments:
# # #             tk.Label(self.main, text="No appointments found!", font=('Arial', 14),
# # #                     bg='#f0f0f0', fg='#e74c3c').pack(pady=50)
# # #             return
        
# # #         # Create treeview
# # #         tree_frame = tk.Frame(self.main, bg='#f0f0f0')
# # #         tree_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
# # #         scrollbar = ttk.Scrollbar(tree_frame, orient='vertical')
# # #         scrollbar.pack(side='right', fill='y')
        
# # #         columns = ('ID', 'Doctor', 'Department', 'Date', 'Time', 'Status')
# # #         tree = ttk.Treeview(tree_frame, columns=columns, show='headings', yscrollcommand=scrollbar.set)
# # #         scrollbar.config(command=tree.yview)
        
# # #         for col in columns:
# # #             tree.heading(col, text=col)
# # #             tree.column(col, width=150)
        
# # #         for app in appointments:
# # #             tree.insert('', 'end', values=app)
        
# # #         tree.pack(fill='both', expand=True)
        
# # #         # Cancel appointment section
# # #         cancel_frame = tk.Frame(self.main, bg='#f0f0f0')
# # #         cancel_frame.pack(pady=20)
        
# # #         tk.Label(cancel_frame, text="Enter Appointment ID to Cancel:", font=('Arial', 11)).pack(side='left', padx=10)
# # #         cancel_id = tk.Entry(cancel_frame, width=15, font=('Arial', 11))
# # #         cancel_id.pack(side='left', padx=10)
        
# # #         def cancel_booking():
# # #             app_id = cancel_id.get()
# # #             if not app_id:
# # #                 messagebox.showerror("Error", "Please enter appointment ID!")
# # #                 return
            
# # #             conn = sqlite3.connect('hospital.db')
# # #             c = conn.cursor()
# # #             c.execute("UPDATE appointments SET status='cancelled' WHERE id=? AND user_id=?", (app_id, self.current_user[0]))
# # #             conn.commit()
# # #             conn.close()
            
# # #             messagebox.showinfo("Success", f"Appointment #{app_id} cancelled successfully!")
# # #             cancel_id.delete(0, tk.END)
# # #             self.view_appointments()
        
# # #         tk.Button(cancel_frame, text="Cancel Appointment", command=cancel_booking,
# # #                  bg='#e74c3c', fg='white', font=('Arial', 11), width=20).pack(side='left', padx=10)
    
# # #     def show_payments(self):
# # #         self.clear_main()
        
# # #         tk.Label(self.main, text="💰 Make Payment", font=('Arial', 24, 'bold'),
# # #                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
# # #         # Get pending appointments
# # #         conn = sqlite3.connect('hospital.db')
# # #         c = conn.cursor()
# # #         c.execute("SELECT id, doctor_name, department, appointment_date, appointment_time FROM appointments WHERE user_id=? AND status='pending'",
# # #                   (self.current_user[0],))
# # #         pending_apps = c.fetchall()
# # #         conn.close()
        
# # #         if not pending_apps:
# # #             tk.Label(self.main, text="No pending appointments for payment!", 
# # #                     font=('Arial', 14), bg='#f0f0f0', fg='#e74c3c').pack(pady=50)
# # #             tk.Button(self.main, text="Book an Appointment", command=self.book_appointment,
# # #                      bg='#3498db', fg='white', font=('Arial', 12), width=20).pack(pady=20)
# # #             return
        
# # #         # Payment form
# # #         payment_frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
# # #         payment_frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
# # #         tk.Label(payment_frame, text="Select Appointment:", font=('Arial', 12, 'bold')).grid(row=0, column=0, pady=10, padx=10, sticky='w')
        
# # #         app_list = [f"ID:{app[0]} - {app[1]} - {app[3]} {app[4]}" for app in pending_apps]
# # #         app_var = tk.StringVar()
# # #         app_combo = ttk.Combobox(payment_frame, textvariable=app_var, values=app_list, width=40, font=('Arial', 11))
# # #         app_combo.grid(row=0, column=1, pady=10, padx=10)
        
# # #         tk.Label(payment_frame, text="Amount (₹):", font=('Arial', 12, 'bold')).grid(row=1, column=0, pady=10, padx=10, sticky='w')
# # #         amount_entry = tk.Entry(payment_frame, width=20, font=('Arial', 11))
# # #         amount_entry.insert(0, "500")
# # #         amount_entry.grid(row=1, column=1, pady=10, padx=10, sticky='w')
        
# # #         tk.Label(payment_frame, text="Payment Method:", font=('Arial', 12, 'bold')).grid(row=2, column=0, pady=10, padx=10, sticky='w')
# # #         method_var = tk.StringVar(value='UPI')
# # #         method_combo = ttk.Combobox(payment_frame, textvariable=method_var, 
# # #                                    values=['Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'Cash'], 
# # #                                    width=28, font=('Arial', 11))
# # #         method_combo.grid(row=2, column=1, pady=10, padx=10, sticky='w')
        
# # #         def process_payment():
# # #             if not app_var.get():
# # #                 messagebox.showerror("Error", "Please select an appointment!")
# # #                 return
            
# # #             # Extract appointment ID
# # #             app_id = app_var.get().split('-')[0].replace('ID:', '').strip()
# # #             amount = float(amount_entry.get())
# # #             method = method_var.get()
            
# # #             # Save payment
# # #             conn = sqlite3.connect('hospital.db')
# # #             c = conn.cursor()
# # #             c.execute("INSERT INTO payments (user_id, appointment_id, amount, payment_method, status, payment_date) VALUES (?,?,?,?,?,?)",
# # #                      (self.current_user[0], app_id, amount, method, 'completed', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
# # #             c.execute("UPDATE appointments SET status='confirmed' WHERE id=?", (app_id,))
# # #             conn.commit()
# # #             conn.close()
            
# # #             trans_id = f"TXN{datetime.now().strftime('%Y%m%d%H%M%S')}"
# # #             messagebox.showinfo("Success", f"✅ Payment Successful!\n\nAmount: ₹{amount}\nMethod: {method}\nTransaction ID: {trans_id}\n\nYour appointment is confirmed!")
            
# # #             self.show_payments()
        
# # #         tk.Button(payment_frame, text="Pay Now", command=process_payment,
# # #                  bg='#27ae60', fg='white', font=('Arial', 12, 'bold'), 
# # #                  width=20).grid(row=3, column=0, columnspan=2, pady=20)
    
# # #     def payment_history(self):
# # #         self.clear_main()
        
# # #         tk.Label(self.main, text="📜 Payment History", font=('Arial', 24, 'bold'),
# # #                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
# # #         conn = sqlite3.connect('hospital.db')
# # #         c = conn.cursor()
# # #         c.execute("SELECT id, appointment_id, amount, payment_method, status, payment_date FROM payments WHERE user_id=? ORDER BY id DESC",
# # #                   (self.current_user[0],))
# # #         payments = c.fetchall()
# # #         conn.close()
        
# # #         if not payments:
# # #             tk.Label(self.main, text="No payment records found!", font=('Arial', 14),
# # #                     bg='#f0f0f0', fg='#7f8c8d').pack(pady=50)
# # #             return
        
# # #         tree_frame = tk.Frame(self.main, bg='#f0f0f0')
# # #         tree_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
# # #         scrollbar = ttk.Scrollbar(tree_frame, orient='vertical')
# # #         scrollbar.pack(side='right', fill='y')
        
# # #         columns = ('ID', 'Appointment ID', 'Amount (₹)', 'Method', 'Status', 'Date')
# # #         tree = ttk.Treeview(tree_frame, columns=columns, show='headings', yscrollcommand=scrollbar.set)
# # #         scrollbar.config(command=tree.yview)
        
# # #         for col in columns:
# # #             tree.heading(col, text=col)
# # #             tree.column(col, width=150)
        
# # #         total = 0
# # #         for payment in payments:
# # #             tree.insert('', 'end', values=payment)
# # #             total += payment[2]
        
# # #         tree.pack(fill='both', expand=True)
        
# # #         total_frame = tk.Frame(self.main, bg='#f0f0f0')
# # #         total_frame.pack(pady=20)
# # #         tk.Label(total_frame, text=f"Total Amount Paid: ₹{total}", 
# # #                 font=('Arial', 14, 'bold'), bg='#f0f0f0', fg='#27ae60').pack()
    
# # #     def show_navigation(self):
# # #         self.clear_main()
        
# # #         tk.Label(self.main, text="🗺️ Indoor Navigation", font=('Arial', 24, 'bold'),
# # #                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
# # #         locations = ['Entrance', 'Reception', 'Cardiology', 'Neurology', 'Emergency', 'Pharmacy']
        
# # #         frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
# # #         frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
# # #         tk.Label(frame, text="Current Location:", font=('Arial', 12)).grid(row=0, column=0, pady=10, padx=10)
# # #         start = ttk.Combobox(frame, values=locations, width=30, font=('Arial', 11))
# # #         start.grid(row=0, column=1, pady=10, padx=10)
        
# # #         tk.Label(frame, text="Destination:", font=('Arial', 12)).grid(row=1, column=0, pady=10, padx=10)
# # #         end = ttk.Combobox(frame, values=locations, width=30, font=('Arial', 11))
# # #         end.grid(row=1, column=1, pady=10, padx=10)
        
# # #         directions = tk.Text(frame, height=8, width=50, font=('Arial', 10))
# # #         directions.grid(row=2, column=0, columnspan=2, pady=20, padx=10)
        
# # #         def get_directions():
# # #             s = start.get()
# # #             e = end.get()
# # #             if s and e:
# # #                 directions.delete(1.0, tk.END)
# # #                 directions.insert(1.0, f"📍 From {s} to {e}\n\n→ Walk straight to main corridor\n→ Take elevator to appropriate floor\n→ Follow signs\n→ You have reached {e}\n\n⏱️ Estimated time: 5-10 minutes")
        
# # #         tk.Button(frame, text="Get Directions", command=get_directions,
# # #                  bg='#3498db', fg='white', font=('Arial', 12), width=20).grid(row=3, column=0, columnspan=2, pady=10)
    
# # #     def emergency(self):
# # #         self.clear_main()
        
# # #         frame = tk.Frame(self.main, bg='#ff4444', relief='ridge', bd=3)
# # #         frame.pack(expand=True, fill='both', padx=50, pady=50)
        
# # #         tk.Label(frame, text="🚨 EMERGENCY MODE 🚨", font=('Arial', 28, 'bold'), 
# # #                 bg='#ff4444', fg='white').pack(pady=30)
        
# # #         tk.Label(frame, text="⚠️ This is for real emergencies only!", 
# # #                 font=('Arial', 14), bg='#ff4444', fg='yellow').pack()
        
# # #         def activate():
# # #             conn = sqlite3.connect('hospital.db')
# # #             c = conn.cursor()
# # #             c.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
# # #                      (self.current_user[0], "Hospital", "Medical Emergency", datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
# # #             conn.commit()
# # #             conn.close()
            
# # #             msg = Toplevel(self.root)
# # #             msg.title("Emergency Response")
# # #             msg.geometry("400x300")
# # #             msg.configure(bg='#ff4444')
# # #             tk.Label(msg, text="🚑 EMERGENCY TEAM DISPATCHED!", font=('Arial', 16, 'bold'), 
# # #                     bg='#ff4444', fg='white').pack(pady=30)
# # #             tk.Label(msg, text=f"Patient: {self.current_user[1]}", font=('Arial', 12), 
# # #                     bg='#ff4444', fg='white').pack()
# # #             tk.Label(msg, text="⏱️ Estimated arrival: 5 minutes", font=('Arial', 12), 
# # #                     bg='#ff4444', fg='yellow').pack(pady=20)
# # #             tk.Button(msg, text="OK", command=msg.destroy, bg='white', fg='black').pack(pady=20)
        
# # #         tk.Button(frame, text="🚑 ACTIVATE EMERGENCY 🚑", command=activate,
# # #                  font=('Arial', 18, 'bold'), bg='#cc0000', fg='white', 
# # #                  width=30, height=2).pack(pady=30)
    
# # #     def ai_assistant(self):
# # #         self.clear_main()
        
# # #         tk.Label(self.main, text="🤖 AI Health Assistant", font=('Arial', 24, 'bold'),
# # #                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
# # #         frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
# # #         frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
# # #         tk.Label(frame, text="Describe your symptoms:", font=('Arial', 12)).pack()
# # #         symptoms = tk.Text(frame, height=5, width=50, font=('Arial', 11))
# # #         symptoms.pack(pady=10)
        
# # #         result = tk.Text(frame, height=8, width=50, font=('Arial', 11), bg='#f0f0f0')
# # #         result.pack(pady=10)
        
# # #         def analyze():
# # #             text = symptoms.get(1.0, tk.END).lower()
# # #             result.delete(1.0, tk.END)
            
# # #             advice = ""
# # #             if 'fever' in text:
# # #                 advice += "• Fever: Rest and stay hydrated\n"
# # #             if 'cough' in text:
# # #                 advice += "• Cough: Use mask, avoid cold\n"
# # #             if 'headache' in text:
# # #                 advice += "• Headache: Rest in dark room\n"
# # #             if 'chest' in text:
# # #                 advice += "⚠️ Chest pain: Seek immediate medical attention!\n"
            
# # #             if advice:
# # #                 result.insert(1.0, f"Analysis:\n{advice}\n\nRecommended: Book a doctor's appointment")
# # #             else:
# # #                 result.insert(1.0, "No specific symptoms detected. Consider a general checkup.")
        
# # #         tk.Button(frame, text="Analyze", command=analyze,
# # #                  bg='#9b59b6', fg='white', font=('Arial', 12), width=20).pack()
    
# # #     def gps_calculator(self):
# # #         self.clear_main()
        
# # #         tk.Label(self.main, text="📍 GPS Distance Calculator", font=('Arial', 24, 'bold'),
# # #                 bg='#f0f0f0', fg='#2c3e50').pack(pady=20)
        
# # #         frame = tk.Frame(self.main, bg='white', relief='ridge', bd=2)
# # #         frame.pack(pady=30, padx=50, ipadx=30, ipady=30)
        
# # #         locations = ['Downtown', 'North Side', 'South Side', 'East End', 'West End']
        
# # #         tk.Label(frame, text="Select your location:", font=('Arial', 12)).pack()
# # #         location = ttk.Combobox(frame, values=locations, width=30, font=('Arial', 11))
# # #         location.pack(pady=10)
        
# # #         result = tk.Text(frame, height=8, width=50, font=('Arial', 11), bg='#f0f0f0')
# # #         result.pack(pady=10)
        
# # #         def calculate():
# # #             loc = location.get()
# # #             if loc:
# # #                 import random
# # #                 dist = random.uniform(1, 15)
# # #                 result.delete(1.0, tk.END)
# # #                 result.insert(1.0, f"📍 From {loc} to Hospital\n\n📏 Distance: {dist:.1f} km\n🚗 Driving: {dist*2:.0f} minutes\n🚶 Walking: {dist*12:.0f} minutes\n💰 Estimated fare: ₹{dist*15:.0f}")
        
# # #         tk.Button(frame, text="Calculate", command=calculate,
# # #                  bg='#3498db', fg='white', font=('Arial', 12), width=20).pack()
    
# # #     def clear_main(self):
# # #         for widget in self.main.winfo_children():
# # #             widget.destroy()

# # # if __name__ == "__main__":
# # #     root = tk.Tk()
# # #     app = HospitalApp(root)
# # #     root.mainloop()










# # from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
# # from datetime import datetime
# # import sqlite3
# # import hashlib
# # import os
# # import random
# # from functools import wraps

# # app = Flask(__name__)
# # app.secret_key = 'your-secret-key-here-change-in-production'

# # # Database helper functions
# # def get_db():
# #     conn = sqlite3.connect('hospital.db')
# #     conn.row_factory = sqlite3.Row
# #     return conn

# # def hash_password(password):
# #     return hashlib.sha256(password.encode()).hexdigest()

# # # Login decorator
# # def login_required(f):
# #     @wraps(f)
# #     def decorated_function(*args, **kwargs):
# #         if 'user_id' not in session:
# #             flash('Please login to access this page', 'warning')
# #             return redirect(url_for('login'))
# #         return f(*args, **kwargs)
# #     return decorated_function

# # # Routes
# # @app.route('/')
# # def index():
# #     return redirect(url_for('login'))

# # @app.route('/login', methods=['GET', 'POST'])
# # def login():
# #     if request.method == 'POST':
# #         email = request.form.get('email')
# #         password = request.form.get('password')
        
# #         if not email or not password:
# #             flash('Please enter email and password', 'danger')
# #             return render_template('login.html')
        
# #         conn = get_db()
# #         cursor = conn.cursor()
# #         cursor.execute("SELECT id, name, email, user_type FROM users WHERE email=? AND password=?", 
# #                       (email, hash_password(password)))
# #         user = cursor.fetchone()
# #         conn.close()
        
# #         if user:
# #             session['user_id'] = user['id']
# #             session['user_name'] = user['name']
# #             session['user_type'] = user['user_type']
# #             flash(f'Welcome back, {user["name"]}!', 'success')
# #             return redirect(url_for('dashboard'))
# #         else:
# #             flash('Invalid email or password!', 'danger')
    
# #     return render_template('login.html')

# # @app.route('/signup', methods=['GET', 'POST'])
# # def signup():
# #     if request.method == 'POST':
# #         name = request.form.get('name')
# #         email = request.form.get('email')
# #         phone = request.form.get('phone')
# #         password = request.form.get('password')
# #         confirm_password = request.form.get('confirm_password')
# #         user_type = request.form.get('user_type', 'patient')
        
# #         if not all([name, email, phone, password]):
# #             flash('All fields are required!', 'danger')
# #             return render_template('login.html')
        
# #         if password != confirm_password:
# #             flash('Passwords do not match!', 'danger')
# #             return render_template('login.html')
        
# #         if len(password) < 6:
# #             flash('Password must be at least 6 characters!', 'danger')
# #             return render_template('login.html')
        
# #         conn = get_db()
# #         cursor = conn.cursor()
        
# #         try:
# #             cursor.execute("INSERT INTO users (name, email, phone, password, user_type) VALUES (?,?,?,?,?)",
# #                           (name, email, phone, hash_password(password), user_type))
# #             conn.commit()
# #             flash('Registration successful! Please login.', 'success')
# #             return redirect(url_for('login'))
# #         except sqlite3.IntegrityError:
# #             flash('Email already registered!', 'danger')
# #         finally:
# #             conn.close()
    
# #     return render_template('login.html')

# # @app.route('/logout')
# # def logout():
# #     session.clear()
# #     flash('Logged out successfully', 'info')
# #     return redirect(url_for('login'))

# # @app.route('/dashboard')
# # @login_required
# # def dashboard():
# #     conn = get_db()
# #     cursor = conn.cursor()
    
# #     # Get appointment count
# #     cursor.execute("SELECT COUNT(*) FROM appointments WHERE user_id=?", (session['user_id'],))
# #     appointment_count = cursor.fetchone()[0]
    
# #     # Get recent appointments
# #     cursor.execute("SELECT id, doctor_name, department, appointment_date, appointment_time, status FROM appointments WHERE user_id=? ORDER BY id DESC LIMIT 5",
# #                   (session['user_id'],))
# #     recent_appointments = cursor.fetchall()
    
# #     conn.close()
    
# #     return render_template('dashboard.html', 
# #                          user_name=session.get('user_name'),
# #                          user_type=session.get('user_type'),
# #                          appointment_count=appointment_count,
# #                          recent_appointments=recent_appointments)

# # @app.route('/book-doctor', methods=['GET', 'POST'])
# # @login_required
# # def book_doctor():
# #     doctors = {
# #         'Cardiology': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams'],
# #         'Neurology': ['Dr. Brown', 'Dr. Jones', 'Dr. Garcia'],
# #         'Pediatrics': ['Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez'],
# #         'Orthopedics': ['Dr. Wilson', 'Dr. Martinez', 'Dr. Anderson'],
# #         'General Medicine': ['Dr. Taylor', 'Dr. Thomas', 'Dr. Moore']
# #     }
# #     time_slots = ['09:00 AM', '10:00 AM', '11:00 AM', '02:00 PM', '03:00 PM', '04:00 PM']
    
# #     if request.method == 'POST':
# #         department = request.form.get('department')
# #         doctor = request.form.get('doctor')
# #         date = request.form.get('date')
# #         time_slot = request.form.get('time')
        
# #         if not all([department, doctor, date, time_slot]):
# #             flash('Please fill all fields!', 'danger')
# #             return render_template('doctor_booking.html', doctors=doctors, time_slots=time_slots)
        
# #         conn = get_db()
# #         cursor = conn.cursor()
        
# #         # Check if slot is available
# #         cursor.execute("SELECT * FROM appointments WHERE doctor_name=? AND appointment_date=? AND appointment_time=? AND status != 'cancelled'",
# #                       (doctor, date, time_slot))
# #         existing = cursor.fetchone()
        
# #         if existing:
# #             flash('This time slot is already booked! Please choose another time.', 'danger')
# #             conn.close()
# #             return render_template('doctor_booking.html', doctors=doctors, time_slots=time_slots)
        
# #         # Book appointment
# #         cursor.execute("INSERT INTO appointments (user_id, doctor_name, department, appointment_date, appointment_time, status) VALUES (?,?,?,?,?,?)",
# #                       (session['user_id'], doctor, department, date, time_slot, 'pending'))
# #         conn.commit()
# #         app_id = cursor.lastrowid
# #         conn.close()
        
# #         flash(f'Appointment booked successfully! ID: {app_id}', 'success')
# #         return redirect(url_for('dashboard'))
    
# #     return render_template('doctor_booking.html', doctors=doctors, time_slots=time_slots)

# # @app.route('/book-bed', methods=['GET', 'POST'])
# # @login_required
# # def book_bed():
# #     bed_types = ['General Ward', 'Semi-Private', 'Private Room', 'ICU', 'Emergency']
    
# #     if request.method == 'POST':
# #         bed_type = request.form.get('bed_type')
# #         patient_name = request.form.get('patient_name')
# #         date = request.form.get('date')
# #         notes = request.form.get('notes')
        
# #         if not all([bed_type, patient_name, date]):
# #             flash('Please fill all required fields!', 'danger')
# #             return render_template('bed_booking.html', bed_types=bed_types)
        
# #         # Create a bed booking record (using appointments table with special format)
# #         conn = get_db()
# #         cursor = conn.cursor()
        
# #         cursor.execute("INSERT INTO appointments (user_id, doctor_name, department, appointment_date, appointment_time, status) VALUES (?,?,?,?,?,?)",
# #                       (session['user_id'], 'Bed Service', f'Bed: {bed_type}', date, 'Bed Booking', 'pending'))
# #         conn.commit()
# #         conn.close()
        
# #         flash(f'Bed booked successfully! Type: {bed_type}', 'success')
# #         return redirect(url_for('dashboard'))
    
# #     return render_template('bed_booking.html', bed_types=bed_types)

# # @app.route('/book-ambulance', methods=['GET', 'POST'])
# # @login_required
# # def book_ambulance():
# #     if request.method == 'POST':
# #         pickup_location = request.form.get('pickup_location')
# #         patient_name = request.form.get('patient_name')
# #         contact = request.form.get('contact')
# #         date = request.form.get('date')
# #         time = request.form.get('time')
# #         notes = request.form.get('notes')
        
# #         if not all([pickup_location, patient_name, contact, date, time]):
# #             flash('Please fill all required fields!', 'danger')
# #             return render_template('ambulance_booking.html')
        
# #         # Save ambulance booking
# #         conn = get_db()
# #         cursor = conn.cursor()
# #         cursor.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
# #                       (session['user_id'], pickup_location, f'Ambulance: {patient_name}', 
# #                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
# #         conn.commit()
# #         conn.close()
        
# #         flash('Ambulance booked successfully! Estimated arrival: 10-15 minutes.', 'success')
# #         return redirect(url_for('dashboard'))
    
# #     return render_template('ambulance_booking.html')

# # @app.route('/book-medicine', methods=['GET', 'POST'])
# # @login_required
# # def book_medicine():
# #     medicines = {
# #         'Paracetamol': {'price': 25, 'category': 'Pain Relief'},
# #         'Aspirin': {'price': 30, 'category': 'Pain Relief'},
# #         'Amoxicillin': {'price': 45, 'category': 'Antibiotic'},
# #         'Cetirizine': {'price': 35, 'category': 'Antihistamine'},
# #         'Omeprazole': {'price': 40, 'category': 'Gastric'},
# #         'Vitamin C': {'price': 20, 'category': 'Vitamin'},
# #         'Metformin': {'price': 50, 'category': 'Diabetes'},
# #         'Amlodipine': {'price': 55, 'category': 'Cardiac'}
# #     }
    
# #     if request.method == 'POST':
# #         medicine = request.form.get('medicine')
# #         quantity = int(request.form.get('quantity', 1))
# #         date = request.form.get('date')
        
# #         if not all([medicine, quantity, date]):
# #             flash('Please fill all required fields!', 'danger')
# #             return render_template('medicine_booking.html', medicines=medicines)
        
# #         # Save medicine order
# #         conn = get_db()
# #         cursor = conn.cursor()
# #         amount = medicines[medicine]['price'] * quantity
        
# #         cursor.execute("INSERT INTO payments (user_id, appointment_id, amount, payment_method, status, created_at) VALUES (?,?,?,?,?,?)",
# #                       (session['user_id'], 0, amount, 'Pharmacy', 'pending',
# #                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
# #         conn.commit()
# #         conn.close()
        
# #         flash(f'Medicine order placed for {medicine} x {quantity}. Total: ₹{amount}', 'success')
# #         return redirect(url_for('dashboard'))
    
# #     return render_template('medicine_booking.html', medicines=medicines)

# # @app.route('/book-blood', methods=['GET', 'POST'])
# # @login_required
# # def book_blood():
# #     blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
# #     blood_banks = ['City Blood Bank', 'Red Cross Center', 'Hospital Blood Bank', 'Community Blood Center']
    
# #     if request.method == 'POST':
# #         blood_type = request.form.get('blood_type')
# #         units = int(request.form.get('units', 1))
# #         hospital = request.form.get('hospital')
# #         date = request.form.get('date')
# #         notes = request.form.get('notes')
        
# #         if not all([blood_type, units, hospital, date]):
# #             flash('Please fill all required fields!', 'danger')
# #             return render_template('blood_booking.html', blood_types=blood_types, blood_banks=blood_banks)
        
# #         # Save blood request
# #         conn = get_db()
# #         cursor = conn.cursor()
# #         cursor.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
# #                       (session['user_id'], hospital, f'Blood Request: {blood_type} x {units} units', 
# #                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
# #         conn.commit()
# #         conn.close()
        
# #         flash(f'Blood request placed: {blood_type} x {units} units at {hospital}', 'success')
# #         return redirect(url_for('dashboard'))
    
# #     return render_template('blood_booking.html', blood_types=blood_types, blood_banks=blood_banks)

# # @app.route('/navigation', methods=['GET', 'POST'])
# # @login_required
# # def navigation():
# #     locations = ['Entrance', 'Reception', 'Cardiology', 'Neurology', 'Pediatrics', 
# #                 'Orthopedics', 'Emergency', 'Pharmacy', 'Radiology', 'Laboratory', 'Cafeteria']
    
# #     directions = None
# #     if request.method == 'POST':
# #         start = request.form.get('start')
# #         end = request.form.get('end')
# #         directions = get_directions(start, end)
    
# #     return render_template('navigation.html', locations=locations, directions=directions)

# # def get_directions(start, end):
# #     """Helper function for navigation"""
# #     hospital_map = {
# #         'Entrance': (0, 0),
# #         'Reception': (5, 0),
# #         'Cardiology': (10, 5),
# #         'Neurology': (10, 10),
# #         'Pediatrics': (5, 15),
# #         'Orthopedics': (15, 5),
# #         'Emergency': (0, 10),
# #         'Pharmacy': (20, 5),
# #         'Radiology': (5, 20),
# #         'Laboratory': (10, 20),
# #         'Cafeteria': (20, 15)
# #     }
    
# #     if start not in hospital_map or end not in hospital_map:
# #         return "Invalid location selected!"
    
# #     start_pos = hospital_map[start]
# #     end_pos = hospital_map[end]
    
# #     dx = end_pos[0] - start_pos[0]
# #     dy = end_pos[1] - start_pos[1]
    
# #     directions = []
# #     directions.append(f"📍 From {start} to {end}")
# #     directions.append("-" * 40)
    
# #     if dx > 0:
# #         directions.append(f"→ Walk {dx} meters East")
# #     elif dx < 0:
# #         directions.append(f"← Walk {abs(dx)} meters West")
    
# #     if dy > 0:
# #         directions.append(f"↓ Walk {dy} meters South")
# #     elif dy < 0:
# #         directions.append(f"↑ Walk {abs(dy)} meters North")
    
# #     distance = ((dx**2) + (dy**2)) ** 0.5
# #     directions.append(f"\n📏 Total distance: {distance:.1f} meters")
# #     directions.append(f"⏱️ Estimated time: {(distance / 60):.1f} minutes")
    
# #     return '\n'.join(directions)

# # @app.route('/emergency', methods=['GET', 'POST'])
# # @login_required
# # def emergency():
# #     if request.method == 'POST':
# #         emergency_type = request.form.get('emergency_type')
# #         location = request.form.get('location', 'Hospital')
        
# #         conn = get_db()
# #         cursor = conn.cursor()
# #         cursor.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
# #                       (session['user_id'], location, emergency_type, 
# #                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
# #         conn.commit()
# #         conn.close()
        
# #         flash('🚨 Emergency team dispatched! Help is on the way.', 'emergency')
# #         return redirect(url_for('dashboard'))
    
# #     return render_template('emergency.html')

# # @app.route('/my-appointments')
# # @login_required
# # def my_appointments():
# #     conn = get_db()
# #     cursor = conn.cursor()
# #     cursor.execute("SELECT id, doctor_name, department, appointment_date, appointment_time, status FROM appointments WHERE user_id=? ORDER BY appointment_date DESC",
# #                   (session['user_id'],))
# #     appointments = cursor.fetchall()
# #     conn.close()
# #     return render_template('appointments.html', appointments=appointments)

# # @app.route('/cancel-appointment/<int:appointment_id>', methods=['POST'])
# # @login_required
# # def cancel_appointment(appointment_id):
# #     conn = get_db()
# #     cursor = conn.cursor()
# #     cursor.execute("UPDATE appointments SET status='cancelled' WHERE id=? AND user_id=?", 
# #                   (appointment_id, session['user_id']))
# #     conn.commit()
# #     conn.close()
    
# #     flash('Appointment cancelled successfully', 'info')
# #     return redirect(url_for('my_appointments'))

# # @app.route('/payment', methods=['GET', 'POST'])
# # @login_required
# # def payment():
# #     conn = get_db()
# #     cursor = conn.cursor()
    
# #     if request.method == 'POST':
# #         appointment_id = request.form.get('appointment_id')
# #         amount = float(request.form.get('amount', 500))
# #         method = request.form.get('method')
        
# #         cursor.execute("INSERT INTO payments (user_id, appointment_id, amount, payment_method, status, created_at) VALUES (?,?,?,?,?,?)",
# #                       (session['user_id'], appointment_id, amount, method, 'completed',
# #                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
# #         cursor.execute("UPDATE appointments SET status='confirmed' WHERE id=?", (appointment_id,))
# #         conn.commit()
        
# #         flash('Payment successful! Appointment confirmed.', 'success')
# #         return redirect(url_for('my_appointments'))
    
# #     # Get pending appointments
# #     cursor.execute("SELECT id, doctor_name, appointment_date, appointment_time FROM appointments WHERE user_id=? AND status='pending'",
# #                   (session['user_id'],))
# #     pending_apps = cursor.fetchall()
# #     conn.close()
    
# #     return render_template('payment.html', pending_apps=pending_apps)

# # @app.route('/payment-history')
# # @login_required
# # def payment_history():
# #     conn = get_db()
# #     cursor = conn.cursor()
# #     cursor.execute("SELECT p.id, p.appointment_id, p.amount, p.payment_method, p.status, p.created_at, a.doctor_name FROM payments p LEFT JOIN appointments a ON p.appointment_id = a.id WHERE p.user_id=? ORDER BY p.id DESC",
# #                   (session['user_id'],))
# #     payments = cursor.fetchall()
# #     conn.close()
    
# #     total = sum(p['amount'] for p in payments)
# #     return render_template('payment_history.html', payments=payments, total=total)

# # @app.route('/ai-assistant', methods=['GET', 'POST'])
# # @login_required
# # def ai_assistant():
# #     analysis_result = None
# #     if request.method == 'POST':
# #         symptoms = request.form.get('symptoms', '').lower()
        
# #         advice = []
# #         departments = set()
        
# #         symptom_map = {
# #             'fever': ('🤒 Fever', 'Rest and stay hydrated. Monitor temperature.', 'General Medicine'),
# #             'cough': ('🤧 Cough', 'Use mask, avoid cold drinks, steam inhalation.', 'General Medicine'),
# #             'headache': ('🤕 Headache', 'Rest in dark room, stay hydrated.', 'Neurology'),
# #             'chest': ('⚠️ Chest Pain', 'SEEK IMMEDIATE MEDICAL ATTENTION!', 'Cardiology'),
# #             'back': ('💪 Back Pain', 'Apply ice pack, gentle stretching.', 'Orthopedics'),
# #             'cold': ('😷 Cold', 'Steam inhalation, drink warm fluids.', 'General Medicine'),
# #             'stomach': ('🍽️ Stomach Issue', 'Avoid spicy food, drink ORS.', 'Gastroenterology'),
# #             'vomiting': ('🤢 Vomiting', 'Stay hydrated, eat bland food.', 'General Medicine'),
# #         }
        
# #         for key, (title, text, dept) in symptom_map.items():
# #             if key in symptoms:
# #                 advice.append(f"{title}\n{text}")
# #                 departments.add(dept)
        
# #         if advice:
# #             analysis_result = {
# #                 'advice': advice,
# #                 'departments': list(departments)
# #             }
# #         else:
# #             analysis_result = {
# #                 'advice': ['No specific symptoms detected. Consider a general checkup.'],
# #                 'departments': ['General Medicine']
# #             }
    
# #     return render_template('ai_assistant.html', analysis=analysis_result)

# # @app.route('/gps-calculator', methods=['GET', 'POST'])
# # @login_required
# # def gps_calculator():
# #     locations = ['Downtown', 'North Side', 'South Side', 'East End', 'West End']
# #     result = None
    
# #     if request.method == 'POST':
# #         location = request.form.get('location')
# #         if location:
# #             distance = round(random.uniform(0.5, 15.0), 1)
# #             result = {
# #                 'location': location,
# #                 'distance': distance,
# #                 'driving': int(distance * 2),
# #                 'walking': int(distance * 12),
# #                 'fare': int(distance * 15)
# #             }
    
# #     return render_template('gps_calculator.html', locations=locations, result=result)

# # @app.route('/get-doctors/<department>')
# # @login_required
# # def get_doctors(department):
# #     doctors = {
# #         'Cardiology': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams'],
# #         'Neurology': ['Dr. Brown', 'Dr. Jones', 'Dr. Garcia'],
# #         'Pediatrics': ['Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez'],
# #         'Orthopedics': ['Dr. Wilson', 'Dr. Martinez', 'Dr. Anderson'],
# #         'General Medicine': ['Dr. Taylor', 'Dr. Thomas', 'Dr. Moore']
# #     }
# #     return jsonify(doctors.get(department, []))

# # if __name__ == '__main__':
# #     app.run(debug=True, port=5001)













# from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
# from datetime import datetime
# import sqlite3
# import hashlib
# import os
# import random
# from functools import wraps

# app = Flask(__name__)
# app.secret_key = 'your-secret-key-change-in-production-12345'

# # Database helper functions
# def get_db():
#     conn = sqlite3.connect('hospital.db')
#     conn.row_factory = sqlite3.Row
#     return conn

# def hash_password(password):
#     return hashlib.sha256(password.encode()).hexdigest()

# # Initialize database
# def init_database():
#     """Create all tables if they don't exist"""
#     conn = sqlite3.connect('hospital.db')
#     c = conn.cursor()
    
#     # Users table
#     c.execute('''CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         email TEXT UNIQUE NOT NULL,
#         phone TEXT NOT NULL,
#         password TEXT NOT NULL,
#         user_type TEXT DEFAULT 'patient'
#     )''')
    
#     # Appointments table
#     c.execute('''CREATE TABLE IF NOT EXISTS appointments (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER NOT NULL,
#         doctor_name TEXT NOT NULL,
#         department TEXT NOT NULL,
#         appointment_date TEXT NOT NULL,
#         appointment_time TEXT NOT NULL,
#         status TEXT DEFAULT 'pending'
#     )''')
    
#     # Emergency table
#     c.execute('''CREATE TABLE IF NOT EXISTS emergencies (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER NOT NULL,
#         location TEXT,
#         emergency_type TEXT,
#         created_at TEXT
#     )''')
    
#     # Payments table
#     c.execute('''CREATE TABLE IF NOT EXISTS payments (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user_id INTEGER NOT NULL,
#         appointment_id INTEGER,
#         amount REAL NOT NULL,
#         payment_method TEXT,
#         status TEXT DEFAULT 'pending',
#         created_at TEXT
#     )''')
    
#     conn.commit()
#     conn.close()
#     print("✅ Database initialized successfully!")

# # Login decorator
# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if 'user_id' not in session:
#             flash('Please login to access this page', 'warning')
#             return redirect(url_for('login'))
#         return f(*args, **kwargs)
#     return decorated_function

# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
        
#         if not email or not password:
#             flash('Please enter email and password', 'danger')
#             return render_template('login.html')
        
#         conn = get_db()
#         cursor = conn.cursor()
#         cursor.execute("SELECT id, name, email, user_type FROM users WHERE email=? AND password=?", 
#                       (email, hash_password(password)))
#         user = cursor.fetchone()
#         conn.close()
        
#         if user:
#             session['user_id'] = user['id']
#             session['user_name'] = user['name']
#             session['user_type'] = user['user_type']
#             flash(f'Welcome back, {user["name"]}!', 'success')
#             return redirect(url_for('dashboard'))
#         else:
#             flash('Invalid email or password!', 'danger')
    
#     return render_template('login.html')

# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         password = request.form.get('password')
#         confirm_password = request.form.get('confirm_password')
#         user_type = request.form.get('user_type', 'patient')
        
#         if not all([name, email, phone, password]):
#             flash('All fields are required!', 'danger')
#             return render_template('login.html')
        
#         if password != confirm_password:
#             flash('Passwords do not match!', 'danger')
#             return render_template('login.html')
        
#         if len(password) < 6:
#             flash('Password must be at least 6 characters!', 'danger')
#             return render_template('login.html')
        
#         conn = get_db()
#         cursor = conn.cursor()
        
#         try:
#             cursor.execute("INSERT INTO users (name, email, phone, password, user_type) VALUES (?,?,?,?,?)",
#                           (name, email, phone, hash_password(password), user_type))
#             conn.commit()
#             flash('Registration successful! Please login.', 'success')
#             return redirect(url_for('login'))
#         except sqlite3.IntegrityError:
#             flash('Email already registered!', 'danger')
#         finally:
#             conn.close()
    
#     return render_template('login.html')

# @app.route('/logout')
# def logout():
#     session.clear()
#     flash('Logged out successfully', 'info')
#     return redirect(url_for('login'))

# @app.route('/dashboard')
# @login_required
# def dashboard():
#     conn = get_db()
#     cursor = conn.cursor()
    
#     # Get appointment count
#     cursor.execute("SELECT COUNT(*) FROM appointments WHERE user_id=?", (session['user_id'],))
#     appointment_count = cursor.fetchone()[0]
    
#     # Get recent appointments
#     cursor.execute("SELECT id, doctor_name, department, appointment_date, appointment_time, status FROM appointments WHERE user_id=? ORDER BY id DESC LIMIT 5",
#                   (session['user_id'],))
#     recent_appointments = cursor.fetchall()
    
#     conn.close()
    
#     return render_template('dashboard.html', 
#                          user_name=session.get('user_name'),
#                          user_type=session.get('user_type'),
#                          appointment_count=appointment_count,
#                          recent_appointments=recent_appointments)

# @app.route('/book-doctor', methods=['GET', 'POST'])
# @login_required
# def book_doctor():
#     doctors = {
#         'Cardiology': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams'],
#         'Neurology': ['Dr. Brown', 'Dr. Jones', 'Dr. Garcia'],
#         'Pediatrics': ['Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez'],
#         'Orthopedics': ['Dr. Wilson', 'Dr. Martinez', 'Dr. Anderson'],
#         'General Medicine': ['Dr. Taylor', 'Dr. Thomas', 'Dr. Moore']
#     }
#     time_slots = ['09:00 AM', '10:00 AM', '11:00 AM', '02:00 PM', '03:00 PM', '04:00 PM']
    
#     if request.method == 'POST':
#         department = request.form.get('department')
#         doctor = request.form.get('doctor')
#         date = request.form.get('date')
#         time_slot = request.form.get('time')
        
#         if not all([department, doctor, date, time_slot]):
#             flash('Please fill all fields!', 'danger')
#             return render_template('doctor_booking.html', doctors=doctors, time_slots=time_slots)
        
#         conn = get_db()
#         cursor = conn.cursor()
        
#         # Check if slot is available
#         cursor.execute("SELECT * FROM appointments WHERE doctor_name=? AND appointment_date=? AND appointment_time=? AND status != 'cancelled'",
#                       (doctor, date, time_slot))
#         existing = cursor.fetchone()
        
#         if existing:
#             flash('This time slot is already booked! Please choose another time.', 'danger')
#             conn.close()
#             return render_template('doctor_booking.html', doctors=doctors, time_slots=time_slots)
        
#         # Book appointment
#         cursor.execute("INSERT INTO appointments (user_id, doctor_name, department, appointment_date, appointment_time, status) VALUES (?,?,?,?,?,?)",
#                       (session['user_id'], doctor, department, date, time_slot, 'pending'))
#         conn.commit()
#         app_id = cursor.lastrowid
#         conn.close()
        
#         flash(f'Appointment booked successfully! ID: {app_id}', 'success')
#         return redirect(url_for('dashboard'))
    
#     return render_template('doctor_booking.html', doctors=doctors, time_slots=time_slots)

# @app.route('/book-bed', methods=['GET', 'POST'])
# @login_required
# def book_bed():
#     bed_types = ['General Ward', 'Semi-Private', 'Private Room', 'ICU', 'Emergency']
    
#     if request.method == 'POST':
#         bed_type = request.form.get('bed_type')
#         patient_name = request.form.get('patient_name')
#         date = request.form.get('date')
#         notes = request.form.get('notes')
        
#         if not all([bed_type, patient_name, date]):
#             flash('Please fill all required fields!', 'danger')
#             return render_template('bed_booking.html', bed_types=bed_types)
        
#         conn = get_db()
#         cursor = conn.cursor()
        
#         cursor.execute("INSERT INTO appointments (user_id, doctor_name, department, appointment_date, appointment_time, status) VALUES (?,?,?,?,?,?)",
#                       (session['user_id'], 'Bed Service', f'Bed: {bed_type}', date, 'Bed Booking', 'pending'))
#         conn.commit()
#         conn.close()
        
#         flash(f'Bed booked successfully! Type: {bed_type}', 'success')
#         return redirect(url_for('dashboard'))
    
#     return render_template('bed_booking.html', bed_types=bed_types)

# @app.route('/book-ambulance', methods=['GET', 'POST'])
# @login_required
# def book_ambulance():
#     if request.method == 'POST':
#         pickup_location = request.form.get('pickup_location')
#         patient_name = request.form.get('patient_name')
#         contact = request.form.get('contact')
#         date = request.form.get('date')
#         time = request.form.get('time')
#         notes = request.form.get('notes')
        
#         if not all([pickup_location, patient_name, contact, date, time]):
#             flash('Please fill all required fields!', 'danger')
#             return render_template('ambulance_booking.html')
        
#         conn = get_db()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
#                       (session['user_id'], pickup_location, f'Ambulance: {patient_name}', 
#                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#         conn.commit()
#         conn.close()
        
#         flash('Ambulance booked successfully! Estimated arrival: 10-15 minutes.', 'success')
#         return redirect(url_for('dashboard'))
    
#     return render_template('ambulance_booking.html')

# @app.route('/book-medicine', methods=['GET', 'POST'])
# @login_required
# def book_medicine():
#     medicines = {
#         'Paracetamol': {'price': 25, 'category': 'Pain Relief'},
#         'Aspirin': {'price': 30, 'category': 'Pain Relief'},
#         'Amoxicillin': {'price': 45, 'category': 'Antibiotic'},
#         'Cetirizine': {'price': 35, 'category': 'Antihistamine'},
#         'Omeprazole': {'price': 40, 'category': 'Gastric'},
#         'Vitamin C': {'price': 20, 'category': 'Vitamin'},
#         'Metformin': {'price': 50, 'category': 'Diabetes'},
#         'Amlodipine': {'price': 55, 'category': 'Cardiac'}
#     }
    
#     if request.method == 'POST':
#         medicine = request.form.get('medicine')
#         quantity = int(request.form.get('quantity', 1))
#         date = request.form.get('date')
        
#         if not all([medicine, quantity, date]):
#             flash('Please fill all required fields!', 'danger')
#             return render_template('medicine_booking.html', medicines=medicines)
        
#         conn = get_db()
#         cursor = conn.cursor()
#         amount = medicines[medicine]['price'] * quantity
        
#         cursor.execute("INSERT INTO payments (user_id, appointment_id, amount, payment_method, status, created_at) VALUES (?,?,?,?,?,?)",
#                       (session['user_id'], 0, amount, 'Pharmacy', 'pending',
#                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#         conn.commit()
#         conn.close()
        
#         flash(f'Medicine order placed for {medicine} x {quantity}. Total: ₹{amount}', 'success')
#         return redirect(url_for('dashboard'))
    
#     return render_template('medicine_booking.html', medicines=medicines)

# @app.route('/book-blood', methods=['GET', 'POST'])
# @login_required
# def book_blood():
#     blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
#     blood_banks = ['City Blood Bank', 'Red Cross Center', 'Hospital Blood Bank', 'Community Blood Center']
    
#     if request.method == 'POST':
#         blood_type = request.form.get('blood_type')
#         units = int(request.form.get('units', 1))
#         hospital = request.form.get('hospital')
#         date = request.form.get('date')
#         notes = request.form.get('notes')
        
#         if not all([blood_type, units, hospital, date]):
#             flash('Please fill all required fields!', 'danger')
#             return render_template('blood_booking.html', blood_types=blood_types, blood_banks=blood_banks)
        
#         conn = get_db()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
#                       (session['user_id'], hospital, f'Blood Request: {blood_type} x {units} units', 
#                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#         conn.commit()
#         conn.close()
        
#         flash(f'Blood request placed: {blood_type} x {units} units at {hospital}', 'success')
#         return redirect(url_for('dashboard'))
    
#     return render_template('blood_booking.html', blood_types=blood_types, blood_banks=blood_banks)

# @app.route('/navigation', methods=['GET', 'POST'])
# @login_required
# def navigation():
#     locations = ['Entrance', 'Reception', 'Cardiology', 'Neurology', 'Pediatrics', 
#                 'Orthopedics', 'Emergency', 'Pharmacy', 'Radiology', 'Laboratory', 'Cafeteria']
    
#     directions = None
#     if request.method == 'POST':
#         start = request.form.get('start')
#         end = request.form.get('end')
#         directions = get_directions(start, end)
    
#     return render_template('navigation.html', locations=locations, directions=directions)

# def get_directions(start, end):
#     hospital_map = {
#         'Entrance': (0, 0),
#         'Reception': (5, 0),
#         'Cardiology': (10, 5),
#         'Neurology': (10, 10),
#         'Pediatrics': (5, 15),
#         'Orthopedics': (15, 5),
#         'Emergency': (0, 10),
#         'Pharmacy': (20, 5),
#         'Radiology': (5, 20),
#         'Laboratory': (10, 20),
#         'Cafeteria': (20, 15)
#     }
    
#     if start not in hospital_map or end not in hospital_map:
#         return "Invalid location selected!"
    
#     start_pos = hospital_map[start]
#     end_pos = hospital_map[end]
    
#     dx = end_pos[0] - start_pos[0]
#     dy = end_pos[1] - start_pos[1]
    
#     directions = []
#     directions.append(f"📍 From {start} to {end}")
#     directions.append("-" * 40)
    
#     if dx > 0:
#         directions.append(f"→ Walk {dx} meters East")
#     elif dx < 0:
#         directions.append(f"← Walk {abs(dx)} meters West")
    
#     if dy > 0:
#         directions.append(f"↓ Walk {dy} meters South")
#     elif dy < 0:
#         directions.append(f"↑ Walk {abs(dy)} meters North")
    
#     distance = ((dx**2) + (dy**2)) ** 0.5
#     directions.append(f"\n📏 Total distance: {distance:.1f} meters")
#     directions.append(f"⏱️ Estimated time: {(distance / 60):.1f} minutes")
    
#     return '\n'.join(directions)

# @app.route('/emergency', methods=['GET', 'POST'])
# @login_required
# def emergency():
#     if request.method == 'POST':
#         emergency_type = request.form.get('emergency_type')
#         location = request.form.get('location', 'Hospital')
        
#         conn = get_db()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
#                       (session['user_id'], location, emergency_type, 
#                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#         conn.commit()
#         conn.close()
        
#         flash('🚨 Emergency team dispatched! Help is on the way.', 'emergency')
#         return redirect(url_for('dashboard'))
    
#     return render_template('emergency.html')

# @app.route('/my-appointments')
# @login_required
# def my_appointments():
#     conn = get_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, doctor_name, department, appointment_date, appointment_time, status FROM appointments WHERE user_id=? ORDER BY appointment_date DESC",
#                   (session['user_id'],))
#     appointments = cursor.fetchall()
#     conn.close()
#     return render_template('appointments.html', appointments=appointments)

# @app.route('/cancel-appointment/<int:appointment_id>', methods=['POST'])
# @login_required
# def cancel_appointment(appointment_id):
#     conn = get_db()
#     cursor = conn.cursor()
#     cursor.execute("UPDATE appointments SET status='cancelled' WHERE id=? AND user_id=?", 
#                   (appointment_id, session['user_id']))
#     conn.commit()
#     conn.close()
    
#     flash('Appointment cancelled successfully', 'info')
#     return redirect(url_for('my_appointments'))

# @app.route('/payment', methods=['GET', 'POST'])
# @login_required
# def payment():
#     conn = get_db()
#     cursor = conn.cursor()
    
#     if request.method == 'POST':
#         appointment_id = request.form.get('appointment_id')
#         amount = float(request.form.get('amount', 500))
#         method = request.form.get('method')
        
#         cursor.execute("INSERT INTO payments (user_id, appointment_id, amount, payment_method, status, created_at) VALUES (?,?,?,?,?,?)",
#                       (session['user_id'], appointment_id, amount, method, 'completed',
#                        datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
#         cursor.execute("UPDATE appointments SET status='confirmed' WHERE id=?", (appointment_id,))
#         conn.commit()
        
#         flash('Payment successful! Appointment confirmed.', 'success')
#         return redirect(url_for('my_appointments'))
    
#     # Get pending appointments
#     cursor.execute("SELECT id, doctor_name, appointment_date, appointment_time FROM appointments WHERE user_id=? AND status='pending'",
#                   (session['user_id'],))
#     pending_apps = cursor.fetchall()
#     conn.close()
    
#     return render_template('payment.html', pending_apps=pending_apps)

# @app.route('/payment-history')
# @login_required
# def payment_history():
#     conn = get_db()
#     cursor = conn.cursor()
#     cursor.execute("SELECT p.id, p.appointment_id, p.amount, p.payment_method, p.status, p.created_at, a.doctor_name FROM payments p LEFT JOIN appointments a ON p.appointment_id = a.id WHERE p.user_id=? ORDER BY p.id DESC",
#                   (session['user_id'],))
#     payments = cursor.fetchall()
#     conn.close()
    
#     total = sum(p['amount'] for p in payments)
#     return render_template('payment_history.html', payments=payments, total=total)

# @app.route('/ai-assistant', methods=['GET', 'POST'])
# @login_required
# def ai_assistant():
#     analysis_result = None
#     if request.method == 'POST':
#         symptoms = request.form.get('symptoms', '').lower()
        
#         advice = []
#         departments = set()
        
#         symptom_map = {
#             'fever': ('🤒 Fever', 'Rest and stay hydrated. Monitor temperature.', 'General Medicine'),
#             'cough': ('🤧 Cough', 'Use mask, avoid cold drinks, steam inhalation.', 'General Medicine'),
#             'headache': ('🤕 Headache', 'Rest in dark room, stay hydrated.', 'Neurology'),
#             'chest': ('⚠️ Chest Pain', 'SEEK IMMEDIATE MEDICAL ATTENTION!', 'Cardiology'),
#             'back': ('💪 Back Pain', 'Apply ice pack, gentle stretching.', 'Orthopedics'),
#             'cold': ('😷 Cold', 'Steam inhalation, drink warm fluids.', 'General Medicine'),
#             'stomach': ('🍽️ Stomach Issue', 'Avoid spicy food, drink ORS.', 'Gastroenterology'),
#             'vomiting': ('🤢 Vomiting', 'Stay hydrated, eat bland food.', 'General Medicine'),
#         }
        
#         for key, (title, text, dept) in symptom_map.items():
#             if key in symptoms:
#                 advice.append(f"{title}\n{text}")
#                 departments.add(dept)
        
#         if advice:
#             analysis_result = {
#                 'advice': advice,
#                 'departments': list(departments)
#             }
#         else:
#             analysis_result = {
#                 'advice': ['No specific symptoms detected. Consider a general checkup.'],
#                 'departments': ['General Medicine']
#             }
    
#     return render_template('ai_assistant.html', analysis=analysis_result)

# @app.route('/gps-calculator', methods=['GET', 'POST'])
# @login_required
# def gps_calculator():
#     locations = ['Downtown', 'North Side', 'South Side', 'East End', 'West End']
#     result = None
    
#     if request.method == 'POST':
#         location = request.form.get('location')
#         if location:
#             distance = round(random.uniform(0.5, 15.0), 1)
#             result = {
#                 'location': location,
#                 'distance': distance,
#                 'driving': int(distance * 2),
#                 'walking': int(distance * 12),
#                 'fare': int(distance * 15)
#             }
    
#     return render_template('gps_calculator.html', locations=locations, result=result)

# @app.route('/get-doctors/<department>')
# @login_required
# def get_doctors(department):
#     doctors = {
#         'Cardiology': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams'],
#         'Neurology': ['Dr. Brown', 'Dr. Jones', 'Dr. Garcia'],
#         'Pediatrics': ['Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez'],
#         'Orthopedics': ['Dr. Wilson', 'Dr. Martinez', 'Dr. Anderson'],
#         'General Medicine': ['Dr. Taylor', 'Dr. Thomas', 'Dr. Moore']
#     }
#     return jsonify(doctors.get(department, []))

# if __name__ == '__main__':
#     # Initialize database first
#     init_database()
#     app.run(debug=True, port=5001)










from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import datetime
import sqlite3
import hashlib
import os
import random
from functools import wraps

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-in-production-12345'

# Database helper functions
def get_db():
    conn = sqlite3.connect('hospital.db')
    conn.row_factory = sqlite3.Row
    return conn

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Initialize database
def init_database():
    """Create all tables if they don't exist"""
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT NOT NULL,
        password TEXT NOT NULL,
        user_type TEXT DEFAULT 'patient'
    )''')
    
    # Appointments table
    c.execute('''CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        doctor_name TEXT NOT NULL,
        department TEXT NOT NULL,
        appointment_date TEXT NOT NULL,
        appointment_time TEXT NOT NULL,
        status TEXT DEFAULT 'pending'
    )''')
    
    # Emergency table
    c.execute('''CREATE TABLE IF NOT EXISTS emergencies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        location TEXT,
        emergency_type TEXT,
        created_at TEXT
    )''')
    
    # Payments table
    c.execute('''CREATE TABLE IF NOT EXISTS payments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        appointment_id INTEGER,
        amount REAL NOT NULL,
        payment_method TEXT,
        status TEXT DEFAULT 'pending',
        created_at TEXT
    )''')
    
    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

# Login decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please login to access this page', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email or not password:
            flash('Please enter email and password', 'danger')
            return render_template('login.html')
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, user_type FROM users WHERE email=? AND password=?", 
                      (email, hash_password(password)))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_type'] = user['user_type']
            flash(f'Welcome back, {user["name"]}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password!', 'danger')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        user_type = request.form.get('user_type', 'patient')
        
        if not all([name, email, phone, password]):
            flash('All fields are required!', 'danger')
            return render_template('login.html')
        
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return render_template('login.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters!', 'danger')
            return render_template('login.html')
        
        conn = get_db()
        cursor = conn.cursor()
        
        try:
            cursor.execute("INSERT INTO users (name, email, phone, password, user_type) VALUES (?,?,?,?,?)",
                          (name, email, phone, hash_password(password), user_type))
            conn.commit()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email already registered!', 'danger')
        finally:
            conn.close()
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    conn = get_db()
    cursor = conn.cursor()
    
    # Get appointment count
    cursor.execute("SELECT COUNT(*) FROM appointments WHERE user_id=?", (session['user_id'],))
    appointment_count = cursor.fetchone()[0]
    
    # Get recent appointments
    cursor.execute("SELECT id, doctor_name, department, appointment_date, appointment_time, status FROM appointments WHERE user_id=? ORDER BY id DESC LIMIT 5",
                  (session['user_id'],))
    recent_appointments = cursor.fetchall()
    
    conn.close()
    
    return render_template('dashboard.html', 
                         user_name=session.get('user_name'),
                         user_type=session.get('user_type'),
                         appointment_count=appointment_count,
                         recent_appointments=recent_appointments)

@app.route('/book-doctor', methods=['GET', 'POST'])
@login_required
def book_doctor():
    doctors = {
        'Cardiology': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams'],
        'Neurology': ['Dr. Brown', 'Dr. Jones', 'Dr. Garcia'],
        'Pediatrics': ['Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez'],
        'Orthopedics': ['Dr. Wilson', 'Dr. Martinez', 'Dr. Anderson'],
        'General Medicine': ['Dr. Taylor', 'Dr. Thomas', 'Dr. Moore']
    }
    time_slots = ['09:00 AM', '10:00 AM', '11:00 AM', '02:00 PM', '03:00 PM', '04:00 PM']
    
    if request.method == 'POST':
        department = request.form.get('department')
        doctor = request.form.get('doctor')
        date = request.form.get('date')
        time_slot = request.form.get('time')
        
        if not all([department, doctor, date, time_slot]):
            flash('Please fill all fields!', 'danger')
            return render_template('doctor_booking.html', doctors=doctors, time_slots=time_slots)
        
        conn = get_db()
        cursor = conn.cursor()
        
        # Check if slot is available
        cursor.execute("SELECT * FROM appointments WHERE doctor_name=? AND appointment_date=? AND appointment_time=? AND status != 'cancelled'",
                      (doctor, date, time_slot))
        existing = cursor.fetchone()
        
        if existing:
            flash('This time slot is already booked! Please choose another time.', 'danger')
            conn.close()
            return render_template('doctor_booking.html', doctors=doctors, time_slots=time_slots)
        
        # Book appointment
        cursor.execute("INSERT INTO appointments (user_id, doctor_name, department, appointment_date, appointment_time, status) VALUES (?,?,?,?,?,?)",
                      (session['user_id'], doctor, department, date, time_slot, 'pending'))
        conn.commit()
        app_id = cursor.lastrowid
        conn.close()
        
        flash(f'Appointment booked successfully! ID: {app_id}', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('doctor_booking.html', doctors=doctors, time_slots=time_slots)

@app.route('/book-bed', methods=['GET', 'POST'])
@login_required
def book_bed():
    bed_types = ['General Ward', 'Semi-Private', 'Private Room', 'ICU', 'Emergency']
    
    if request.method == 'POST':
        bed_type = request.form.get('bed_type')
        patient_name = request.form.get('patient_name')
        date = request.form.get('date')
        notes = request.form.get('notes')
        
        if not all([bed_type, patient_name, date]):
            flash('Please fill all required fields!', 'danger')
            return render_template('bed_booking.html', bed_types=bed_types)
        
        conn = get_db()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO appointments (user_id, doctor_name, department, appointment_date, appointment_time, status) VALUES (?,?,?,?,?,?)",
                      (session['user_id'], 'Bed Service', f'Bed: {bed_type}', date, 'Bed Booking', 'pending'))
        conn.commit()
        conn.close()
        
        flash(f'Bed booked successfully! Type: {bed_type}', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('bed_booking.html', bed_types=bed_types)

@app.route('/book-ambulance', methods=['GET', 'POST'])
@login_required
def book_ambulance():
    if request.method == 'POST':
        pickup_location = request.form.get('pickup_location')
        patient_name = request.form.get('patient_name')
        contact = request.form.get('contact')
        date = request.form.get('date')
        time = request.form.get('time')
        notes = request.form.get('notes')
        
        if not all([pickup_location, patient_name, contact, date, time]):
            flash('Please fill all required fields!', 'danger')
            return render_template('ambulance_booking.html')
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
                      (session['user_id'], pickup_location, f'Ambulance: {patient_name}', 
                       datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()
        
        flash('Ambulance booked successfully! Estimated arrival: 10-15 minutes.', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('ambulance_booking.html')

@app.route('/book-medicine', methods=['GET', 'POST'])
@login_required
def book_medicine():
    medicines = {
        'Paracetamol': {'price': 25, 'category': 'Pain Relief'},
        'Aspirin': {'price': 30, 'category': 'Pain Relief'},
        'Amoxicillin': {'price': 45, 'category': 'Antibiotic'},
        'Cetirizine': {'price': 35, 'category': 'Antihistamine'},
        'Omeprazole': {'price': 40, 'category': 'Gastric'},
        'Vitamin C': {'price': 20, 'category': 'Vitamin'},
        'Metformin': {'price': 50, 'category': 'Diabetes'},
        'Amlodipine': {'price': 55, 'category': 'Cardiac'}
    }
    
    if request.method == 'POST':
        medicine = request.form.get('medicine')
        quantity = int(request.form.get('quantity', 1))
        date = request.form.get('date')
        
        if not all([medicine, quantity, date]):
            flash('Please fill all required fields!', 'danger')
            return render_template('medicine_booking.html', medicines=medicines)
        
        conn = get_db()
        cursor = conn.cursor()
        amount = medicines[medicine]['price'] * quantity
        
        cursor.execute("INSERT INTO payments (user_id, appointment_id, amount, payment_method, status, created_at) VALUES (?,?,?,?,?,?)",
                      (session['user_id'], 0, amount, 'Pharmacy', 'pending',
                       datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()
        
        flash(f'Medicine order placed for {medicine} x {quantity}. Total: ₹{amount}', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('medicine_booking.html', medicines=medicines)

@app.route('/book-blood', methods=['GET', 'POST'])
@login_required
def book_blood():
    blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    blood_banks = ['City Blood Bank', 'Red Cross Center', 'Hospital Blood Bank', 'Community Blood Center']
    
    if request.method == 'POST':
        blood_type = request.form.get('blood_type')
        units = int(request.form.get('units', 1))
        hospital = request.form.get('hospital')
        date = request.form.get('date')
        notes = request.form.get('notes')
        
        if not all([blood_type, units, hospital, date]):
            flash('Please fill all required fields!', 'danger')
            return render_template('blood_booking.html', blood_types=blood_types, blood_banks=blood_banks)
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
                      (session['user_id'], hospital, f'Blood Request: {blood_type} x {units} units', 
                       datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()
        
        flash(f'Blood request placed: {blood_type} x {units} units at {hospital}', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('blood_booking.html', blood_types=blood_types, blood_banks=blood_banks)

@app.route('/navigation', methods=['GET', 'POST'])
@login_required
def navigation():
    locations = ['Entrance', 'Reception', 'Cardiology', 'Neurology', 'Pediatrics', 
                'Orthopedics', 'Emergency', 'Pharmacy', 'Radiology', 'Laboratory', 'Cafeteria']
    
    directions = None
    if request.method == 'POST':
        start = request.form.get('start')
        end = request.form.get('end')
        directions = get_directions(start, end)
    
    return render_template('navigation.html', locations=locations, directions=directions)

def get_directions(start, end):
    hospital_map = {
        'Entrance': (0, 0),
        'Reception': (5, 0),
        'Cardiology': (10, 5),
        'Neurology': (10, 10),
        'Pediatrics': (5, 15),
        'Orthopedics': (15, 5),
        'Emergency': (0, 10),
        'Pharmacy': (20, 5),
        'Radiology': (5, 20),
        'Laboratory': (10, 20),
        'Cafeteria': (20, 15)
    }
    
    if start not in hospital_map or end not in hospital_map:
        return "Invalid location selected!"
    
    start_pos = hospital_map[start]
    end_pos = hospital_map[end]
    
    dx = end_pos[0] - start_pos[0]
    dy = end_pos[1] - start_pos[1]
    
    directions = []
    directions.append(f"📍 From {start} to {end}")
    directions.append("-" * 40)
    
    if dx > 0:
        directions.append(f"→ Walk {dx} meters East")
    elif dx < 0:
        directions.append(f"← Walk {abs(dx)} meters West")
    
    if dy > 0:
        directions.append(f"↓ Walk {dy} meters South")
    elif dy < 0:
        directions.append(f"↑ Walk {abs(dy)} meters North")
    
    distance = ((dx**2) + (dy**2)) ** 0.5
    directions.append(f"\n📏 Total distance: {distance:.1f} meters")
    directions.append(f"⏱️ Estimated time: {(distance / 60):.1f} minutes")
    
    return '\n'.join(directions)

@app.route('/emergency', methods=['GET', 'POST'])
@login_required
def emergency():
    if request.method == 'POST':
        emergency_type = request.form.get('emergency_type')
        location = request.form.get('location', 'Hospital')
        
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO emergencies (user_id, location, emergency_type, created_at) VALUES (?,?,?,?)",
                      (session['user_id'], location, emergency_type, 
                       datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        conn.close()
        
        flash('🚨 Emergency team dispatched! Help is on the way.', 'emergency')
        return redirect(url_for('dashboard'))
    
    return render_template('emergency.html')

@app.route('/my-appointments')
@login_required
def my_appointments():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, doctor_name, department, appointment_date, appointment_time, status FROM appointments WHERE user_id=? ORDER BY appointment_date DESC",
                  (session['user_id'],))
    appointments = cursor.fetchall()
    conn.close()
    return render_template('appointments.html', appointments=appointments)

@app.route('/cancel-appointment/<int:appointment_id>', methods=['POST'])
@login_required
def cancel_appointment(appointment_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE appointments SET status='cancelled' WHERE id=? AND user_id=?", 
                  (appointment_id, session['user_id']))
    conn.commit()
    conn.close()
    
    flash('Appointment cancelled successfully', 'info')
    return redirect(url_for('my_appointments'))

@app.route('/payment', methods=['GET', 'POST'])
@login_required
def payment():
    conn = get_db()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        appointment_id = request.form.get('appointment_id')
        amount = float(request.form.get('amount', 500))
        method = request.form.get('method')
        
        cursor.execute("INSERT INTO payments (user_id, appointment_id, amount, payment_method, status, created_at) VALUES (?,?,?,?,?,?)",
                      (session['user_id'], appointment_id, amount, method, 'completed',
                       datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        cursor.execute("UPDATE appointments SET status='confirmed' WHERE id=?", (appointment_id,))
        conn.commit()
        
        flash('Payment successful! Appointment confirmed.', 'success')
        return redirect(url_for('my_appointments'))
    
    # Get pending appointments
    cursor.execute("SELECT id, doctor_name, appointment_date, appointment_time FROM appointments WHERE user_id=? AND status='pending'",
                  (session['user_id'],))
    pending_apps = cursor.fetchall()
    conn.close()
    
    return render_template('payment.html', pending_apps=pending_apps)

@app.route('/payment-history')
@login_required
def payment_history():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT p.id, p.appointment_id, p.amount, p.payment_method, p.status, p.created_at, a.doctor_name FROM payments p LEFT JOIN appointments a ON p.appointment_id = a.id WHERE p.user_id=? ORDER BY p.id DESC",
                  (session['user_id'],))
    payments = cursor.fetchall()
    conn.close()
    
    total = sum(p['amount'] for p in payments)
    return render_template('payment_history.html', payments=payments, total=total)

@app.route('/ai-assistant', methods=['GET', 'POST'])
@login_required
def ai_assistant():
    analysis_result = None
    if request.method == 'POST':
        symptoms = request.form.get('symptoms', '').lower()
        
        advice = []
        departments = set()
        
        symptom_map = {
            'fever': ('🤒 Fever', 'Rest and stay hydrated. Monitor temperature.', 'General Medicine'),
            'cough': ('🤧 Cough', 'Use mask, avoid cold drinks, steam inhalation.', 'General Medicine'),
            'headache': ('🤕 Headache', 'Rest in dark room, stay hydrated.', 'Neurology'),
            'chest': ('⚠️ Chest Pain', 'SEEK IMMEDIATE MEDICAL ATTENTION!', 'Cardiology'),
            'back': ('💪 Back Pain', 'Apply ice pack, gentle stretching.', 'Orthopedics'),
            'cold': ('😷 Cold', 'Steam inhalation, drink warm fluids.', 'General Medicine'),
            'stomach': ('🍽️ Stomach Issue', 'Avoid spicy food, drink ORS.', 'Gastroenterology'),
            'vomiting': ('🤢 Vomiting', 'Stay hydrated, eat bland food.', 'General Medicine'),
        }
        
        for key, (title, text, dept) in symptom_map.items():
            if key in symptoms:
                advice.append(f"{title}\n{text}")
                departments.add(dept)
        
        if advice:
            analysis_result = {
                'advice': advice,
                'departments': list(departments)
            }
        else:
            analysis_result = {
                'advice': ['No specific symptoms detected. Consider a general checkup.'],
                'departments': ['General Medicine']
            }
    
    return render_template('ai_assistant.html', analysis=analysis_result)

@app.route('/gps-calculator', methods=['GET', 'POST'])
@login_required
def gps_calculator():
    locations = ['Downtown', 'North Side', 'South Side', 'East End', 'West End']
    result = None
    
    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            distance = round(random.uniform(0.5, 15.0), 1)
            result = {
                'location': location,
                'distance': distance,
                'driving': int(distance * 2),
                'walking': int(distance * 12),
                'fare': int(distance * 15)
            }
    
    return render_template('gps_calculator.html', locations=locations, result=result)

@app.route('/get-doctors/<department>')
@login_required
def get_doctors(department):
    doctors = {
        'Cardiology': ['Dr. Smith', 'Dr. Johnson', 'Dr. Williams'],
        'Neurology': ['Dr. Brown', 'Dr. Jones', 'Dr. Garcia'],
        'Pediatrics': ['Dr. Miller', 'Dr. Davis', 'Dr. Rodriguez'],
        'Orthopedics': ['Dr. Wilson', 'Dr. Martinez', 'Dr. Anderson'],
        'General Medicine': ['Dr. Taylor', 'Dr. Thomas', 'Dr. Moore']
    }
    return jsonify(doctors.get(department, []))

if __name__ == '__main__':
    # Initialize database first
    init_database()
    
    # Create test user if not exists
    conn = sqlite3.connect('hospital.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email='test@test.com'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (name, email, phone, password, user_type) VALUES (?,?,?,?,?)",
                      ('Test User', 'test@test.com', '9876543210', hash_password('test123'), 'patient'))
        conn.commit()
        print("✅ Test user created: test@test.com / test123")
    conn.close()
    
    app.run(debug=True, port=5001)