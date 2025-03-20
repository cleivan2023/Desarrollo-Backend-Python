"""  Objetivo: Configurar la estructura básica de la aplicación Flask y crear rutas 
principales con HTML estático para crear un sitio web de su grupo. 
1.
 Instale Flask. 
2. Cree una aplicación Flask con las rutas iniciales: 
1.
 2.
 /: Página de inicio con una bienvenida al sitio informativo. 
/about: Página "Acerca de", que contenga una breve descripción del grupo y 
los nombres de los integrantes. 
3. Cree un archivo app.py y una carpeta templates/con templates HTML para 
cada ruta (index.html y about.html). """

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)


#luego de running on http, ingresar/about para que aparescan los integrantes