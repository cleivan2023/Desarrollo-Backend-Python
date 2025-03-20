from flask import Flask, render_template, redirect, url_for #Flask es un microframeworkweb en Python que permite crear aplicaciones web de manera rápida y sencilla. 

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('bienvenido'))

@app.route('/welcome')
def bienvenido():
    return render_template('home.html', nombre=' Juam')

if __name__ == '__main__':
    app.run(debug=True)

    
