from flask import Flask, jsonify
import socket
import platform
import datetime
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "CI/CD Pipeline Working Successfully",
        "status": "healthy",
        "application": "Flask CI/CD Demo"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "UP",
        "timestamp": str(datetime.datetime.now())
    })

@app.route('/system')
def system():
    return jsonify({
        "hostname": socket.gethostname(),
        "platform": platform.system(),
        "python_version": platform.python_version()
    })

@app.route('/version')
def version():
    return jsonify({
        "application": "Flask CI/CD Demo",
        "version": "1.0.0"
    })

@app.route('/env')
def env():
    return jsonify({
        "environment": os.getenv("ENVIRONMENT", "development")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)