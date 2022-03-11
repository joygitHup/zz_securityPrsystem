import hashlib
import os
import sys

from tools.randman_devicenumber import produce_device_number

class md5_funtion_show:
   def __init__(self,md5_value):
     self.constant='660046874642CF00'.encode('utf-8')
     self.md5_value=md5_value
   def MD5_function(self):
     m=hashlib.md5()
     m.update(self.md5_value+self.constant)
     pas = m.hexdigest()
     return pas,bytes(self.md5_value).decode('utf-8')
if __name__=="__main__":
  op=md5_funtion_show(md5_value=produce_device_number().encode('utf-8'))
  print(op.MD5_function())
