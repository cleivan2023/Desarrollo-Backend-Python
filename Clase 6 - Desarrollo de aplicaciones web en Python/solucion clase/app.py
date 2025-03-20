"""SOLUCION EN CLASES DE LOS EJERCICIOS 
Bloque A - Ejercicio 1

Configuración inicial y rutas básicas
Objetivo: Configurar la estructura básica de la aplicación Flask y crear rutas principales con HTML estático.
Instale Flask.
Cree una aplicación Flask con las rutas iniciales:
/ Página de inicio con una bienvenida al sitio informativo.
/about: Página "Acerca de", que contenga una breve descripción del grupo y los nombres de los integrantes.
Cree un archivo app.py y una carpeta templates/ con templates HTML para cada ruta (index.html y about.html)."""

from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')


# Ruta para la página "Acerca de"
@app.route('/about')
def about():
    group = {
        'name': "Grupo de Desarrollo Web",
        'description': "Nuestro objetivo es aprender los fundamentos de desarrollo backend con Flask.",
        'members': ["Ana", "José", "Luis", "Carla"],
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    return render_template('about.html', group=group)


if __name__ == '__main__':
    app.run(debug=True)