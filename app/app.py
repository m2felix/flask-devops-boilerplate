from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "🚀 Hello from DevOps Flask App!"})

@app.route('/api/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "service": "DevOps Flask App",
        "uptime": "OK"
    })

@app.route('/api/time')
def current_time():
    now = datetime.utcnow()
    return jsonify({
        "current_time_utc": now.strftime("%Y-%m-%d %H:%M:%S UTC")
    })

# Keep your random quote endpoint if you already have it
@app.route('/api/random-quote')
def random_quote():
    import random
    quotes = [
        "The best way to get started is to quit talking and begin doing.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Don’t let yesterday take up too much of today."
    ]
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

