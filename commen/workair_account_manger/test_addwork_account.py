import json
import unittest
import demjson
import requests

from config import request_config

class TestAddWorkAccount(unittest.TestCase):
    def test_addwork_account(self):
        '''添加工区账号'''
        url=request_config.host+request_config.add_workaccount_url
        data=json.loads(request_config.add_workaccount_data)
        requests_result=requests.post(url=url,data=data,headers=eval(request_config.worare_header)).json()
        return requests_result

if __name__=="__main__":
    unittest.main()