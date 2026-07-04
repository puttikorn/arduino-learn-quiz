# -*- coding: utf-8 -*-
import subprocess
import time
import sys

print("Starting local HTTP server on port 8000...")
# Start python HTTP server
web_proc = subprocess.Popen(
    ["python3", "-m", "http.server", "8000"],
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)

time.sleep(1)

print("Starting SSH tunnel via localhost.run with auto-reconnect...")
ssh_command = ["ssh", "-o", "StrictHostKeyChecking=no", "-o", "ServerAliveInterval=30", "-o", "ServerAliveCountMax=3", "-R", "80:localhost:8000", "nokey@localhost.run"]

try:
    while True:
        proc = subprocess.Popen(
            ssh_command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Read stdout line by line
        for line in proc.stdout:
            line_str = line.strip()
            if "lhr.life" in line_str and "tunneled with tls" in line_str:
                parts = line_str.split("https://")
                if len(parts) > 1:
                    url = "https://" + parts[-1].strip()
                    with open("tunnel_url.txt", "w", encoding="utf-8") as f:
                        f.write(url)
                    print(f"\n==================================================")
                    print(f"Server is running locally at: http://127.0.0.1:8000")
                    print(f"Public tunnel URL: {url}")
                    print(f"==================================================\n")
            sys.stdout.flush()
        
        # If it exits, wait 5 seconds and retry
        proc.wait()
        print(f"SSH tunnel disconnected (exit code {proc.returncode}). Reconnecting in 5 seconds...")
        time.sleep(5)
except KeyboardInterrupt:
    print("Terminating server and tunnel...")
finally:
    web_proc.terminate()
