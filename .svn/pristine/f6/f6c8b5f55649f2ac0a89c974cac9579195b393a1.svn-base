import requests
import unittest
from config import request_config

class TestEditorWorkAccount(unittest.TestCase):
    def test_work_account_by_editor(self):
        url=request_config.host+request_config.eidtor_workaccount_url
        data=request_config.eidtor_workaccount_data
        requests_result=requests.put(url=url,data=data.encode('utf-8'),headers=eval(request_config.worare_header)).json()
        return requests_result

if __name__=="__main__":
    pass