from flask import Flask, request


app = Flask(__name__)# nuevo objeto, recibe como parametro "el nombre de la app"

@app.route('/') # decorador para definir una ruta raiz
def index(): # funcion que se ejecuta al momento de que un usuario entre a la ruta raiz
    return 'Hola mundo cruel'

# se pueden obtener las diferentes partes de la ruta y usarlas como parametro
@app.route('/params/') # se ejecuta cuando no hay nada despues del slash
@app.route('/params/<name>/') # se ejecuta cuando hay algo despues del slash
@app.route('/params/<name>/<int:num>') # se ejecuta cuando hay algo despues del slash
def params(name = 'valor por default', num = 0): # si no hay nada despues del slash, la variable name toma el valor por defecto
    # forma 1 para obrener parametros de las rutas
    return 'los parametros son : {} , {}'.format(name, num)

if __name__ == '__main__':
    app.run(port= 8000, debug = True)# se encarga de lanzar el servdor por default en el puerto 5000