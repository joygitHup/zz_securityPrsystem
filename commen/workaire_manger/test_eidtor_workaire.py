import requests
import unittest
from config import request_config

class TestEidtorWorkArea(unittest.TestCase):
    def test_workare_eidtor(self):
        url=request_config.host+request_config.eidtor_url
        requesat_result=requests.options(url=url,headers=eval(request_config.worare_header)).json()
        return requesat_result

    def test_extra_url(self):
        url = request_config.host + request_config.eidtor_url_another
        requesat_result = requests.options(url=url, headers=eval(request_config.worare_header)).json()
        return requesat_result

    def test_eidtor_woreareinfor(self):
        url = request_config.host + request_config.eidtor_infor_after_url
        data=request_config.eidtor_infor_data
        requesat_result = requests.options(url=url, headers=eval(request_config.worare_header),data=data).json()
        return requesat_result
if __name__=="__main__":
    unittest.main()