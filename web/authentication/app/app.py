from flask import Flask, render_template, request, flash, redirect, url_for, abort, session
from flask_mysqldb import MySQL
from functools import wraps
import sqlite3

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'd4v1nc1c0d3'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'mysql_db'
app.config['MYSQL_USER'] = 'guill4ume'
app.config['MYSQL_PASSWORD'] = 'v3ry_s3cure_p455w0rd'
app.config['MYSQL_DB'] = 'lajoute'

mysql = MySQL(app)

def no_sqlmap(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'sqlmap' in request.headers.get('User-Agent') or 'buster' in request.headers.get('User-Agent'):
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
@no_sqlmap
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('home.html')

@app.route("/login", methods=["GET", "POST"])
@no_sqlmap
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        conn = sqlite3.connect('accounts.db')
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        c = conn.cursor()
        # Check if account exists using SQLite
        c.execute(f"SELECT * FROM accounts WHERE username='{username}' AND password='{password}'")
        # Fetch one record and return result
        account = c.fetchone()
        conn.close()

        if account:
            # Create session data, we can access this data in other routes
            session['logged_in'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            session['admin'] = account[3]
            # Redirect to home page
            return redirect(url_for('home'))
        elif username == 'admin':
            # Account doesnt exist or username/password incorrect
            msg = 'How dare you!'
            flash(msg)
            return render_template('login.html')
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
            flash(msg)
            return render_template('login.html')
    # Show the login form with message (if any)
    else:
        return render_template('login.html')

@app.route("/logout")
@no_sqlmap
def logout():
    session['logged_in'] = False
    return home()

@app.route("/members")
@no_sqlmap
def members():
    if session['logged_in']:
        cur = mysql.connection.cursor()

        if 'q' not in request.args.keys():
            # Check if account exists using SQLite
            cur.execute("SELECT name, address, payed_cotisation FROM members")
            # Fetch all records
            joute_members = cur.fetchall()
        else:
            try:
                cur.execute(f'SELECT name, address, payed_cotisation FROM members WHERE name LIKE "%{request.args["q"]}%"')
                joute_members = cur.fetchall()
            except:
                joute_members = []

        return render_template("members.html", members=joute_members)
    else:
        redirect(url_for('login'))

if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0', port='80')
