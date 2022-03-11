import hashlib
class md5_funtion_password():
    def __init__(self,md5password):
        self.md5_password = md5password
    def MD5_password(self):
        '''对用户密码进行加密'''
        m = hashlib.md5()
        m.update(self.md5_password)
        pas = m.hexdigest()
        return pas, bytes(self.md5_password).decode('utf-8')
if __name__=="__main__":
    op=md5_funtion_password(md5password='12345678'.encode('utf-8'))
    print(op.MD5_password())
