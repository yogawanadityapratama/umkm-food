from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
from passlib.hash import sha256_crypt
import datetime

app = Flask(__name__)
app.secret_key = 'secret_key'

def connect_db():
    return sqlite3.connect("database.db")

@app.route('/')
def index():
    if 'user' in session:
        return redirect('/read')
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM post")
    posts = cursor.fetchall()
    connection.close()
    return render_template('out.html', posts=posts)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('Username already exists. Please choose a different one.', 'error')
        else:
            hashed_password = sha256_crypt.using(rounds=1000).hash(password)
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            connection.commit()
            flash('Account created successfully! Please login.', 'success')
            return redirect(url_for('signin'))

        connection.close()

    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        user = cursor.fetchone()

        if user and sha256_crypt.verify(password, user[2]):
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password. Please try again.', 'error')

        connection.close()

    return render_template('signin.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/create', methods=["POST"])
def create():
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO post (nama, ket, harga, link, link_image, date) VALUES (?, ?, ?, ?, ?, ?)",
                   (request.form['nama'], request.form['ket'], request.form['harga'], request.form['link'], request.form['link_image'],today))
    connection.commit()
    connection.close()
    return redirect('/read')

@app.route('/read')
def read():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM post")
    posts = cursor.fetchall()
    connection.close()
    return render_template('read.html', posts=posts)

@app.route('/update/<int:id>', methods=['GET'])
def get(id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM post WHERE id=?", (id,))
    post = cursor.fetchone()
    connection.close()
    return render_template('update.html', post=post)

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("UPDATE post SET nama=?, ket=?, harga=?, link=?, link_image=?, date=? WHERE id=?",
                   (request.form['nama'], request.form['ket'], request.form['harga'], request.form['link'], request.form['link_image'], today, id))
    connection.commit()
    connection.close()
    return redirect('/read')

@app.route('/delete/<int:id>')
def delete(id):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM post WHERE id=?", (id,))
    connection.commit()
    connection.close()
    return redirect('/read')

if __name__ == '__main__':
    app.run(debug=True)