from flask import Flask
import psutil
import socket
import platform
import time

app = Flask(__name__)

@app.route("/")
def home():
    return {
        "message": "Server Monitor API Running"
    }

@app.route("/stats")
def stats():
    return {
        "hostname": socket.gethostname(),
        "system": platform.system(),
        "cpu_usage": psutil.cpu_percent(),
        "ram_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "boot_time": time.ctime(psutil.boot_time())
    }

app.run(host="0.0.0.0", port=5000)