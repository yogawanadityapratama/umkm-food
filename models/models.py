import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS post (
    id INTEGER PRIMARY KEY,
    nama VARCHAR(255),
    ket VARCHAR (255),
    harga INT(11),
    link VARCHAR(255),
    link_image VARCHAR(255),
    date VARCHAR(255)
);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
''')
connection.commit()
connection.close()