import unittest

import  requests

from config import request_config

class TestShowDevice(unittest.TestCase):
    def test_show_device_list(self):
        url=request_config.host+request_config.show_device_list_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result
if __name__=="__main__":
    unittest.main()