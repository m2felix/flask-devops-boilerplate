from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

# Serve the main HTML page
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint for a random quote
@app.route('/api/random-quote')
def random_quote():
    quotes = [
        "The best way to get started is to quit talking and begin doing.",
        "Success is not in what you have, but who you are.",
        "Your time is limited, so don’t waste it living someone else’s life.",
        "The harder you work for something, the greater you’ll feel when you achieve it.",
        "Don’t watch the clock; do what it does. Keep going."
    ]
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

