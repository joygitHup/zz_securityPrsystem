import requests
import unittest
from config import request_config

class TestAddTools(unittest.TestCase):
    def test_tools_infor_by_add(self):
        url=request_config.host+request_config.tools_infor_by_add_url
        data=request_config.tools_infor_by_add_data
        requests_result=requests.post(url=url,data=data.encode('utf-8'),headers=eval(request_config.worare_header)).json()
        return requests_result


if __name__=="__main__":
    pass