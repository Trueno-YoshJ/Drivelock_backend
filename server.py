import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

FIREBASE_URL = "https://drivelock-e984e-default-rtdb.asia-southeast1.firebasedatabase.app/data.json"

@app.route("/update", methods=["POST"])
def update():
    try:
        data = request.get_json(force=True)
        print("Received from SIM900A:", data)
        r = requests.post(FIREBASE_URL, json=data)
        print("Firebase response:", r.text)
        return jsonify({"status": "ok", "firebase": r.text})
    except Exception as e:
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)})

@app.route("/")
def index():
    return "Server is running!"

if __name__ == "__main__":
    # Read the port Render assigns
    port = int(os.environ.get("PORT", 10000))
    print(f"Starting server on port {port}")
    app.run(host="0.0.0.0", port=port)
