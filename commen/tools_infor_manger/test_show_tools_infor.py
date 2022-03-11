import requests
import unittest
from config import request_config

class TestShowTools(unittest.TestCase):
    def test_show_tools_infor(self):
        url=request_config.host+request_config.show_tools_infor_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return  requests_result


if __name__=="__main__":
    pass