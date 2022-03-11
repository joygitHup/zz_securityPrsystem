import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
# root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
# sys.path.append(root_path)
report_save_path=os.path.abspath(os.path.join(os.getcwd(), ".."))
report_path=report_save_path+'\\report'
log_path=report_save_path+'\\log'
alluredir_path=report_save_path+'\\target'

print(log_path)



