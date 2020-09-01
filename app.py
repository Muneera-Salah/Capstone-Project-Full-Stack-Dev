import os
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Actor, Movie
from sqlalchemy import exc
import json
from flask_cors import CORS

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  cors = CORS(app, resources={r"*": {"origins": "*"}})
  ''' 
  CORS Headers 
  '''
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
      response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
      return response
  ''' 
  Endpoints
  '''
  @app.route('/', methods=['GET'])
  def index():
    return 'index'
  
  @app.route('/actors', methods=['GET'])
  def get_actors():
    query_results = Actor.query.all()
    actors = [data.format() for data in query_results]
    return jsonify({
        'success':True,
        'actors': actors
    })

  @app.route('/movies', methods=['GET'])
  def get_movies():
    query_results = Movie.query.all()
    movies = [data.format() for data in query_results]
    return jsonify({
        'success':True,
        'movies': movies
    })
    
    
  ''' 
  Error Handling
  '''
  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
        "success": False, 
        "error": 422,
        "message": "unprocessable"
        }), 422

  @app.errorhandler(404)
  def not_found_error(error):
      return jsonify({
        "success": False, 
        "error": 404,
        "message": "resource not found"
        }), 404

  @app.errorhandler(500)
  def internal_server(error):
      return jsonify({
        "success": False, 
        "error": 500,
        "message": "internal server error"
        }), 500

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
        "success": False, 
        "error": 400,
        "message": "bad request"
        }), 400

  @app.errorhandler(405)
  def not_allowed(error):
      return jsonify({
        "success": False, 
        "error": 405,
        "message": "method not allowed"
        }), 405
        
  return app

app = create_app()

if __name__ == '__main__':
    app.run()