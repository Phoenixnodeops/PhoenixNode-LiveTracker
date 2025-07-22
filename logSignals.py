import json
import os
from datetime import datetime

LIVE_SIGNAL_FILE = "liveSignal.json"
HISTORY_FILE = "signalHistory.json"

def load_json_file(filepath, default):
    if os.path.exists(filepath):
        with open(filepath, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️ Warning: Could not decode {filepath}. Using default.")
    return default

def main():
    # Load current live signal
    current_signal = load_json_file(LIVE_SIGNAL_FILE, {})
    if not current_signal:
        print("❌ No current signal to log.")
        return

    # Load history
    history = load_json_file(HISTORY_FILE, [])

    # Prevent duplicate timestamp
    latest_timestamp = next(iter(current_signal.values()))["timestamp"]
    if any(latest_timestamp == next(iter(entry.values()))["timestamp"] for entry in history):
        print("🟡 Signal already logged. Skipping.")
        return

    # Append and save
    history.append(current_signal)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

    print("✅ Signal logged to history.")

if __name__ == "__main__":
    main()
