import unittest

import requests

from config import request_config

class TestShowAccount(unittest.TestCase):
    def test_admin_manger_show_account(self):
        '''管理员管理账号显示数据'''
        url=request_config.host+request_config.admin_manger_account_show_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result

if __name__=="__main__":
    unittest.main()
