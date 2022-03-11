import hashlib
import unittest

import  requests
from config import request_config
from tools.MD5_tools import md5_funtion_show
import demjson
# import random
# def produce_device_number():
#       constant=str('ZZGT01B0001T1N000')+str(random.randint(10,90))
#       return  constant
class TestAddUser(unittest.TestCase):
    def test_add_user_devices(self):
          url=request_config.host+request_config.add_user_devices_url
          header=request_config.worare_header
          data=demjson.encode(request_config.add_user_devices_data)
          print(data)
          requests_result=requests.post(url=url,data=data,headers=eval(header)).json()
          return requests_result
if __name__=="__main__":
    # op = md5_funtion_show(md5_value='ZZGT01B0001T1N00081'.encode('utf-8'))
    # op.MD5_function()
    unittest.main()