# PhoenixNode_ExecutionEngine.py

import json
import datetime
import subprocess
import os

# --- Config ---
DATA_FILE = "data.json"
GITHUB_REPO = "Phoenixnodeops/PhoenixNode-LiveTracker"
COMMIT_MESSAGE = "🔁 Auto-update: ExecutionEngine pushed new signal data"
GITHUB_TOKEN = "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"

# --- Simulated AI Signal Engine ---
def generate_data():
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    return {
        "timestamp": now,
        "deribit": {"momentum": "bullish"},
        "bridges": {"status": "elevated"},
        "wallets": {"activity": "spiking"},
        "deltaSignal": round(0.15, 2),
    }

# --- Update data.json ---
def update_json(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# --- Git Commands to Sync to GitHub ---
def push_to_github():
    try:
        # Set author identity once
        subprocess.run(["git", "config", "--global", "user.email", "trunks051630@protonmail.com"], check=True)
        subprocess.run(["git", "config", "--global", "user.name", "PhoenixNodeOps"], check=True)

        # Check if there are any changes
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not result.stdout.strip():
            print("📝 No changes to commit")
            return

        # Set remote with token
        remote_url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_REPO}.git"
        subprocess.run(["git", "remote", "set-url", "origin", remote_url], check=True)

        subprocess.run(["git", "add", DATA_FILE], check=True)
        subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], check=True)
        subprocess.run(["git", "push"], check=True)

        print("✅ Successfully pushed to GitHub")

    except subprocess.CalledProcessError as e:
        print(f"⚠️ Git operation failed: {e}")
        print("📝 Data file updated locally, but sync to GitHub failed")

# --- Full Execution ---
if __name__ == '__main__':
    data = generate_data()
    update_json(data)
    push_to_github()
    print("✅ PhoenixNode_ExecutionEngine updated and pushed.")
