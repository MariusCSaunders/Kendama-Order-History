from flask import url_for
from flask_testing import TestCase

from service_4.app import app, prices

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_get_dama(self):

        for dama in prices['damas']:
            for accessory in prices['accessories']:
                result = {'damas':dama, 'accessories': accessory}
                response = self.client.post(url_for('post_order'), json=result)
                self.assert200(response)
                total_price = prices['damas'][dama] + prices['accessories'][accessory] + 3.50
                self.assertEqual(response.json, round(total_price, 2))
