import os
from flask import Flask, jsonify
from lightning_sdk import Studio

app = Flask(__name__)

STUDIO_NAME = os.environ.get("STUDIO_NAME")
TEAMSPACE = os.environ.get("TEAMSPACE", "default")
ORG = os.environ.get("ORG")

@app.route("/")
def index():
    return jsonify({"status": "running"})

@app.route("/wake")
def wake():
    try:
        print(f"Debug - STUDIO_NAME: {STUDIO_NAME}")
        print(f"Debug - TEAMSPACE: {TEAMSPACE}")
        print(f"Debug - ORG: {ORG}")
        
        if not STUDIO_NAME:
            return jsonify({"status": "error", "message": "STUDIO_NAME not set"}), 500
        
        studio = Studio(name=STUDIO_NAME, teamspace=TEAMSPACE, org=ORG)
        studio.start()
        return jsonify({"status": "success", "message": "Studio started"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))