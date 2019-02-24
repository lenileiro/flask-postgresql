import json
from ..base import BaseTest


class TestPostRequest(BaseTest):

    def test_account_creation(self):
        user = {
                "national_id": 32308961,
                "firstname": "john",
                "lastname": "Joe",
                "othername": "smith",
                "email": "johndoe@gmail.com",
                "isadmin": "False",
                "phone": "+254724862149",
                "password": "123456789",
                "passporturl": "https://demo.com/image.jpg"
            }
        response = self.client.post(
            '/api/v2/user/signup', data=json.dumps(user),
            content_type="application/json")

        result = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
