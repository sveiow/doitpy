#coding=utf-8
#输出目录文件的MD5
import os
import re
import hashlib

rule = re.compile(r'^(.*)\.(jpg|jpeg|bmp|gif|png|JPG|JPEG|BMP|GIF|PNG)$')
for filepath in os.listdir(os.getcwd()):
    filepath = os.getcwd()+'/'+filepath
    if rule.match(filepath):
        pic = open(filepath,'rb')
        pic16md5 = hashlib.md5(pic.read()).digest()
        pic32md5 = hashlib.md5(pic.read()).hexdigest()
        print '%s'%filepath
        print 'MD5 16 is: %s'%pic16md5
        print 'MD5 32 is: %s'%pic32md5

