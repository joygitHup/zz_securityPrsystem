import pytest
import requests
import unittest
from config import request_config
# import  allure
# @allure.step("操作步骤: 工区管理")
# @allure.feature("工区管理")
class TestShowWorkArea(unittest.TestCase):
     def test_workare_manger(self):
          url=request_config.host+request_config.worare_url
          header=request_config.worare_header
          request_result=requests.get(url=url,headers=eval(header)).json()
          return request_result

if __name__=="__main__":
    unittest.main()