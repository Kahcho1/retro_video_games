from flask import Flask
import uuid # unique key

app = Flask(__name__)

app.config['SECRET_KEY'] = str(uuid.uuid4())

from application import routes
