from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Games, Console

test_game = {
                "id": 1,
                "game_name": "Final Fantasy VIII",
                "date": 11/2/1999,
                "description": "Whatever",
                "console": []
            }

test_console = {

                "id": 1,
                "console_name": "N64",
                "date": 26/9/1996
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
        db.session.add(Games(game_name="Test Name", date=15/1/1994, description="Run Test unit"))

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):

    def test_read_all_games(self):
        response = self.client.get(url_for('read_vgdb'))
        all_games = { "games": {test_game} }
        self.assertEquals(all_games, response.json)
    
    def test_read_all_console(self):
        response = self.client.get(url_for('read_cdb'))
        all_console = { "console": {test_console} }
        self.assertEquals(all_console, response.data)
    
class TestCreate(TestBase):
    def test_add_game(self):
        response = self.client.post(
            url_for('add_game'),
            json={
                "game_name": "Final Fantasy VII",
                "description": "lets mosey", 
                "date": 31/1/1997, 
                "consoles_id": 2
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
                "console_name": "Test Console",
                "date": 15/5/1995
                },
            follow_redirects=True
            )
        self.assertEquals(b"Add test console entry", response.data)
        self.assertEquals(Console.query.get(2).console_name, "Testing add console")

# class TestUpdate(TestBase):
#     def test_update_game(self):
#         response = self.client.put(
#             url_for('update_game', id=1),
#             json={"name": "Testing update game"},
#         )
#         self.assertEquals(b"Game name with ID 1 has been changed to: Testing update game", response.data)
#         self.assertEqual(Console.query.get(1).name, "Testing update game")

#     def test_update_platform(self):
#         response = self.client.put(
#             url_for('update_platform', id=1),
#             json={"name": "Testing update console"},
#         )
#         self.assertEquals(b"Console name with ID 1 has been changed to: Testing update console", response.data)
#         self.assertEqual(Console.query.get(1).name, "Testing update console")

class TestDelete(TestBase):
    def test_delete_game(self):
        response = self.client.delete(url_for("delete_game", id=1))
        self.assertEquals(b"Delete game with ID 1", response.data)
        self.assertIsNone(Games.query.get(1))

    def test_delete_platform(self):
        response = self.client.delete(url_for("delete_platform", id=1))
        self.assertEquals(b"Delete console with ID 1", response.data)
        self.assertIsNone(Console.query.get(1))