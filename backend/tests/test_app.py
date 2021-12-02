from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Tasks

test_game = {
                "id": 1,
                "name": "Final Fantasy VIII",
                "release_date": 11/2/1999,
                "description": "Whatever",
                "console": []
            }

test_console = {

                "id": 1,
                "name": "N64",
                "release_date": 26/9/1996
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
        db.session.add(Games(name="Test Name", release_date=15/1/1994, description="Run Test unit", console=[]))
        db.session.commit

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestRead(TestBase):

    def test_read_all_games(self):
        response = self.client.get(url_for('read_vgdb'))
        all_games = { "games": {test_game} }
        self.assertEquals(all_games, response.json)
    
    def test_read_tasks_dict(self):
        response = self.client.get(url_for('read_cdb'))
        all_console = { "console": {test_console} }
        self.assertEquals(all_console, response.data)
    
class TestCreate(TestBase):
    def test_add_game(self):
        response = self.client.post(
            url_for('add_platform'),
            json={
                "name": "Final Fantasy VII",
                "description": "lets mosey", 
                "release_date": 31/1/1997, 
                "consoles_id": 2
                },
            follow_redirects=True
            )
        self.assertEqual(b"Add test game entry", response.data)
        self.assertEqual(Games.query.get(2).name, "Testing add games")

    def test_add_platform(self):
        response = self.client.post(
            url_for('create_task'),
            data={"desc": "Testing create task"},
            follow_redirects=True
            )
        self.assertEqual(b"Add test game entry", response.data)
        self.assertEqual(Console.query.get(2).name, "Testing add games")

class TestUpdate(TestBase):
    def test_update_task(self):
        response = self.client.post(
            url_for('update_task', id=1),
            data={"desc": "Testing update task"},
            follow_redirects=True
            )
        self.assertIn(b"Testing update task", response.data)

class TestDelete(TestBase):
    def test_delete_task(self):
        response = self.client.get(
            url_for("delete", id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Run unit tests", response.data) # NotIn meaning deleted

class TestComp(TestBase):
    def test_comp_task(self):
        response = self.client.get(
            url_for("status", id=1),
            follow_redirects=True
        )
        self.assertEqual(Tasks.query.get(1).comp, True)

class TestIncomp(TestBase):
    def test_Incomp_task(self):
        response = self.client.get(
            url_for("status_incomp", id=1),
            follow_redirects=True
        )
        self.assertEqual(Tasks.query.get(1).comp, False)
