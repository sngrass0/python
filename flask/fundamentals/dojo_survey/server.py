from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = "In the name of the moon I'll punish YOU"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def display_results():
    print(request.form.getlist('color'))
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
    # color
    session['colors'] =  request.form.getlist('color');
    # render template
    return render_template('user.html')

if __name__ == "__main__":
    app.run(debug=True)