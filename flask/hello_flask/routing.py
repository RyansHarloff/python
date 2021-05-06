from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!' 

@app.route('/Dojo')
def success():
    return "Dojo"

@app.route('/say/<name>') 
def hello(name):
    print(name)
    return "Hi, " + name



if __name__=="__main__":
    app.run(debug=True)


