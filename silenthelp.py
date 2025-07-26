from flask import Flask, render_template, request, redirect, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'secret123'

DB_FILE = 'data.db'

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                description TEXT,
                location TEXT,
                preferred_mode TEXT,
                email TEXT
            )
        ''')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    category = request.form['category']
    description = request.form['description']
    location = request.form['location']
    preferred_mode = request.form['preferred_mode']
    email = request.form.get('email')

    with sqlite3.connect(DB_FILE) as conn:
        conn.execute(
            "INSERT INTO requests (category, description, location, preferred_mode, email) VALUES (?, ?, ?, ?, ?)",
            (category, description, location, preferred_mode, email)
        )

    flash("Your anonymous request has been submitted. Thank you!")
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.execute("SELECT * FROM requests")
        requests_data = cursor.fetchall()
    return render_template('dashboard.html', requests=requests_data)

if __name__ == '__main__':
    if not os.path.exists(DB_FILE):
        init_db()
    app.run(debug=True)
