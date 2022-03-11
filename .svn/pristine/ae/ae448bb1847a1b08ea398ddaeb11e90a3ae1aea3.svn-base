import  requests
import unittest
from config import request_config

class TestSiwchPerson(unittest.TestCase):
    def test_siwch_to_workAre(self):
        url=request_config.host+request_config.siwch_to_workAre_url
        requests_result=requests.get(url=url,headers=eval(request_config.worare_header)).json()
        return requests_result
if __name__=="__main__":
    pass