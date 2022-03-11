import unittest

import requests

from config import request_config
class TestSearchDevice(unittest.TestCase):
    def test_serecher_by_device(self):
        url=request_config.host+request_config.device_secher_url
        header=request_config.worare_header
        requests_result=requests.get(url=url,headers=eval(header)).json()
        print(requests_result)
        return requests_result
if __name__=="__mian__":
    pass