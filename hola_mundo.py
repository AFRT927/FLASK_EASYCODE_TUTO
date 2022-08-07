from flask import Flask

app = Flask(__name__)# nuevo objeto, recibe como parametro "el nombre de la app"

@app.route('/') # decorador para definir una ruta raiz
def index(): # funcion que se ejecuta al momento de que un usuario entre a la ruta raiz
    return 'Hola mundo'

app.run()# se encarga de ejecutar el servdor por default en el puerto 5000