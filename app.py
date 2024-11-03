from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal para mostrar el formulario
@app.route('/')
def index():
    return render_template("index.html")

# Ruta para procesar el formulario
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Obtenemos los datos del formulario (las horas trabajadas por día)
        monday = float(request.form['monday'])
        tuesday = float(request.form['tuesday'])
        wednesday = float(request.form['wednesday'])
        thursday = float(request.form['thursday'])
        friday = float(request.form['friday'])
        saturday = float(request.form['saturday'])
        sunday = float(request.form['sunday'])

        # Calculamos el total de horas trabajadas
        total_hours = monday + tuesday + wednesday + thursday + friday + saturday + sunday

        # Retornamos el resultado
        return render_template('index.html', total_hours=total_hours)

    except ValueError:
        return render_template('index.html', error="Por favor ingrese valores válidos.")

if __name__ == '__main__':
    app.run(debug=True)
