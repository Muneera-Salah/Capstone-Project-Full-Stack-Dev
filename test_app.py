import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie, Cast

database_path = os.environ['DATABASE_URL']
# localhost
# database_name = "capstone_test"
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
            'age': '61'
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

    def test_create_new_movie(self):
        res = self.client().post('/moive', json=self.new_movie)
        data = json.loads(res.data)
        pass

    def test_create_new_actor(self):
        res = self.client().post('/actor', json=self.new_actor)
        data = json.loads(res.data)
        pass


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()