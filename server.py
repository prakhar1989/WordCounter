from flask import Flask, jsonify, request, render_template
from collections import Counter

### HELPERS ###
def validate_word_count(text, words):
    cnt = Counter()
    for word in text.split():
        if word not in words:
            cnt[word] += 1
    return cnt

### APP ###
app = Flask(__name__)

@app.route("/")
def main():
    resp = {
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
        "words": ["ipsum", "dolor", "set"] }
    return jsonify(resp)

@app.route("/validate", methods=["POST"])
def validate():
    return "hello world"

@app.route('/admin')
def admin():
    return render_template("admin.html")

@app.route('/add', methods=["POST"])
def add():
    return "Data added!"

if __name__ == "__main__":
    app.run(debug=True)
