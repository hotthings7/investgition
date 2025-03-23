# keepalive.py
import requests
import time
import random

while True:
    requests.get(f'https://your-render-app.onrender.com/?rand={random.randint(1000,9999)}')
    time.sleep(300)