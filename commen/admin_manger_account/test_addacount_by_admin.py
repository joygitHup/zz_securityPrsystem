import json
import unittest
import demjson
import requests
from config import request_config
class TestAddCount(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.url = request_config.host+request_config.admin_manger_addcount_url
        self.header = eval(request_config.worare_header)
    '''case01:正确添加账号'''
    def test_addcount_by_admin(self):
        data=request_config.admin_manger_addcount_data
        print(data)
        requests_result=requests.post(url=self.url,data=data,headers=self.header).json()
        return requests_result
    '''case02:账号为空'''
    # def test_addcount02_by_admin(self):
    #     data=request_config.admin_manger_addcount02_data
    #     print(data)
    #     requests_result=requests.post(url=self.url,data=data,headers=self.header).json()
    #     return requests_result
    #
    # '''case03:账号已存在'''
    # def test_addcount03_by_admin(self):
    #     data=request_config.admin_manger_addcount03_data
    #     print(data)
    #     requests_result=requests.post(url=self.url,data=data,headers=self.header).json()
    #     return requests_result
    @classmethod
    def tearDownClass(self):
        print('test finnnshi!')


if __name__=="__main__":
    unittest.main()