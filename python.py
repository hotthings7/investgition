# app.py
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

if __name__ == '__main__':
    app.run()

# keepalive.py
import requests
import time
import random

while True:
    requests.get(f'https://your-render-app.onrender.com/?rand={random.randint(1000,9999)}')
    time.sleep(300)