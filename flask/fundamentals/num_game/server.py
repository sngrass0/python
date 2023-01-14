from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = "In the name of the moon I'll punish YOU"

@app.route('/')
def index():
    if 'secret_num' not in session:
        session['secret_num'] = random.randint(1, 100) 
    return render_template('index.html')

@app.route('/check', methods=["POST"])
def check_guess():
    if request.form['guess'] != "":
        session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset_game():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)