# app.py
from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')

    app.run()

# keepalive.py
import requests
import time
import random

while True:
    requests.get(f'https://investgition.onrender.com/?rand={random.randint(1000,9999)}')
    time.sleep(300)

    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)