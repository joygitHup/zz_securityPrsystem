import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
class sendEmai():
    @staticmethod
    def Sendemail(newfile):
        f=open(newfile,'rb')
        mail_body=f.read()
        f.close()
        smtpserver = 'smtp.exmail.qq.com'
        user = 'laixiangming@cloudeasetech.com'
        password = 'Laiyi823' #这里是密码 codingLaiyi823@
        sender="laixiangming@cloudeasetech.com"
        # xuli@mogul-tech.com
        receiver=["laixiangming@cloudeasetech.com"]
        subject='自动化测试报告'
        msg = MIMEMultipart('mixed')
        msg_html1 = MIMEText(mail_body,'html','utf-8')
        msg.attach(msg_html1)
        msg_html = MIMEText(mail_body,'html','utf-8')
        msg_html["Content-Disposition"] = 'attachment;filename="result.html"'
        msg.attach(msg_html)
        msg['From'] = 'laixiangming@cloudeasetech.com'
        msg['To'] = ";".join(receiver)
        msg['Subject'] = Header(subject,'utf-8')
        smtp = smtplib.SMTP_SSL(smtpserver,465)
        # smtp.connect(smtpserver,465)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()