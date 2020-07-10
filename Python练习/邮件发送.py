# 参考文章：https://blog.csdn.net/qq_20417499/article/details/80566265
# 参考文章：https://www.jianshu.com/p/5d0330d4dd37
import smtplib  # 发送的库
from email.mime.text import MIMEText #邮件正文的库
from email.mime.multipart import MIMEMultipart  #组装邮件内容的库
from email.mime.application import MIMEApplication  #添加附件的库
# 邮件的基本配置变量
mail_host = "smtp.exmail.qq.com"   # SMTP服务器
mail_user = "xuweijun@peilian.com"   # 用户名
mail_pwd = "**********"   #16位授权密码
to_addr = 'kidmagic@126.com' # 收件人邮箱
mail_port = 465  # SSL默认是465
# 创建正文内容
content = 'Hello,This is my Python test mail.'
textApart = MIMEText(content)
# 创建附件内容
excelfile = 'AAA.xlsx'
excelApart = MIMEApplication(open('/Users/xuweijun/Downloads/stu02.xlsx', 'rb').read())
excelApart.add_header('Content-Disposition', 'attachment', filename=excelfile)
# 将邮件内容组装起来
m = MIMEMultipart()       #创建邮件内容主体
m.attach(textApart)       #添加文件正文
m.attach(excelApart)      #添加邮件附件
m['Subject'] = '邮件测试'   #添加邮件标题
# 使用smtplib.SMTIP_SSL 发送邮件
server = smtplib.SMTP_SSL(host='smtp.exmail.qq.com', port=465)     # 要用SSL
# server.set_debuglevel(1)                   # 打印和SMTP服务器交互的所有信息
server.login(mail_user, mail_pwd)          # 登录SMTP服务器（用户名和授权密码）
server.sendmail(mail_user, to_addr, m.as_string())   #发邮件（发件人、收件人、邮件内容） 注意要as_string
server.quit()
