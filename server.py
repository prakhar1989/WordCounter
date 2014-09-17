# -*- coding: utf-8 -*-
"""
Server app for WordCount Validator
"""
from flask import Flask, jsonify, request, render_template, abort, redirect, g
from app import utils
from app import db
import os
import sqlite3

### APP ###
app = Flask(__name__)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, "data/texts.db"),
    DEBUG=True
))

# -------------
# DB OPERATIONS
# -------------
def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def setup_db(seed=True):
    """ create a new DB and add seed data if seed is True """
    db = connect_db()
    c = db.cursor()
    c.execute(''' DROP TABLE IF EXISTS texts ''')
    c.execute(''' CREATE TABLE texts (body TEXT, words TEXT, token INTEGER PRIMARY KEY) ''')
    if seed:
        t = ("the quick brown fox jumped over the lazy dog", \
             "for brown lazy", utils.generate_token())
        c.execute("INSERT INTO texts VALUES (?, ?, ?)", t)
    db.commit()
    db.close()

# g is request specific and dies at the end 
# of the reqeust - ensuring statelessness
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def db_fetch_text(token):
    db = get_db()
    c = db.cursor()
    try:
        token = int(token)
    except ValueError:
        return (None, None, None)
    c.execute('SELECT * FROM texts WHERE token=?', (token, ))
    result = c.fetchone()
    return result

def db_add_text(text, words, token):
    db = get_db()
    c = db.cursor()
    text = (text, words, token)
    c.execute("INSERT INTO texts VALUES (?, ?, ?)", text)
    db.commit()

def db_get_random_text():
    db = get_db()
    c = db.cursor()
    c.execute("SELECT * FROM texts ORDER BY RANDOM() LIMIT 1")
    result = c.fetchone()
    return result

# ------
# ROUTES
# ------
@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "GET":
        if request.args.get("random"):
            token = utils.generate_token()
            text, words = utils.generate_random_text()
            db_add_text(text, words, token)
        else:
            text_model = db_get_random_text()
            if not text_model: # if nothing in DB, generate random text
                redirect("/?random=true")
            text, words, token = text_model
        resp = { "text": text, "words": words.split(), "token" : token }
        return jsonify(resp)
    else:
        if not request.json or not request.json.get("token") or \
           not request.json.get('text') or not request.json.get('words'):
            abort(400)
        data = request.json
        text_model = db_fetch_text(data.get('token'))
        if not text_model or text_model[0] != data.get('text') or \
           not utils.validate_word_count(text_model[0], text_model[1], data.get('words')):
            abort(400)
        return jsonify({"status": "success"})

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/add', methods=["POST"])
def add():
    text = request.form["text"]
    words = request.form["words"]
    if not words:
        # autogenerate words
        words = " ".join(utils.get_exclusion_words(text))
        print words
    else:
        for word in words.split():
            if word not in text.split():
                return jsonify({"status":
                    "Invalid data - few words not found in data."})
    token = utils.generate_token()
    db_add_text(text, words, token)
    return jsonify({"status": "Data added successfully"})

if __name__ == "__main__":
    app.run(port=8000)
