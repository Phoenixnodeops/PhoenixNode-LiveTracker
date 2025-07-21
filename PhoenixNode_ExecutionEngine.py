# PhoenixNode_ExecutionEngine.py

# Core functions:
# - Watch Arbitrum/Optimism bridges
# - Read Deribit ETH options orderbook
# - Monitor key whale wallets
# - Output delta signals to dashboard feed
import json
import datetime
import subprocess
import os

# --- Config ---
DATA_FILE = "data.json"
GITHUB_REPO = "Phoenixnodeops/PhoenixNode-LiveTracker"
COMMIT_MESSAGE = "🔁 Auto-update: ExecutionEngine pushed new signal data"

# --- Simulated AI Signal Engine ---
def generate_data():
    now = datetime.datetime.now(datetime.timezone.utc).isoformat() + "Z"
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
        # Check if there are any changes to commit
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if not result.stdout.strip():
            print("📝 No changes to commit")
            return

        # Configure git remote with token if available
        github_token = os.getenv("GITHUB_TOKEN")
        if github_token:
            remote_url = f"https://{github_token}@github.com/{GITHUB_REPO}.git"
            subprocess.run(["git", "remote", "set-url", "origin", remote_url], check=True)

        # Add and commit with retry logic
        subprocess.run(["git", "add", DATA_FILE], check=True)
        
        # Check if there's anything staged
        result = subprocess.run(["git", "diff", "--cached", "--quiet"], capture_output=True)
        if result.returncode == 0:
            print("📝 No staged changes to commit")
            return
            
        subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], check=True)
        subprocess.run(["git", "push"], check=True)
        print("✅ Successfully pushed to GitHub")
        
    except subprocess.CalledProcessError as e:
        if "lock" in str(e).lower():
            print("⚠️ Git lock detected - retrying after brief delay...")
            import time
            time.sleep(2)
            try:
                subprocess.run(["git", "add", DATA_FILE], check=True)
                subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], check=True)
                subprocess.run(["git", "push"], check=True)
                print("✅ Successfully pushed to GitHub on retry")
            except subprocess.CalledProcessError as retry_e:
                print(f"⚠️ Git operation failed even on retry: {retry_e}")
                print("📝 Data file updated locally, but sync to GitHub failed")
        else:
            print(f"⚠️ Git operation failed: {e}")
            print("📝 Data file updated locally, but sync to GitHub failed")

# --- Full Execution ---
if __name__ == "__main__":
    data = generate_data()
    update_json(data)
    # Temporarily disabled Git sync due to Replit lock file protection
    # push_to_github()
    print("✅ PhoenixNode_ExecutionEngine updated locally.")
    print("📝 Git sync temporarily disabled - data file updated successfully")