import requests
import unittest
from config import request_config

class TestSearchTools(unittest.TestCase):
    def test_tools_infor_sercher(self):
        url=request_config.host+request_config.show_tools_sercher_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result


if __name__=="__main__":
    pass
