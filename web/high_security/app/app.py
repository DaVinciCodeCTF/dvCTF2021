from flask import Flask, render_template, request, flash, redirect, url_for, abort, session
from flask_mysqldb import MySQL
from functools import wraps
from datetime import datetime
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'lol1337test1h0p3n01s33this'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'hs_db'
app.config['MYSQL_USER'] = 'reallystrongadmin'
app.config['MYSQL_PASSWORD'] = 'Yr%Pq79J6My7wb'
app.config['MYSQL_DB'] = 'useless_site'

mysql = MySQL(app)

def no_sqlmap(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.headers.getlist("User-Agent"):
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
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, username, admin FROM users WHERE username=%s AND password=%s", (username, password))
        account = cur.fetchone()

        if account:
            # Create session data, we can access this data in other routes
            session['logged_in'] = True
            session['id'] = account[0]
            session['username'] = account[1]
            session['admin'] = account[2]
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            cur.execute("SELECT id, username FROM users WHERE username=%s", (username,))
            account_exists = cur.fetchone()
            if account_exists:

                if request.headers.getlist("X-Forwarded-For"):
                    ip = request.headers.getlist("X-Forwarded-For")[0]
                else:
                    ip = request.remote_addr

                time_connection = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
                app.logger.info(f'Failed connection from {ip}')
                cur.execute("INSERT INTO login_attempts (user_id, ip, time) VALUES (%s, %s, %s)", (account_exists[0], ip, time_connection))
                mysql.connection.commit()
                # Account doesnt exist or username/password incorrect
                msg = 'Incorrect password!'
                flash(msg)
                return render_template('login.html')
            else:
                # Account doesnt exist or username/password incorrect
                msg = 'Incorrect username!'
                flash(msg)
                return render_template('login.html')
    # Show the login form with message (if any)
    else:
        return render_template('login.html')

@app.route("/register", methods=["GET", "POST"])
@no_sqlmap
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        account_exists = cur.execute("SELECT username FROM users WHERE username=%s", (username,))
        if account_exists:
            msg = 'Username taken'
            flash(msg)
            return render_template('register.html')

        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        msg = 'You created your account. You can now log in'
        flash(msg)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route("/logout")
@no_sqlmap
def logout():
    session['logged_in'] = False
    return home()

@app.route("/security")
@no_sqlmap
def members():
    cur = mysql.connection.cursor()
    if session['admin']:
        cur.execute("SELECT id, ip, time FROM login_attempts WHERE user_id=%s", (session['id'],))
    else:
        cur.execute("SELECT id, ip, time FROM login_attempts WHERE user_id=%s", (session['id'],))
    login_attempts = cur.fetchall()
    ids = [(i[0],) for i in login_attempts]
    cur = mysql.connection.cursor()
    cur.executemany("DELETE FROM login_attempts WHERE id=%s", ids)
    mysql.connection.commit()
    return render_template("security.html", attempts=login_attempts)

if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0', port='80')
