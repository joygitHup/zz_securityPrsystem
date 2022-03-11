import unittest

import requests

from config import request_config

class TestSearchAccount(unittest.TestCase):
    def test_admin_manger_account_sercher(self):
        url=request_config.host+request_config.admin_manger_account_sercher_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result
if __name__=="__main__":
    unittest.main()
