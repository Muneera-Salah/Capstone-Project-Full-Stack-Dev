import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie, Cast

database_path = os.environ['DATABASE_URL']
# localhost
# database_name = "capstone"
# database_path = "postgres://{}:{}@{}/{}".format('postgres', 'postgres','localhost:5432', database_name)


class CapstoneTestCase(unittest.TestCase):
    """This class represents the Capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        setup_db(self.app, self.database_path)

        self.new_movie = {
            'title': 'Toy Story',
            'release_date': '1995-1-1'
        }
        
        self.new_actor = {
            'name': 'Tom Hanks',
            'gender': 'male',
            'age': 61
        }     
        
        self.new_actor_missing_name = {
            'gender': 'male',
            'age': 61
        }

        self.new_moive_missing_name = {
            'release_date': '1995-1-1'
        }

        self.update_actor_data = {
            'name': 'Tom Hanks',
            'gender': 'male',
            'age': 60
        }     
        
        self.update_moive_data = {
            'title': 'Toy Story2',
            'release_date': '2020-1-1'
        }     

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    '''
    GET
    /actors route
    '''
    def test_get_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
    '''
    GET
    /movies route
    '''
    def test_get_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
    '''
    POST
    /actor route
    '''
    def test_create_new_actor(self):
        res = self.client().post('/actor', json=self.new_actor)
        data = json.loads(res.data)
        pass

    def test_422_if_actor_creation_fails(self):
        res = self.client().post('/actor', json=self.new_actor_missing_name)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    '''
    POST
    /moive route
    '''
    def test_create_new_movie(self):
        res = self.client().post('/moive', json=self.new_movie)
        data = json.loads(res.data)
        pass

    def test_422_if_moive_creation_fails(self):
        res = self.client().post('/moive', json=self.new_moive_missing_name)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    '''
    PATCH
    /actors/<int:id> route
    '''
    def test_update_actor(self):
        res = self.client().patch('/actors/1', json=self.update_actor_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actor'])

    def test_404_if_update_actor_fails(self):
        res = self.client().patch('/actors/5000', json=self.update_actor_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    '''
    PATCH
    /movies/<int:id> route
    '''
    def test_update_movie(self):
        res = self.client().patch('/movies/1', json=self.update_moive_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movie'])

    def test_404_if_update_movie_fails(self):
        res = self.client().patch('/movies/5000', json=self.update_moive_data)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    '''
    DELETE
    /movies/<int:id> route
    '''
    def test_detete_moive(self):
        res = self.client().delete('/movies/1')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['moive_id'])

    def test_404_if_detete_moive_fails(self):
        res = self.client().delete('/movies/5000')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()