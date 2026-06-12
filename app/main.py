from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

PORT = int(os.getenv("PORT", "8080"))
HOSTNAME = socket.gethostname()

@app.route("/")
def home():
    return jsonify({
        "application": "simple-python",
        "status": "running",
        "hostname": HOSTNAME,
        "environment": "OpenShift"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/version")
def version():
    return jsonify({"version": "1.0.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
