# -*- coding: utf-8 -*-
import subprocess
import time
import sys
import os

print("Starting local HTTP server on port 8000...")
# Start python HTTP server
web_proc = subprocess.Popen(
    ["python3", "-m", "http.server", "8000"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

time.sleep(1)

print("Starting localtunnel on port 8000...")
# Run npx --yes localtunnel --port 8000
proc = subprocess.Popen(
    ["npx", "--yes", "localtunnel", "--port", "8000"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1
)

# Read stdout line by line
for line in proc.stdout:
    line_str = line.strip()
    print("LT:", line_str)
    if "url is:" in line_str:
        url = line_str.split("url is:")[-1].strip()
        with open("tunnel_url.txt", "w", encoding="utf-8") as f:
            f.write(url)
        print(f"\n==================================================")
        print(f"Server is running locally at: http://127.0.0.1:8000")
        print(f"Public tunnel URL: {url}")
        print(f"==================================================\n")
    sys.stdout.flush()

# If it exits
time.sleep(1)
if proc.poll() is not None:
    print(f"localtunnel exited with code {proc.returncode}")
    web_proc.terminate()
