import requests
import unittest
from config import request_config

class TestAddToolStype(unittest.TestCase):
    def test_add_toolstype(self):
        '''添加工具种类'''
        url=request_config.host+request_config.add_tools_type_url
        data=request_config.add_tools_type_data
        requests_result=requests.post(url=url,data=data.encode('utf-8'),headers=eval(request_config.worare_header)).json()
        return requests_result

if __name__=="__mian__":
    pass