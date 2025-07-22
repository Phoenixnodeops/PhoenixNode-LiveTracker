import subprocess
import time
import os

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

def auto_push():
    git_url = os.getenv("GIT_URL")
    if not git_url:
        print("❌ GIT_URL not found in secrets.")
        return

    run("git config --global user.name 'PhoenixNodeOps'")
    run("git config --global user.email 'trunks051630@protonmail.com'")
    run("git add .")
    run("git commit -m '🤖 Auto-push: New data update' || echo '⚠️ No changes to commit'")
    run(f"git push {git_url} HEAD:main --force")

    print("✅ Auto-push complete. Waiting 60 seconds...")

if __name__ == "__main__":
    while True:
        auto_push()
        time.sleep(60)