import os
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from models import setup_db
from sqlalchemy import exc
import json
from flask_cors import CORS

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  # CORS(app)
  cors = CORS(app, resources={r"*": {"origins": "*"}})
  # CORS Headers 
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
      return response

  @app.route('/', methods=['GET'])
  def index():
    return 'index'

  return app

app = create_app()

if __name__ == '__main__':
    app.run()