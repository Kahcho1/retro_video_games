from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Games, Console
from datetime import datetime

test_game = {
                "id": 1,
                "name": "Final Fantasy VIII",
                "release_date": datetime(1999,2,11),
                "description": "Whatever",
                "console": []
            }

test_console = {

                "id": 1,
                "name": "N64",
                "release_date": datetime(1996,9,20)
                }

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app


    def setUp(self):
        db.create_all()
        db.session.add(Games(game_name="Test Name", date=datetime(1994,1,15), description="Run Test unit"))

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):

    def test_read_all_games(self):
        response = self.client.get(url_for('read_game'))
        all_games = { "games": test_game }
        self.assertEquals(all_games, response.json)
    
    def test_read_all_console(self):
        response = self.client.get(url_for('read_console'))
        all_console = { "console": test_console }
        self.assertEquals(all_console, response.data)
    
class TestCreate(TestBase):
    def test_add_game(self):
        response = self.client.post(
            url_for('add_game'),
            json={
                "name": "Final Fantasy VII",
                "description": "lets mosey", 
                "release_date": datetime(1997,1,31), 
                "console": []
                },
            follow_redirects=True
            )
        self.assertEquals(b"Add test game entry", response.data)
        self.assertEquals(Games.query.get(2).game_name, "Testing add games")

    def test_add_platform(self):
        response = self.client.post(
            url_for('add_platform'),
            json={
                "id": 2,
                "name": "Test Console",
                "release_date": datetime(1995,5,15)
                },
            follow_redirects=True
            )
        self.assertEquals(b"Add test console entry", response.data)
        self.assertEquals(Console.query.get(2).console_name, "Testing add console")




class TestDelete(TestBase):
    def test_delete_game(self):
        response = self.client.delete(url_for("delete_game", id=1))
        self.assertEquals(b"Delete game with ID 1", response.data)
        self.assertIsNone(Games.query.get(1))

    def test_delete_platform(self):
        response = self.client.delete(url_for("delete_platform", id=1))
        self.assertEquals(b"Delete console with ID 1", response.data)
        self.assertIsNone(Console.query.get(1))