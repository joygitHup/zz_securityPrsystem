import unittest

import requests

from config import request_config

class TestDeleteAccount(unittest.TestCase):
    def  test_delete_by_manger(self):
        '''管理员删除账号'''
        url=request_config.host+request_config.admin_manger_deleteaccount_url
        print(url)
        requests_result=requests.delete(url=url,headers=eval(request_config.worare_header))
        return  requests_result
if __name__=="__main__":
    unittest.main()