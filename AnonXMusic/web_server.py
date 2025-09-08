from flask import Flask
import threading

flask_app = Flask('')

@flask_app.route('/')
def home():
    return "AnonXMusic Bot is alive!"

def run_web():
    flask_app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = threading.Thread(target=run_web)
    t.daemon = True
    t.start()
