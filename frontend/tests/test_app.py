from flask import url_for
from flask_testing import TestCase
from application import app
from application.routes import backend_host
import requests_mock

test_game = {
                "id": 1,
                "names": "whatever",
                "release_date": 11/1/1991,
                "console": "PST",
                "description": "Test Test Test"
            }

test_console = {
                    "id": 1,
                    "names": "Test console",
                    "release_date": 22/2/1992
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
        response = self.client.get(url_for('add_game'))
        self.assert200(response)

