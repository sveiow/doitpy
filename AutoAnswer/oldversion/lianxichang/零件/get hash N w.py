#coding=gbk

import os
import re
import hashlib

#�Զ��M��ģʽ�v��Ŀ䛈DƬ��GET HASH
rule = re.compile(r'^(.*)\.(jpg|jpeg|bmp|gif|png|JPG|JPEG|BMP|GIF|PNG)$')
dirpath = r'C:\Users\Swains\Desktop'
wp = os.getcwd() + '/' +'tk.log'       ##os.getcwd�@ȡ��ǰ����Ŀ�
for fp in os.listdir(dirpath):
    fp = dirpath + '/' + fp
    if rule.match(fp):
        pic = open(fp,'rb')
        picmd5 = hashlib.md5(pic.read()).hexdigest()
        w = '%s the hash is %s \n' % (fp ,picmd5)          ##����HASH���ļ�
        pic.close()
        tk = open(wp,'a')
        tk.write(w)
        tk.close()
