import os
import configparser
con = configparser.ConfigParser()  # 实例化
config_ini_path=os.path.join(os.getcwd(),'config','caserun1.ini')
print(config_ini_path)
con.read(r'%s'%config_ini_path, encoding='utf-8')
print(con.sections())
class GetPath:
    """通过配置文件获取到指定文件夹下的相应用例"""
    def get_options(self, section):
        """
        通过get_options方法，拿到[case]下的'baidu', 'blog', 'news'
        :param section:
        :return:
        """
        # 通过section名，获取config文件中section名为[case]下的options，即'baidu', 'blog', 'news'
        options = con.options(section)
        # 可以看到打印出来为option拼接的一个list['baidu', 'blog', 'news']
        return options
    def get_case_path(self):
        """
        通过get_options方法，拿到[case]下的'baidu', 'blog', 'news'
        通过get_case_path方法，将[case]下，对应状态存储为1的取出来
        然后跟项目路径进行拼接，从而拼接出来一个路径list
        :return:
        """
        # 定义一个空list
        end_path = []
        # 然后我们拼接
        # 获取工程目录C:\Users\songlihui\PycharmProjects\temp20191015
        current_path = os.path.dirname(os.path.abspath(__file__))
        # 打印一下看一下是否正确
        print('current_path', current_path)
        # 开始拼接
        # 可以看到模块baidu，是在我们创建的工程temp20191015下的case下
        # 所以先循环取出'baidu', 'blog', 'news'
        options = GetPath().get_options('case')
        print('options', options)
        for option in options:
            value = con.getint('case', option)
            if value == 1:
                end_path.append(os.path.join(current_path, 'case', option))
        print(end_path)
        return end_path
if __name__ == '__main__':
    print( GetPath().get_options(section='cases'))
    # GetPath().get_case_path()