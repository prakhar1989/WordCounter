from flask import Flask, jsonify, request, render_template, abort
import json
import utils
import db

### APP ###
app = Flask(__name__)

@app.route("/")
def main():
    text, words = utils.get_random_text()
    token = utils.generate_token()
    # TODO: presist in DB
    resp = { "text": text, "words": words, "token" : token }
    return jsonify(resp)

@app.route("/validate", methods=["POST"])
def validate():
    data = request.json
    text_model = db.fetch_text(data.get('token'))
    if not text_model or text_model[0] != data.get('text') or \
       not utils.validate_word_count(text_model[0], text_model[1], data.get('words')):
        abort(400)
    return jsonify({"status": "success"})

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/add', methods=["POST"])
def add():
    return "Data added!"

if __name__ == "__main__":
    app.run(debug=True)
