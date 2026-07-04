import os
from flask import Flask, jsonify
from lightning_sdk import Studio

app = Flask(__name__)

STUDIO_NAME = os.environ.get("STUDIO_NAME")
TEAMSPACE = os.environ.get("TEAMSPACE", "default")
USERNAME = os.environ.get("USERNAME")

@app.route("/")
def index():
    return jsonify({"status": "running"})

@app.route("/wake")
def wake():
    try:
        print(f"Waking Studio: {STUDIO_NAME}")
        studio = Studio(name=STUDIO_NAME, teamspace=TEAMSPACE, user=USERNAME)
        studio.start()
        return jsonify({"status": "success", "message": "Studio started"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))