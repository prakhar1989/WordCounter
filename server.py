from flask import Flask, jsonify, request, render_template, abort
from app import utils
from app import db

### APP ###
app = Flask(__name__)

@app.route("/")
def main():
    # TODO: fetch a random value from db
    text_model = db.fetch_text(1341441)
    if not text_model:
        abort(500) # Server error
    text, words, token = text_model
    resp = { "text": text, "words": words.split(), "token" : token }
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
    # persist in db
    #text = request.post("text")
    #words = utils.generate_excluded_words(text)
    #text, words = utils.get_random_text()
    #token = utils.generate_token()
    return "Data added!"

if __name__ == "__main__":
    app.run(debug=True)
