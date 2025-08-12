from flask import Flask, jsonify, send_from_directory
import random
import os

app = Flask(__name__)

# Serve index.html
@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

# Random Quote API
@app.route('/api/random-quote')
def random_quote():
    quotes = [
        "Keep pushing forward 🚀",
        "DevOps is a culture, not a role 💡",
        "Automate everything you can 🔧",
        "Small steps every day lead to big results 📈"
    ]
    return jsonify({"quote": random.choice(quotes)})

# Health Check API
@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "DevOps Flask App",
        "uptime": "OK"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

