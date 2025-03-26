from flask import Flask, render_template, url_for, redirect, request, flash
import datetime

app = Flask(__name__)
app.secret_key = 'asdasfgfhgsdfdfg'

lista_dict = []

@app.route('/')
def home():
    return render_template("home.html", nombre="Al curso Flask")

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f"¡Bienvenido a {nombre}!"

@app.route('/hola')
def bienvenido():
    nombre = request.args.get('nombre', 'Pablo')
    return render_template("home.html", nombre=nombre)

@app.route('/about/')
def about():
    integrantes = ['alumno 1', 'alumno 2', 'alumno 3', 'alumno 4']
    datos = {'integrantes': integrantes, 'actualizacion': datetime.datetime.now(), 'cantidad': len(integrantes)}
    return render_template("about.html", datos=datos)

@app.route('/perfil')
def perfil():
    nombre = request.args.get('nombre', '-')
    edad = request.args.get('edad', '-')
    profesion = request.args.get('profesion', '-')
    datos = {'nombre': nombre, 'edad': edad, 'profesion': profesion, 'actualizacion': datetime.datetime.now()}
    return render_template("perfil.html", datos=datos)

@app.route('/anuncio', methods=['GET', 'POST'])
def anuncio():
    error = None
    datos = None

    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        contenido = request.form.get('contenido', '').strip()
        prioridad = request.form.get('prioridad', 'media')

        if not titulo:
            error = "Por favor, completa el título."
            flash(error)
        if not contenido:
            error = "Por favor, completa el contenido."
            flash(error)

        if titulo and contenido:
            flash("Gracias por tu anuncio.")
            datos = {"titulo": titulo, "contenido": contenido, "prioridad": prioridad}
            lista_dict.append(datos)

        return render_template("formulario.html", datos=datos, error=error)

    return render_template("formulario.html", datos=datos, error=error)

@app.route('/anuncios')
def anuncios():
    return render_template("anuncios.html", datos=lista_dict)

@app.route('/borrar_anuncios')
def borrar_anuncios():
    lista_dict.clear()
    return render_template("anuncios.html", datos=lista_dict)

if __name__ == '__main__':
    app.run(debug=True)















