from flask import Flask, send_from_directory
import threading
import time
import requests
import os

app = Flask(__name__)

# Serve HTML files from static folder
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

# Keepalive endpoint
@app.route('/ping')
def ping():
    return "Alive", 200

# Background keepalive thread
def keepalive():
    while True:
        try:
            url = f"https://{os.environ.get('RENDER_EXTERNAL_HOSTNAME')}/ping" 
            requests.get(url, timeout=10)
            print("Keepalive ping sent")
        except Exception as e:
            print(f"Ping failed: {str(e)}")
        
        # Ping every 5 minutes (Render sleeps after 15)
        time.sleep(300)

# Start keepalive when app starts
if __name__ == "__main__":
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':  # Prevent duplicate threads
        thread = threading.Thread(target=keepalive)
        thread.daemon = True
        thread.start()
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)