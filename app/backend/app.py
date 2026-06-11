from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "backend",
        "status": "running"
    })

@app.route("/api")
def api():
    return jsonify({
        "message": "Hello from Backend Service 🚀"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthyy"
    })

@app.route("/db")
def db():
    return jsonify({
        "database_host": os.getenv("DB_HOST"),
        "database_name": os.getenv("DB_NAME"),
        "status": "configured"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)