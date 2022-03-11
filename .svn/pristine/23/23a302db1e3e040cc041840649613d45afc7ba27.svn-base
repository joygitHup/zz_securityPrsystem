import requests
import unittest
from config import request_config

class TestAddMatter(unittest.TestCase):
     def test_resoucetype_by_add(self):
          '''添加物料信息'''
          url=request_config.host+request_config.resoucetype_by_add_url
          data=request_config.resoucetype_by_add_data
          requests_result=requests.post(url=url,data=data.encode('utf-8'),headers=eval(request_config.worare_header)).json()
          return requests_result


if __name__=="__main__":
    pass