from flask import Flask, request


app = Flask(__name__)# nuevo objeto, recibe como parametro "el nombre de la app"

@app.route('/') # decorador para definir una ruta raiz
def index(): # funcion que se ejecuta al momento de que un usuario entre a la ruta raiz
    return 'Hola mundo cruel'

@app.route('/params')
def params():
    # forma 1 para obrener parametros de las rutas 
                            # param name, message if param doesnt exist
    param = request.args.get('params1','no contiene este parametro')
    param_dos = request.args.get('params2','no contiene este parametro')
    return 'el parametro 1 es {} y el parametr_dos es {}'.format(param, param_dos)

if __name__ == '__main__':
    app.run(port= 8000, debug = True)# se encarga de lanzar el servdor por default en el puerto 5000