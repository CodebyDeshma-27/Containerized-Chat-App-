from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # allow frontend to access backend

messages = []

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Chat API is running", "endpoints": ["/messages", "/send"]})

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify(messages)

@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    user = data.get("user", "Anonymous")
    message = data.get("message", "")
    msg_obj = {"user": user, "message": message}
    messages.append(msg_obj)
    return jsonify({"status": "success", "message": msg_obj})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
