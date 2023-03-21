from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xc2\x82\xb6q\xc0\x9f5\x8e\xf3\xe6)"\x88K\xc2_3^Q\x0f\x9f]'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flask_app.flaskblog import routes