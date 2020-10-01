from flask import Flask
from db.model import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pass123@localhost:5432/EsteticaTest"
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app
