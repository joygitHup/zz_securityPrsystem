import requests
import unittest
from config import request_config

class TestSearchMatter(unittest.TestCase):
    def test_resouce_by_sercher(self):
        '''搜索物料信息'''
        url=request_config.host+request_config.resoucetype_sercher_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result
if __name__=="__main__":
    pass