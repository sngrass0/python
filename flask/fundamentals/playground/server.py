from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<p>for this assignment please go to <a href='/play'>/play</a></p>"

@app.route('/play')
def play():
    return render_template('index.html', times = 3, color = 'royalblue')

@app.route('/play/<int:x>')
def play_x(x):
    return render_template('index.html', times = x, color = 'royalblue')

@app.route('/play/<int:x>/<string:color>')
def play_color(x, color):
    return render_template('index.html', times = x, color = color)

if __name__ == "__main__":
    app.run(debug=True)
