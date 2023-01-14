from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "In the name of the moon I'll punish YOU"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def display_results():
    # name
    if request.form['name'] == "":
        session['name'] = "Guest"
    else:
        session['name'] = request.form['name']
    # location 
    session['location'] = request.form['location']
    # language
    session['language'] = request.form['language']
    # comment
    session['comment'] = request.form['comment']
    # os
    session['os'] = request.form['os']
    # render templaye
    return render_template('user.html', name = session['name'], 
    location = session['location'], language = session['language'], 
    comment = session['comment'], os = session['os'])

if __name__ == "__main__":
    app.run(debug=True)