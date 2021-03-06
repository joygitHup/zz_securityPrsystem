import json
import requests
import unittest
from config import request_config
class TestLogin(unittest.TestCase):
    def test_login(self):
        host = request_config.host
        url = request_config.url
        data = request_config.data
        header = request_config.header
        result = requests.post(url=host + url, data=data, headers=eval(header)).json()
        print(result)
        return result['token']
if __name__ == "__main__":
    unittest.main()