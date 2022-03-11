import  requests
import unittest
from config import request_config

class TestShowPerson(unittest.TestCase):
    def test_show_peple_list(self):
        url=request_config.host+request_config.pepole_manger_list_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result

if __name__=="__main__":
    pass