import requests
import unittest
from config import request_config

class TestShowWorkAccount(unittest.TestCase):
    def test_workaccount_show(self):
        '''工区管理账号信息显示'''
        url=request_config.host+request_config.admin_work_account_show_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result

if __name__=="__main__":
    pass