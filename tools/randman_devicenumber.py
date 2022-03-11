import random
# class produce_activecode():
#     def __init__(self):
#         self.constant='ZZGT01B0001T1N000'
def produce_device_number():
      # 随机生成设备号
      constant=str('ZZGT01B0001T1N000')+str(random.randint(10,99))
      return  constant
if __name__=="__mian__":
    op=produce_device_number()
    print(op)