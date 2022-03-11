import requests
import unittest
from config import request_config

class TestEidtorWarehouse(unittest.TestCase):
    def test_eidtor_warehouse_infor(self):
        '''编辑工区信息'''
        url=request_config.host+request_config.eidtor_warehouse_infor_url
        data=request_config.eidtor_warehouse_infor_data
        requests_result=requests.put(url=url,data=data.encode('utf-8'),headers=eval(request_config.worare_header)).json()
        return requests_result

if __name__=="__main__":
    pass