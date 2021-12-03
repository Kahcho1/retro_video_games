from flask import url_for
from flask_testing import TestCase
from application import app
from application.routes import backend_host
import requests_mock
from datetime import datetime

test_game = {
                "id": 1,
                "name": "whatever",
                "release_date": datetime(1991,1,11),
                "console": "PST",
                "description": "Test Test Test"
            }

test_console = {
                    "id": 1,
                    "name": "Test console",
                    "release_date": datetime(1992,2,22)
                }

class TestBase(TestCase):
    def create_app(self):

        app.config.update(
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

class TestViews(TestBase):
    def test_home_get(self):
        with requests_mock.Mocker() as m:
            all_games = {"games": [test_game]}
            m.get(f"http://{backend_host}/read/vgdb", json=all_games)
            response = self.client.get(url_for('home'))
            self.assert200(response)

    def test_home_console_get(self):
        with requests_mock.Mocker() as m:
            all_console = {"console": [test_console]}
            m.get(f"http://{backend_host}/read/cdb", json=all_console)
            response = self.client.get(url_for('home_console'))
            self.assert200(response)

    def test_add_get(self):
        response = self.client.get(url_for('add_game'))
        self.assert200(response)

    def test_add_console_get(self):
        response = self.client.get(url_for('add_platform'))
        self.assert200(response)




class TestRead(TestBase):

    def test_read_home_game(self):
        with requests_mock.Mocker() as m:
            all_games = {"games": [test_game]}
            m.get(f"http://{backend_host}/read/vgdb", json=all_games)
            response = self.client.get(url_for('home'))
            self.assertIn(b"Test Test Test", response.data)

    def test_read_home_console(self):
        with requests_mock.Mocker() as m:
            all_console = {"console": [test_console]}
            m.get(f"http://{backend_host}/read/cdb", json=all_console)
            response = self.client.get(url_for('home_console'))
            self.assertIn(b"Test console", response.data)

class TestCreate(TestBase):
    def test_add_game(self):
        with requests_mock.Mocker() as m:
            all_games = { "games":
                [
                    test_game,
                    {
                        "id": 2,
                        "name": "let's mosey",
                        "release_date": datetime(1992,2,22),
                        "console": "N10",
                        "description": "Test descrip"
                    }
                ]
            }
            m.post(f"http://{backend_host}/add/game", text="Testing add games")
            m.get(f"http://{backend_host}/read/cdb", json=all_games)
            response = self.client.post(
                url_for('add_game'),
                json={"name": "Testing Game Name"},
                follow_redirects=True
            )
            self.assertIn(b"Testing Game Name ", response.data)

    def test_add_console(self):
        with requests_mock.Mocker() as m:
            all_console = { "console":
                [
                    test_console,
                    {
                        "id": 2,
                        "name": "Test PSX",
                        "release_date": datetime(1996/2/22)
                    }
                ]
            }
            m.post(f"http://{backend_host}/add/platform", text="Testing add console")
            m.get(f"http://{backend_host}/read/cdb", json=all_console)
            response = self.client.post(
                url_for('add_platform'),
                json={"name": "Test PSX"},
                follow_redirects=True
            )
            self.assertIn(b"Test PSX", response.data)





class TestDelete(TestBase):
    def test_delete_games(self):
        with requests_mock.Mocker() as m:
            m.delete(f"http://{backend_host}/delete/game/1")
            m.get(f"http://{backend_host}/read/vgdb", json={ "games": [] })
            response = self.client.get(
                url_for("delete", id=1),
                follow_redirects=True
            )
            self.assertNotIn(b"Test Game Name", response.data)

    def test_delete_console(self):
        with requests_mock.Mocker() as m:
            m.delete(f"http://{backend_host}/delete/platform/1")
            m.get(f"http://{backend_host}/read/cdb", json={ "console": []})
            response = self.client.get(
                url_for("delete_platform", id=1),
                follow_redirects=True
            )
            self.assertNotIn(b"Test console Name", response.data)