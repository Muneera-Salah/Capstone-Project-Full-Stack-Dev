import os
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Actor, Movie, Cast
from sqlalchemy import exc
import json
from flask_cors import CORS
from auth import AuthError, requires_auth

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
  @requires_auth('get:actors')
  def get_actors(payload):
    try:
      query_results = Actor.query.all()
      if query_results is None:
          abort(404)
      else:    
        actors = [data.format() for data in query_results]
        return jsonify({
            'success':True,
            'actors': actors
        })
    except:
      abort(422)  

  @app.route('/movies', methods=['GET'])
  @requires_auth('get:movies')
  def get_movies(payload):
    try:
      query_results = Movie.query.all()
      if query_results is None:
          abort(404)
      else:        
        query_results = Movie.query.all()
        movies = [data.format() for data in query_results]
        return jsonify({
            'success':True,
            'movies': movies
        })
    except:
      abort(422)

  @app.route('/actor', methods=['POST'])
  @requires_auth('post:actor')
  def add_actor(payload):
    body = request.get_json()
    new_name = body.get('name', None)
    new_gender = body.get('gender', None)
    new_age= body.get('age', None)
    try:
      actor = Actor(name=new_name, gender=new_gender, age=new_age)
      actor.insert()
      body['id'] = Actor.id
      return jsonify({
          "success": True,
          "actor": actor.format()
          })
    except:
      abort(422)

  @app.route('/movie', methods=['POST'])
  @requires_auth('post:movie')
  def add_movie(payload):
    body = request.get_json()
    new_title = body.get('title', None)
    new_release_date = body.get('release_date', None)
    try:
        movie = Movie(title=new_title, release_date=new_release_date)
        movie.insert()
        body['id'] = Movie.id
        return jsonify({
            "success": True,
            "movie": movie.format()
            })
    except:
      abort(422)

  @app.route('/actors/<int:id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actor(payload,id):
    actor = Actor.query.filter(Actor.id == id).one_or_none()
    if actor is None:
      abort(404)

    body = request.get_json()
    new_name = body.get('name', None)
    new_gender = body.get('gender', None)
    new_age= body.get('age', None)
    
    actor.name = new_name
    actor.gender = new_gender
    actor.age= new_age

    try:
      actor.update()
      return jsonify({
          "success": True,
          "actor": actor.format()
          })
    except:
      abort(404)

  @app.route('/movies/<int:id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movie(payload,id):
    movie = Movie.query.filter(Movie.id == id).one_or_none()
    if movie is None:
      abort(404)

    body = request.get_json()
    new_title = body.get('title', None)
    new_release_date = body.get('release_date', None)
    
    movie.title = new_title
    movie.release_date = new_release_date

    try:
      movie.update()
      return jsonify({
          "success": True,
          "movie": movie.format()
          })
    except:
      abort(404)

  @app.route('/movies/<int:id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(payload,id): 
    try:
      movie = Movie.query.filter(Movie.id == id).one_or_none()
      if movie is None:
          abort(404)
      else:
          movie.delete()
          return jsonify({
              "success": True,
              "movie_id": id
          })
    except:
        abort(404)

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

  ''' 
  AuthError Handling
  '''        
  @app.errorhandler(AuthError)
  def auth_error(error):
      return jsonify(error.error), error.status_code

  return app

app = create_app()

if __name__ == '__main__':
    app.run()