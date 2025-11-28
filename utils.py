# Utility functions — JRAVIS Business Brain

import requests
import json

BACKEND_URL = "https://jravis-backend.onrender.com/task/new"

def send_task(task):
    try:
        res = requests.post(BACKEND_URL, json=task)
        print("➡️ Sent Task:", json.dumps(task))
        print("⬅️ Backend Response:", res.text)
    except Exception as e:
        print("❌ Task Send Error:", str(e))
