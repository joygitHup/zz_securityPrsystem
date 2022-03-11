import unittest

import requests

from config import request_config

class TestEidtorAccount(unittest.TestCase):
    def test_eidtor_account_by_admin(self):
        url=request_config.host+request_config.admin_manger_eidtorcount_url
        data=request_config.admin_manger_eidtorcount_data
        requests_result=requests.put(url=url,headers=eval(request_config.worare_header),data=data.encode('utf-8')).json()
        return requests_result

if __name__=="__main__":
    unittest.main()