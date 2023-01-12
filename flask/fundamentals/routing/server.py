from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say(name):
    return f"Hi, {name}!"

@app.route('/repeat/<int:times>/<string:message>')
def repeat_message(times, message):
    long_message = ''
    for x in range(times):
        long_message += f"<p>{message}</p>"
    return long_message

if __name__=="__main__":  
    app.run(debug=True)    
