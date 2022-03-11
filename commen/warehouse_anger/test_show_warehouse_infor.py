import requests
import unittest
from config import request_config

class TestShowWarehouse(unittest.TestCase):
    def test_show_ware_infor(self):
        '''展示仓库信息'''
        url=request_config.host+request_config.warehouse_show_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result
if __name__=="__main__":
    pass