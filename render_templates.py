from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index(name = 'Andres'):
    age = 17
    my_list = [1, 2, 3, 4]
    title = 'trabajando con macros'
    return render_template('index.html', name=name, age= age, list = my_list, title = title)

@app.route('/client')
def client():
    name_list = ['Andres', 'Oscar', 'Mauricio', 'Maria']
    return render_template('client.html', list = name_list)

if __name__ == '__main__':
    app.run(debug = True, port = 8000)