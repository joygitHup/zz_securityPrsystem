import requests
import unittest
from config import request_config

class TestShowToolStype(unittest.TestCase):
    def test_tools_show_infor(self):
        '''工具列表-信息展示'''
        url=request_config.host+request_config.tools_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return  requests_result


if __name__=="__main__":
    pass
