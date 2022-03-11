import requests
import unittest
from config import request_config

class TestShowWorkDetails(unittest.TestCase):
    def test_work_details(self):
         '''作业票显示'''
         url=request_config.host+request_config.work_detalis_show_url
         requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
         return requests_result

if __name__=="__main__":
    unittest.main()