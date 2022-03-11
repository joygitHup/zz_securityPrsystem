import requests
import unittest
from config import request_config

class TestSearchToolStype(unittest.TestCase):
    def test_sercher_tools_by(self):
        '''工具种类的搜索'''
        url=request_config.host+request_config.tools_sercher_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result
if __name__=="__main__":
    pass