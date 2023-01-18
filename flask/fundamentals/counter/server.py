from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "In the name of the moon I'll punish YOU"

@app.route('/')
def index():
    # keep track of count
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    # keep track of views
    if 'views' in session:
        session['views'] += 1
    else:
        session['views'] = 1
     # return rendered template with new count
    return render_template('index.html', count = session['count'], views = session['views'])

@app.route('/destroy_session')
def destroy_session():
    # clear all keys in session
    session.pop('count')
    return redirect('/')

@app.route('/add_2')
def add_2():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count']
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)