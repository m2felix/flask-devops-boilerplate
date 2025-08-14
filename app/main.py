from flask import Flask, jsonify, render_template
from datetime import datetime
import random
import psutil
import time

app = Flask(__name__)

# Simple in-memory metrics
request_count = 0
last_reset_time = time.time()

@app.before_request
def before_request_func():
    global request_count
    request_count += 1

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

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

@app.route('/api/system-stats')
def system_stats():
    global request_count, last_reset_time

    # CPU & Memory usage from psutil
    cpu_usage = psutil.cpu_percent(interval=0.2)
    memory_usage = psutil.virtual_memory().percent

    # Requests/sec calculation
    now = time.time()
    elapsed = now - last_reset_time
    requests_per_sec = request_count / elapsed if elapsed > 0 else 0

    # Reset every 10 seconds
    if elapsed >= 10:
        request_count = 0
        last_reset_time = now

    # Mock error and response time values
    errors = 0  # You could track real errors later
    response_time = round(random.uniform(80, 200), 2)  # ms

    return jsonify({
        "cpu": cpu_usage,
        "memory": memory_usage,
        "requests_sec": round(requests_per_sec, 2),
        "errors": errors,
        "response_time": response_time
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

