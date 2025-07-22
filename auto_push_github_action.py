import subprocess
import time

# GitHub token + repo setup
GITHUB_USER = "Phoenixnodeops"
GITHUB_TOKEN = "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"
REPO = "PhoenixNode-LiveTracker"
BRANCH = "main"
REPO_URL = f"https://{GITHUB_USER}:{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{REPO}.git"

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

def auto_push():
    while True:
        print("🔁 Checking for changes...")

        run("git config --global user.name 'PhoenixNodeOps'")
        run("git config --global user.email 'trunks051630@protonmail.com'")
        run(f"git remote set-url origin {REPO_URL}")
        run("git add .")
        run("git commit -m '🤖 Auto-push: New data update' || echo '⚠️ No changes to commit'")
        run("git push origin main --force")

        print("✅ Push complete. Sleeping 60s...")
        time.sleep(60)

if __name__ == "__main__":
    auto_push()