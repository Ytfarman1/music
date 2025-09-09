from flask import Flask
import threading
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running fine on Koyeb 🚀"

def start_web_server():
    app.run(host="0.0.0.0", port=8080)
def keep_alive():
    t = threading.Thread(target=run_web)
    t.daemon = True
    t.start()
