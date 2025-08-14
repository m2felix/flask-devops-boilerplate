from flask import Flask, jsonify, render_template
from datetime import datetime
import random, psutil

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@app.route('/api/system-stats')
def system_stats():
    return jsonify({
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "requests_sec": random.randint(10, 50),  # Simulated
        "errors": random.randint(0, 2),          # Simulated
        "response_time": f"{random.randint(80, 200)} ms"
    })

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

@app.route('/api/random-quote')
def random_quote():
    quotes = [
        "The best way to get started is to quit talking and begin doing.",
        "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "Don’t let yesterday take up too much of today."
    ]
    return jsonify({"quote": random.choice(quotes)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

