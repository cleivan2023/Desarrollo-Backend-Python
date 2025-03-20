from flask import Flask #Flask es un microframeworkweb en Python que permite crear aplicaciones web de manera rápida y sencilla.

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenido a mi aplicación Flask!"

if __name__ == '__main__':
    app.run(debug=True)