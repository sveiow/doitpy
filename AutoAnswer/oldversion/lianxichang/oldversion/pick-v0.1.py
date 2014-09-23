#coding:gbk
import win32gui
import win32con

getbrow = win32gui.FindWindow("Chrome_WidgetWin_1","�������-������ - Google Chrome")         ##���崰��
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##ǿ����ʾ����
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##�������
win32gui.SetForegroundWindow(getbrow)           ##������������ᵽ��ǰ

from PIL import Image
import ImageGrab
import os
import hashlib

hashp = os.getcwd() + '/hash/1.dict'
workingp = os.getcwd() + '/tmp/'
if os.path.exists(workingp):
    pass
else:
    os.mkdir('tmp')
    
hashpath = os.getcwd() + '/hash'       ##os.getcwd�@ȡ��ǰ����Ŀ�
if os.path.exists(hashpath):
    pass
else:
    os.mkdir('hash')
    
fullsc = ImageGrab.grab()               ##��ȫ�D
Qbox = (515,470,1020,488)               ##�}Ŀ����
Abox = (510,564,840,586)
Bbox = (510,590,840,612)
Cbox = (510,617,840,639)
Dbox = (510,644,840,666)

imageQ = fullsc.crop(Qbox).save(workingp + 'imageQ.jpg','JPEG')

picQ = open(workingp +'imageQ.jpg','rb')
Qmd5 = hashlib.md5(picQ.read()).hexdigest()         ##Ӌ���}ĿQ��MD5

import win32con
import win32api

##���A
Ax = 465
Ay = 580
win32api.SetCursorPos([Ax,Ay])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,Ax,Ay)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,Ax,Ay)
##�ύ��
put_x = 505
put_y = 715
win32api.SetCursorPos([put_x,put_y])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,put_x,put_y)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,put_x,put_y)

getipsc = ImageGrab.grab()          ##Ϊ��ȡ�𰸶���ͼ
Tipsbox = (690,705,705,725)
sTips = getipsc.crop(Tipsbox).save(workingp + 'Tips.JPG','JPEG')         ##�ύ��֮��鿴���_��
Tips = Image.open(os.getcwd() +'/Tips/Tips.JPG')
exA = Image.open(os.getcwd() +'/Tips/TipsA.JPG')
exB = Image.open(os.getcwd() +'/Tips/TipsB.JPG')
exC = Image.open(os.getcwd() +'/Tips/TipsC.JPG')
exD = Image.open(os.getcwd() +'/Tips/TipsD.JPG')


if Tips.histogram() == exA.histogram():
    imageA = fullsc.crop(Abox).save(workingp + 'imageA.jpg','JPEG')
    picA = open(workingp +'imageA.jpg','rb')
    Amd5 = hashlib.md5(picA.read()).hexdigest()         ##Ӌ���A��MD5
    w = '%s : %s \n' % (Qmd5 ,Amd5)          ##����HASH���ļ�
    tk = open(hashp,'a')
    tk.write(w)
    tk.close()
    picA.close()
    
elif Tips.histogram() == exB.histogram():
    imageB = fullsc.crop(Bbox).save(workingp + 'imageB.jpg','JPEG')
    picB = open(workingp +'imageB.jpg','rb')
    Bmd5 = hashlib.md5(picB.read()).hexdigest()         ##Ӌ���B��MD5
    w = '%s : %s \n' % (Qmd5 ,Bmd5)          ##����HASH���ļ�
    tk = open(hashp,'a')
    tk.write(w)
    tk.close()
    picB.close()
    
elif Tips.histogram() == exC.histogram():
    imageC = fullsc.crop(Cbox).save(workingp + 'imageC.jpg','JPEG')
    picC = open(workingp +'imageC.jpg','rb')
    Cmd5 = hashlib.md5(picC.read()).hexdigest()         ##Ӌ���C��MD5
    w = '%s : %s \n' % (Qmd5 ,Cmd5)          ##����HASH���ļ�
    tk = open(hashp,'a')
    tk.write(w)
    tk.close()
    picC.close()
    
elif Tips.histogram() == exD.histogram():
    imageD = fullsc.crop(Dbox).save(workingp + 'imageD.jpg','JPEG')
    picD = open(workingp +'imageD.jpg','rb')
    Dmd5 = hashlib.md5(picD.read()).hexdigest()         ##Ӌ���D��MD5
    w = '%s : %s \n' % (Qmd5 ,Dmd5)          ##����HASH���ļ�
    tk = open(hashp,'a')
    tk.write(w)
    tk.close()
    picD.close()
else:
    print 'no answer!'
    
