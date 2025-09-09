from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running fine on Koyeb 🚀"

def start_web_server():
    thread = threading.Thread(
        target=lambda: app.run(
            host="0.0.0.0",
            port=8080,
            debug=False,
            use_reloader=False
        )
    )
    thread.daemon = True
    thread.start()
