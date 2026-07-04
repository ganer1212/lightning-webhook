import os
from flask import Flask, jsonify
from lightning_sdk import Studio
import lightning_sdk

app = Flask(__name__)

STUDIO_NAME = os.environ.get("STUDIO_NAME")
TEAMSPACE = os.environ.get("TEAMSPACE", "default")
USER = os.environ.get("USER")
LIGHTNING_USER_ID = os.environ.get("LIGHTNING_USER_ID")
LIGHTNING_API_KEY = os.environ.get("LIGHTNING_API_KEY")

# Set Lightning credentials as environment variables for SDK to pick up
if LIGHTNING_USER_ID:
    os.environ["LIGHTNING_USER_ID"] = LIGHTNING_USER_ID
if LIGHTNING_API_KEY:
    os.environ["LIGHTNING_API_KEY"] = LIGHTNING_API_KEY

@app.route("/")
def index():
    return jsonify({"status": "running"})

@app.route("/wake")
def wake():
    try:
        print(f"Debug - STUDIO_NAME: {STUDIO_NAME}")
        print(f"Debug - TEAMSPACE: {TEAMSPACE}")
        print(f"Debug - USER: {USER}")
        print(f"Debug - LIGHTNING_USER_ID: {LIGHTNING_USER_ID}")
        print(f"Debug - LIGHTNING_API_KEY: {'SET' if LIGHTNING_API_KEY else 'NOT SET'}")
        
        if not STUDIO_NAME:
            return jsonify({"status": "error", "message": "STUDIO_NAME not set"}), 500
        
        studio = Studio(name=STUDIO_NAME, teamspace=TEAMSPACE, user=USER)
        studio.start()
        return jsonify({"status": "success", "message": "Studio started"})
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Error details: {error_details}")
        return jsonify({"status": "error", "message": str(e), "details": error_details}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))