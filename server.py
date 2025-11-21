from flask import Flask, request, jsonify
import requests
import json

# Your Firebase Realtime Database URL (MUST END WITH .json)
FIREBASE_URL = "https://drivelock-e984e-default-rtdb.asia-southeast1.firebasedatabase.app/data.json"

app = Flask(__name__)

@app.route("/update", methods=["GET", "POST"])
def update():
    # 1. Get data from SIM900A
    if request.method == "GET":
        data = request.args.to_dict()   # For GET request
    else:
        try:
            data = request.get_json()   # For POST JSON
        except:
            data = {"error": "Invalid JSON"}

    # 2. Send data to Firebase using PATCH (update without deleting)
    try:
        fb_resp = requests.patch(
            FIREBASE_URL,
            data=json.dumps(data)
        )
        firebase_reply = fb_resp.json()
    except Exception as e:
        firebase_reply = {"error": str(e)}

    # 3. Respond back to SIM900A
    return jsonify({
        "received_from_sim900a": data,
        "firebase_response": firebase_reply
    })


# Simple test route
@app.route("/")
def home():
    return "SIM900A → Flask Server → Firebase OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
