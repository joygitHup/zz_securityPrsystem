import requests

from config import request_config


def test_add_warehouse_infor():
    url=request_config.host+request_config.add_warehouse_infor_url
    data=request_config.add_warehouse_infor_data
    requests_result=requests.post(url=url,data=data,headers=eval(request_config.worare_header)).json()
    return requests_result
if __name__=="__main__":
    print(test_add_warehouse_infor())