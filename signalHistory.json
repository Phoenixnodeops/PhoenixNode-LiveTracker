import json
import os
from datetime import datetime

DATA_FILE = "data.json"
HISTORY_FILE = "signalHistory.json"

def append_to_history():
    if not os.path.exists(DATA_FILE):
        print("❌ data.json not found")
        return

    with open(DATA_FILE, "r") as f:
        current_data = json.load(f)

    timestamp = current_data.get("timestamp", datetime.utcnow().isoformat())

    # Remove timestamp from the record and attach it to each entry
    signal_record = {}
    for asset, data in current_data.items():
        if asset == "timestamp":
            continue
        signal_record[asset] = {
            **data,
            "timestamp": timestamp
        }

    # Load or create history file
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append(signal_record)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

    print(f"📚 Logged {len(signal_record)} signals to history")

if __name__ == "__main__":
    append_to_history()
