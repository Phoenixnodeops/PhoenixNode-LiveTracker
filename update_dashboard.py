import json
from datetime import datetime
import random

data = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "deribit": {"momentum": random.choice(["bullish", "bearish", "neutral"])},
    "bridges": {"status": random.choice(["stable", "spike", "drain"])},
    "wallets": {"activity": random.choice(["normal", "high", "anomalous"])},
    "deltaSignal": round(random.uniform(-0.05, 0.05), 4)
}

with open("PhoenixNode_DashboardFeed.json", "w") as f:
    json.dump(data, f, indent=2)
