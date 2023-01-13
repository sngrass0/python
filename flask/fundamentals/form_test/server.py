from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "this is the example secret keyyyy"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got POST info")
    # prints the request form as a immutable dictionary to terminal
    print(request.form)
    # set session to store the request
    session['username']  = request.form['name']
    session['username']  = request.form['name']
    # always return a redirect
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)