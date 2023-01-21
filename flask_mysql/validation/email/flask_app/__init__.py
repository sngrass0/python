# __init__.py
from flask import Flask, flash
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "In the name of the moon I shall punish YOU!"

bcrypt = Bcrypt(app)   
