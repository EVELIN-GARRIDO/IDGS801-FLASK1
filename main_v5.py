# Importar Flask
from flask import Flask, render_template
from flask import request

# Usar el famework
app = Flask(__name__)

# Decoradores
@app.route('/calcular', methods = ['GET'])
def calcular():
    return render_template('calcular.html')

@app.route('/resultado', methods = ['POST'])
def resultado():
    n1 = request.form.get("txtNum1")
    n2 = request.form.get("txtNum2")
    res = int(n1) * int(n2)
    return render_template("resultado.html", n1 = n1, n2 = n2, res = res)


# Indicar el nombre a partir del cual hará la ejecución la aplicación
if __name__ == "__main__":
    app.run(debug = True, port = 3000)