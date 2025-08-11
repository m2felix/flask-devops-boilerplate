from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# HTML landing page
@app.route("/")
def home():
    return render_template("index.html")

# Original API
@app.route("/api/message")
def api_message():
    return jsonify({"message": "🚀 Hello from DevOps Flask App!"})

# New random quote API
@app.route("/api/random-quote")
def random_quote():
    quotes = [
        "Code is like humor. When you have to explain it, it’s bad.",
        "In a world of bits and bytes, be the algorithm.",
        "Ship it. Then improve it."
    ]
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

