# -*- coding: utf-8 -*-

import sys
# sysモジュールをリロードする
reload(sys)
# デフォルトの文字コードを変更する．
sys.setdefaultencoding('utf-8')
# デフォルトの文字コードを出力する．
print 'defaultencoding:', sys.getdefaultencoding()


import re
import time
from getpass import getpass

import poplib
poplib._MAXLINE=20480

import email
from email.header import decode_header
from email.Header import Header
from email.MIMEText import MIMEText
from email import Utils



USERNAME = raw_input('username :')
PASSWORD = getpass('password :')

list_num = raw_input('number? : ')
keyword = raw_input('keyword? : ')



M = poplib.POP3_SSL('outlook.office365.com', 995)
print M.getwelcome()

print M.user(USERNAME)
print M.pass_(PASSWORD)


num = len(M.list()[1])
print num

mail_list = M.list()

#print mail_list

msg1 = M.retr(list_num)[1]
#print type(msg1)
#print msg1

mail = ''
for j in msg1:
    mail = mail + j + '\n'
#print mail

msg = email.message_from_string(mail)
#print msg
print type(msg)

email_default_encoding = 'iso-2022-jp'

msg_subject = decode_header(msg.get('Subject'))[0][0]
msg_encoding = decode_header(msg.get('Subject'))[0][1] or email_default_encoding

if not msg.is_multipart():
    body_encoding = msg.get_content_charset()
    body = msg.get_payload(decode=True)
    print body_encoding
    print body



subject = msg_subject.decode(msg_encoding)
print msg_encoding
print subject

#target = u'メール'

target = keyword

if target in subject:
    print subject
else:
    print 'None'




#for i in range(num):
#    for j in M.retr(i+1)[1]:
#        print j




M.quit()




