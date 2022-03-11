import requests
import unittest
from config import request_config

class TestSearchWorkDetails(unittest.TestCase):
    def test_work_by_keyword_sercher(self):
        url=request_config.host+request_config.work_datails_by_secher_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result

if __name__=="__main__":
    pass
