from dataclasses import dataclass
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
db = SQLAlchemy(app)

# configuring our database uri
# note an error here
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{username}:{password}@{server}/{database}".\
    format(username=os.getenv('MYSQL_USERNAME'), password=os.getenv('MYSQL_PASSWORD'), server=os.getenv('MYSQL_HOST'), database=os.getenv('MYSQL_DATABASE'))

# basic model
@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id: int
    email: str
    password: str

    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))


@app.route("/")
def hello():
    users = User.query.all()
    print(users)
    return jsonify(users)

if __name__ == "__main__":
    # users = User(email="user3@gmail.com", password="123456"), User(email="user4@gmail.com", password="123456")
    # db.create_all()
    # db.session.add_all(users)
    # db.session.commit()
    app.run(host='0.0.0.0', port=5000)
