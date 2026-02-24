from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    mensaje = os.getenv("MENSAJE", "Mensaje por defecto")
    return mensaje

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
