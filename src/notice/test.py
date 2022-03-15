# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.mime.text import MIMEText
from email.header import Header
print ("正在推送......") 
smtp = 'smtp.qq.com'
'''
email['From'] = 'hjzhu@hillstonenet.com'
email['To'] = 'hjzhu@hillstonenet.com'
log.info('rec...')
subject = 'threat-info'
email['Subject'] = Header(subject, 'utf-8')
'''
sender = 'threat_broadcast@qq.com'
password = 'eqiiccfetmdnbiaa'
try:
    smtpObj = smtplib.SMTP(smtp)
    smtpObj.login = (sender,password)
    smtpObj.sendmail(sender,'threat_broadcast@qq.com','test')
except smtplib.SMTPException:
    print 'error'
