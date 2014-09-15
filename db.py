## SETUP A DECORATOR
import sqlite3

DATABASE = 'data/texts.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

def fetch_text(token):
    db = get_db()
    c = db.cursor()
    c.execute('SELECT * FROM texts WHERE token=?', (int(token), ))
    result = c.fetchone()
    db.close()
    return result

def add_text(token):
    db = get_db()
    c = db.cursor()
    text = ("the quick brown fox jumped on the lazy dog", "quick brown lazy", token)
    c.execute('INSERT INTO texts VALUES (?, ?, ?)', text)
    db.commit()
    db.close()

def setup():
    db = get_db()
    c = db.cursor()
    c.execute(''' DROP TABLE IF EXISTS texts ''')
    c.execute(''' CREATE TABLE texts (body TEXT, words TEXT, token INTEGER) ''')
    db.commit()
    db.close()

if __name__ == "__main__":
    setup()
