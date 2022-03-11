import unittest

import  requests

from config import request_config
class TestSearchPerson(unittest.TestCase):
    def test_sercher_pepole_by_name(self):
        url=request_config.host+request_config.pepole_manger_url
        requests_result=requests.options(url=url,headers=eval(request_config.worare_header)).json()
        return  requests_result
if __name__=="__main__":
    pass