import requests
import unittest
from config import request_config

class TestAddWarehouse(unittest.TestCase):
    def test_add_warehouse_infor(self):
        url=request_config.host+request_config.add_warehouse_infor_url
        data=request_config.add_warehouse_infor_data
        requests_result=requests.post(url=url,data=data,headers=eval(request_config.worare_header)).json()
        return requests_result
if __name__=="__main__":
    pass