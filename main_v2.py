# Importar Flask
from flask import Flask

# Usar el famework
app = Flask(__name__)

# Decoradores
@app.route('/')
def index():
    return "Hola Mundo Flask cambios nuevos"

@app.route('/hola')
def hola():
    return "Hola desde hola"

@app.route('/nueva')
def nueva():
    return "Hola desde Nueva"

# Indicar el nombre a partir del cual hará la ejecución la aplicación
if __name__ == "__main__":
    app.run(debug = True, port = 3000)