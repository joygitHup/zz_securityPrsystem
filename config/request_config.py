from commen.login.test_logincase import TestLogin
from tools.MD5_tools import md5_funtion_show
from  tools.md5_userpassword import md5_funtion_password
from tools.randman_devicenumber import produce_device_number
from tools.randman_prduce_account import randum_pr_account_number
host='http://192.168.1.112:9090'
url='/zz/admin/authorizations/'
header='{"Content-Type":"application/json;charset=UTF-8"}'
# '''登录01用例'''
# username="admin",
# psw="25d55ad283aa400af464c76d713c07ad"
md5_funtion_password=md5_funtion_password(md5password='12345678'.encode('utf-8'))
data='{"username":"admin","password":"%s"}'%md5_funtion_password.MD5_password()[0]
testlogin=TestLogin()
header_Authorization='JWT '+testlogin.test_login()
# testlogin=TestLogin()
# header_Authorization='JWT '+testlogin.test_login01()
worare_url='/zz/admin/work_area/?page=1&page_size=10'
worare_header='{"Content-Type":"application/json;charset=UTF-8","Authorization":"%s"}'%header_Authorization
# 编辑工区名称
eidtor_url='/zz/admin/work_area/?parent_id=0'
eidtor_url_another='/zz/desktop/warehouse/warehouses/?parent_id=0'
# 提交数据
eidtor_infor_after_url='/zz/admin/work_area/3241/'
eidtor_infor_data='{"warehouse_ids":["0558d73a-f9ae-11eb-a0bb-38f9d3e52378"]}'
#人员管理
pepole_manger_list_url='/zz/admin/users/?is_device=false&page=1&page_size=10'
pepole_manger_url='/zz/admin/users/?fullname__icontains=%E5%91%A8%E5%81%A5&is_device=false&page=1&page_size=10'
#siwch_to_workAre
siwch_to_workAre_url='/zz/admin/users/?is_device=false&page=1&page_size=10&work_area_id=3261'
#设备管理
show_device_list_url='/zz/admin/users/?is_device=true&page=1&page_size=10'
eidtor_infor_with_device_url='/zz/admin/users/51ea6d06-00c8-11ec-b256-38f9d3e52378/'

#仓库管理
add_warehouse_infor_url='/zz/desktop/warehouse/warehouses/'
add_warehouse_infor_data='{"name":"test1","remark":"123456"}'

#编辑仓库信息
eidtor_warehouse_infor_url='/zz/desktop/warehouse/warehouses/38651228-f8bf-11eb-8bb9-38f9d3e52378/'
eidtor_warehouse_infor_data='{"name":"仓库12","remark":"teee"}'
#展示仓库信息
warehouse_show_url='/zz/desktop/warehouse/warehouses/?page=1&page_size=10&status=0'
#设备管理-添加设备
op = md5_funtion_show(md5_value=produce_device_number().encode('utf-8'))
# op = md5_funtion_show(md5_value='ZZGT01B0001T1N00081'.encode('utf-8'))
add_user_devices_url='/zz/desktop/user_devices/'
add_user_devices_data={"device_id":op.MD5_function()[1],"device_name": op.MD5_function()[1],"device_password":op.MD5_function()[0],"work_area_id": "3241"}
#通过设备搜索
device_secher_url='/zz/admin/users/?fullname__icontains=01&is_device=true&page=1&page_size=10'
#工具种类_信息展示
tools_url='/zz/desktop/warehouse/category/?page=1&page_size=10'
#工具种类_搜索
tools_sercher_url='/zz/desktop/warehouse/category/?page=1&page_size=10'
#工具种类_添加工具种类
add_tools_type_url='/zz/desktop/warehouse/tool/'
add_tools_type_data='{"category_id": "fe402b0f-9b68-11eb-959f-3fc01b7f3a38","name": "工具3","option": "3","quota": 0,"source_code": "3","status": 0,"unit": "1"}'
#工具种类_编辑工具种类
eidtor_tool_infor_url='/zz/desktop/warehouse/tool/0b4ad8cc-0975-11ec-9f36-38f9d3e52378/'
eidtor_tool_infor_data='{"category_id": "fe402b0f-9b68-11eb-959f-3fc01b7f3a38","name": "工具1","option": "1","quota": 0,"source_code": "1","status": 0,"unit": "个"}'
#物料种类-显示所有物料
resoucetype_show_url='/zz/desktop/warehouse/tool/?page=1&page_size=10&status=1'
#物料种类-搜索物料
resoucetype_sercher_url='/zz/desktop/warehouse/tool/?name=1&source_code=1&page=1&page_size=10&status=1'
#物料种类-添加物料信息
resoucetype_by_add_url='/zz/desktop/warehouse/tool/'
resoucetype_by_add_data='{"category_id": "0381e545-9b69-11eb-959f-3fc01b7f3a38","name": "物料2","option": "2","quota": 0,"source_code": "2","status": 1,"unit": "2"}'
#物料种类-编辑物料信息
resoucetype_by_eidtor_url='/zz/desktop/warehouse/tool/83c30a24-0975-11ec-b05e-38f9d3e52378/'
resoucetype_by_eidtor_data='{"category_id": "0381e545-9b69-11eb-959f-3fc01b7f3a38","name": "物料3","option": "/","quota": 0,"source_code": "3","status": 1,"unit": "米"}'
#作业票详情_展示作业票信息
work_detalis_show_url='/zz/api/inspection_sheets/?page=1&page_size=20'
#作业票详情_查看作业票
looking_work_detalis_url='/zz/api/inspection_sheets/13cbc94c-0194-11ec-86b7-38f9d3e52378/'
#作业票详情_现场复盘
work_details_recover_host='http://192.168.1.112:8087'
work_details_recover_url='/lbs/coordinate/findloclist'
work_details_recover_data='{"orderid": "13cbc94c-0194-11ec-86b7-38f9d3e52378","user_name": "全部"}'
#作业票详情_搜索
work_datails_by_secher_url='/zz/api/inspection_sheets/?page=1&page_size=20&max_time=2021-09-01&min_time=2021-08-31&keywords=41'
#管理员账号管理
admin_manger_account_show_url='/zz/admin/register/?type=1&page=1&page_size=10'
# 管理员账号管理-搜索
admin_manger_account_sercher_url='/zz/admin/register/?username=3&describe=%E4%B8%89&type=1&page=1&page_size=10'
#管理员账号
#case01:正确添加账号
randum_account=randum_pr_account_number()
admin_manger_addcount_url='/zz/api/grant_permission/'
admin_manger_addcount_data='{"username":"%s","password":"12345678","describe":"test by irven","work_area_ids":"","permission_ids":[2,3,7,11],"warehouse_ids":[],"type":1}'%randum_account
#case02:账号为空
admin_manger_addcount02_data='{"username":"","password":"12345678","describe":"test by irven","work_area_ids":"","permission_ids":[2,3,7,11],"warehouse_ids":[],"type":1}'
#case03:账号已存在
admin_manger_addcount03_data='{"username":"root","password":"12345678","describe":"test by irven","work_area_ids":"","permission_ids":[2,3,7,11],"warehouse_ids":[],"type":1}'
#case04:密码为空
#case05:密码与确认密码不一致
#case06:不勾选权限
#case07:只勾选一个权限
#case08:勾选全部权限

#管理员账号-编辑账号
admin_manger_eidtorcount_url='/zz/api/grant_permission/'
admin_manger_eidtorcount_data='{"describe": "123456","password": "123456789","permission_ids": [2],"type": 1,"user_id": 5037,"warehouse_ids": [],"work_area_ids": ""}'
#删除账号管理
admin_manger_deleteaccount_url='/zz/admin/user/5037/'
#工区账号管理-显示
admin_work_account_show_url='/zz/admin/register/?type=2&page=1&page_size=10'
#工区账号管理-搜索
admin_work_account_sercher_url='/zz/admin/register/?username=1&warehouse_id=5284f436-fe3f-11eb-8638-38f9d3e52378&describe=%E4%B8%80&type=2&page=1&page_size=10'
#工区账号管理-添加账号管理
add_workaccount_url='/zz/api/grant_permission/'
add_workaccount_data='{"describe": "123","password": "12345678","permission_ids": [1, 10, 11, 9],"type": 2,"username": "x11","warehouse_ids": ["c46b399e-f8bf-11eb-b2bf-38f9d3e52378"],"work_area_ids": "3261"}'
#工区账号管理-编辑账号
eidtor_workaccount_url='/zz/api/grant_permission/'
eidtor_workaccount_data='{"describe": "123456789","password": "123456789","permission_ids": [9],"type": 2,"user_id": 5030,"warehouse_ids": ["0558d73a-f9ae-11eb-a0bb-38f9d3e52378", "38651228-f8bf-11eb-8bb9-38f9d3e52378"],"work_area_ids": "3342,3343,5197"}'

#工具信息-显示
show_tools_infor_url='/zz/admin/tool_managers/?page=1&page_size=10&status=0'
#工具信息-搜索
show_tools_sercher_url='/zz/admin/tool_managers/?name=1&page=1&page_size=10&status=0'
#工具信息—添加工具信息
tools_infor_by_add_url='/zz/admin/tool_managers/'
tools_infor_by_add_data='{"category_id": "fe402b0f-9b68-11eb-959f-3fc01b7f3a38","label_id": "5","sku_id": "eaa5c756-e486-11eb-9f2a-005056af4428","state": 0,"tool_id": "eaa5c756-e486-11eb-9f2a-005056af4428","warehouse_id": "5284f436-fe3f-11eb-8638-38f9d3e52378"}'

#工具信息-编辑工具信息
tools_infor_by_eidtor_url='/zz/admin/tool_managers/3c531b9e-0a2b-11ec-9798-38f9d3e52378/'
tools_infor_by_eidtor_data='{"category_id": "fe402b0f-9b68-11eb-959f-3fc01b7f3a38","label_id": "2","sku_id": "eaa5c756-e486-11eb-9f2a-005056af4428","state": 0,"warehouse_id": "c46b399e-f8bf-11eb-b2bf-38f9d3e52378"}'
