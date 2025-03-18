#!/usr/bin/env python3
import time
import subprocess
from flask import Flask, Response, send_from_directory

app = Flask(__name__, static_folder='static')

def get_cpu_usage():
    result = subprocess.run(
        ["mpstat", "1", "1"], 
        capture_output=True, 
        text=True
    )
    for line in result.stdout.split("\n"):
        if "all" in line:
            parts = line.split()
            idle_str = parts[-1].replace(',', '.')
            idle = float(idle_str)  
            return round(100 - idle, 2)
    return 0

def generate():
    while True:
        cpu = get_cpu_usage()
        yield f"data: {cpu}\n\n"
        time.sleep(1)

@app.route('/cpu-monitor')
def stream():
    return Response(generate(), mimetype='text/event-stream')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)