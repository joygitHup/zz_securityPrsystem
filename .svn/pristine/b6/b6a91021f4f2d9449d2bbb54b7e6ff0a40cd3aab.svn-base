import requests
import unittest
from config import request_config

class TestSearchWorkAccount(unittest.TestCase):
    def test_workaccount_by_sercher(self):
        url=request_config.host+request_config.admin_work_account_sercher_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return  requests_result

if __name__=="__masin__":
    pass
