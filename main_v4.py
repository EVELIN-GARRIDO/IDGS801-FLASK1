# Importar Flask
from flask import Flask, render_template

# Usar el famework
app = Flask(__name__)

# Decoradores
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')


# Indicar el nombre a partir del cual hará la ejecución la aplicación
if __name__ == "__main__":
    app.run(debug = True, port = 3000)