from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello World'})

# Run Server
if __name__ == '__main__':
    app.run(debug=True)


