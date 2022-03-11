import requests

from config import request_config
import  unittest

class TestEidtorInforDevice(unittest.TestCase):
    '''编辑设备信息的接口测试'''
    def setUp(self):
        self.url = request_config.host + request_config.eidtor_infor_with_device_url
        self.herder = eval(request_config.worare_header)
    # def setUp(self):
    #     print('test begain')
    #     self.url=request_config.host + request_config.eidtor_infor_with_device_url
    #     self.herder=eval(request_config.worare_header)
    #     print('test over')

    def test_eidtor_infor_with_devicess(self):
        requests_result=requests.options(url=self.url,headers=self.herder).json()
        return requests_result
    def tearDown(self):
        print('test finnnshi!')
if __name__=="__main__":
    pass