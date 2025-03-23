# app.py
from flask import Flask, send_file
import os
import requests
import time
import random

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')
while True:
    try:
        requests.get(f'https://investgition.onrender.com/?rand={random.randint(1000,9999)}')
        time.sleep(300)  # Ping every 5 mins
    except Exception as e:
        print("Ping failed:", e)



if __name__ == '__main__':
    # Get PORT from Render environment variable or default to 5000
    port = int(os.environ.get('PORT', 6000))
    # Bind to 0.0.0.0 to be externally visible on Render
    app.run(host='0.0.0.0', port=port)

