from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    expression = ''
    
    if request.method == 'POST':
        # Recibir la expresión del formulario
        expression = request.form['expression']
        
        try:
            # Intentar evaluar la expresión matemática
            result = eval(expression)
            expression = str(result)
        except Exception as e:
            expression = 'Error'

    return render_template('index.html', expression=expression)

if __name__ == '__main__':
    app.run(debug=True)
