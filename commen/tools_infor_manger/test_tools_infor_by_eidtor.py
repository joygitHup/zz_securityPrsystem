import requests
import unittest
from config import request_config

class TestEidtorTools(unittest.TestCase):
    def test_eidtor_tools_infor(self):
        url=request_config.host+request_config.tools_infor_by_eidtor_url
        data=request_config.tools_infor_by_eidtor_data
        requests_result=requests.patch(url=url,headers=eval(request_config.worare_header),data=data.encode('utf-8')).json()
        return requests_result

if __name__=="__main__":
    pass