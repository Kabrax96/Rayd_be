# comment
from flask import render_template
import config
from models import User

# asingando Flask a una variable (__name__)
# El siguiente paso es crear la entidad de aplicación empleando Connexion en lugar de Flask
# indica a Connexion en qué directorio debe buscar su archivo de configuración
app = config.connex_app
# connexion.App(__name__, specification_dir="./") # Remove: import Flask
# Provee la conexion con swagger.yml
app.add_api(config.basedir / "swagger.yml")

# Asignado una ruta a Flask


@app.route("/")
# Definiendo una funcion (home)
# Renderisa una variable a render_tamplate de Home.htlm
def home():
    people = User.query.all()
    return render_template("home.html/", people=people)


# Condicional donde si la variable __name__ es igual a "__main__"
# Entonces app corre la condicion entre parentiesis
# print('')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

print('app.py')
