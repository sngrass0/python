from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "In the name of the moon I shall punish YOU!"

bcrypt = Bcrypt(app)