import sqlite3
import argparse
import utils

DATABASE = "data/texts.db"

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

def add_text(text, words, token):
    db = get_db()
    c = db.cursor()
    text = (text, words, token)
    c.execute('INSERT INTO texts VALUES (?, ?, ?)', text)
    db.commit()
    db.close()

def get_random_text():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM texts ORDER BY RANDOM() LIMIT 1")
    result = c.fetchone()
    db.close()
    return result

def setup():
    db = get_db()
    c = db.cursor()
    c.execute(''' DROP TABLE IF EXISTS texts ''')
    c.execute(''' CREATE TABLE texts (body TEXT, words TEXT, token INTEGER PRIMARY KEY) ''')
    db.commit()
    db.close()

if __name__ == "__main__":
    # ADD DECORATORS OR WITH IF POSSIBLE
    parser = argparse.ArgumentParser(description="Setup data for WordCount Validator")
    parser.add_argument("setup", help="Initialize database", nargs="?")

    args = parser.parse_args()
    if args.setup:
        print "Setting up database ...",
        setup()
        # seed data
        add_text("the quick brown fox jumped over the lazy dog", \
                 "fox brown lazy", utils.generate_token())
        print "Done."
