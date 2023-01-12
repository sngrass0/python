from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def default():
    return render_template('index.html', x = 4, y = 4, color1 = 'green', color2 = 'beige')

@app.route('/<int:x>')
def board_x(x):
    return render_template('index.html', x = x, y = 4, color1 = 'green', color2 = 'beige')

@app.route('/<int:x>/<int:y>')
def board_x_y(x,y):
    return render_template('index.html', x = x, y = y, color1 = 'green', color2 = 'beige')

if __name__ == "__main__":
    app.run(debug=True)