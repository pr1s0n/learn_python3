### Python SMTP发送邮件
Python中支持SMTP的模块有**smtplib**和**email**,email负责构造邮件，smtplib负责发送邮件。
```
# -*- coding: utf-8 -*
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
# 输入Email地址和口令:
#from_addr = input('From: ')
sender = 'xxxx@163.com'
password = input('Password: ')
# 输入收件人地址:
#to_addr = input('To: ')
receiver = 'xxxx@163.com'
# 输入SMTP服务器地址:
#smtp_server = input('SMTP server: ')
subject = 'test'
smtp_server = 'smtp.163.com'
#邮件对象
msg = MIMEMultipart()
msg.attach(MIMEText('<html><body><h1>Hello</h1>'+'<p>send by <a href="http://www.python.org">Python</a>...</p>'+'</body></html>', 'html', 'utf-8'))
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'xxxx@163.com <xxxx@163.com>'
msg['To'] = 'pr1s0n <xxxx@163.com>'
#msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('C:/Users/evilli/Desktop/图片/人像原图.jpg', 'rb') as f:
	# 设置附件的MIME和文件名，这里是png类型:
	mime = MIMEBase('image', 'jpeg', filename='1.jpg')
	# 加上必要的头信息:
	mime.add_header('Content-Disposition', 'attachment', filename='1.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	# 把附件的内容读进来:
	mime.set_payload(f.read())
	# 用Base64编码:
	encoders.encode_base64(mime)
	# 添加到MIMEMultipart:
	msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(sender, password)
server.sendmail(sender, [receiver], msg.as_string())
server.quit()
```
这里在实验的时候发现163邮箱不能直接对QQ邮箱发信，说是垃圾邮件。所以测试的时候用的另一个163邮箱，成功发信。
