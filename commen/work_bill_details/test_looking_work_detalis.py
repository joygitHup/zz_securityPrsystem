import requests
import unittest
from config import request_config

class TestLookWorkDetails(unittest.TestCase):
    def test_looking_work_detalis(self):
        '''查看作业票详情'''
        url=request_config.host+request_config.looking_work_detalis_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result
if __name__=="__main__":
    pass