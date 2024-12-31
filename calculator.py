from flask import Flask, render_template, request
import math

app = Flask(__name__)

# Ruta para mostrar la interfaz
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar el formulario de la calculadora
@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form.get('expression', '')
    if expression:
        try:
            # Evaluar la expresión matemática
            result = eval(expression)
        except Exception as e:
            result = 'Error'
    else:
        result = ''

    return render_template('index.html', result=result, expression=expression)

if __name__ == '__main__':
    app.run(debug=True)