from sqlalchemy import Column, String, Integer, Date, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

'''
Actor
Have name  ,age and gender
'''
class Actor(db.Model):  
  __tablename__ = 'Actor'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  age = Column(Integer)
  gender = Column(String)
  casts = db.relationship('Cast', backref='Actor', lazy=True)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def format(self):
    return {
      'id': self.id,
      'name': self.name,
      'gender': self.gender,
      'age': self.age
      }

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()
    
  def delete(self):
    db.session.delete(self)
    db.session.commit()
    
'''
Movie
Have name and release date
'''
class Movie(db.Model):  
  __tablename__ = 'Movie'

  id = Column(Integer, primary_key=True)
  title = Column(String)
  release_date = Column(Date)
  casts = db.relationship('Cast', backref='Movie', lazy=True)

  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release_date': self.release_date
      }

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()
    
  def delete(self):
    db.session.delete(self)
    db.session.commit()

'''
Cast
Have actor id and movie id
'''
class Cast(db.Model):  
  __tablename__ = 'Cast'

  id = Column(Integer, primary_key=True)
  movie_id = db.Column(db.Integer, db.ForeignKey('Movie.id'), nullable=False)
  actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id'), nullable=False)

  def __init__(self, movie_id, actor_id):
    self.movie_id = movie_id
    self.actor_id = actor_id

  def format(self):
    return {
      'id': self.id,
      'movie_id': self.movie_id,
      'actor_id': self.actor_id
      }

  def insert(self):
    db.session.add(self)
    db.session.commit()

  def update(self):
    db.session.commit()
    
  def delete(self):
    db.session.delete(self)
    db.session.commit()            