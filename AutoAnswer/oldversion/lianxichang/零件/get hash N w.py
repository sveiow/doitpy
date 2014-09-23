#coding=gbk

import os
import re
import hashlib

#以二進制模式歷遍目錄圖片，GET HASH
rule = re.compile(r'^(.*)\.(jpg|jpeg|bmp|gif|png|JPG|JPEG|BMP|GIF|PNG)$')
dirpath = r'C:\Users\Swains\Desktop'
wp = os.getcwd() + '/' +'tk.log'       ##os.getcwd獲取當前工作目錄
for fp in os.listdir(dirpath):
    fp = dirpath + '/' + fp
    if rule.match(fp):
        pic = open(fp,'rb')
        picmd5 = hashlib.md5(pic.read()).hexdigest()
        w = '%s the hash is %s \n' % (fp ,picmd5)          ##寫入HASH至文件
        pic.close()
        tk = open(wp,'a')
        tk.write(w)
        tk.close()
