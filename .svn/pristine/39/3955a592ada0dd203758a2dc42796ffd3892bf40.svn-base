import requests
import unittest
from config import request_config

class TestEditorToolStype(unittest.TestCase):
    def test_editor_tool_infor(self):
        '''编辑工具信息'''
        url=request_config.host+request_config.eidtor_tool_infor_url
        data=request_config.eidtor_tool_infor_data
        requests_result=requests.put(url=url,data=data.encode('utf-8'),headers=eval(request_config.worare_header)).json()
        return requests_result
if __name__=="__main__":
    pass