import requests
import unittest


class TestAPI(unittest.TestCase):
    key = 'fruit.txt'
    value = 'orange'
    url = "http://127.0.0.1:5000"
    put_url = f'{url}/api/v1/add_data'
    get_url = f'{url}/api/v1/{key}'


    def test_put_data(self):
        """
        Check if response status code is 201 and 1 object returned
        """
        resp = requests.put(f'{TestAPI.put_url}/{TestAPI.key}/{TestAPI.value}')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(len(resp.json()), 1)

    def test_get_data(self):
        """
        Check if response status code is 200 and key: value pair returned
        """
        resp = requests.get(TestAPI.get_url)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json(), {f"{TestAPI.key}": f"{TestAPI.value}"})


if __name__ == '__main__':
    TestAPI().test_put_data()
    TestAPI().test_get_data()