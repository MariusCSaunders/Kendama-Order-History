from flask import url_for
from flask_testing import TestCase

from service_2.app import app, damas

class TestBase(TestCase):
    def create_app(self):
        return app


class TestResponse(TestBase):

    def test_get_dama(self):

        for i in range(20):
            response = self.client.get(url_for('get_dama'))
            self.assert200(response)
            self.assertIn(response.data.decode(), damas)