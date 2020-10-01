from flask import Flask
#from flask_cors import CORS
from db.model import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:pass123@localhost:5432/EsteticaTest"
db.init_app(app)
#CORS(app, resources={r"/*": {"origins": "*"}})


if __name__ == "__main___":
    app.run(port=5000, debug=True)
