import requests
import unittest
from config import request_config

class TestShowWorkDetailsRec(unittest.TestCase):
    def test_work_details_recover(self):
        '''现场复盘'''
        url=request_config.work_details_recover_host+request_config.work_details_recover_url
        data=request_config.work_details_recover_data
        requests_result=requests.post(url=url,data=data.encode('utf-8'),headers=eval(request_config.worare_header)).json()
        return  requests_result
if __name__=="__main__":
    if __name__ == '__main__':
        unittest()
