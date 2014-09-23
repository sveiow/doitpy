#coding=utf-8
#�у�����version:3.0
from PIL import Image
import ImageGrab

import os
import hashlib
import time
import pickle

import win32gui
import win32con
import win32api

# class autoAnswer():
getbrow = win32gui.FindWindow('Chrome_WidgetWin_1',u'�������-������ - Google Chrome')            ##���崰��
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##ǿ����ʾ����
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##�������
win32gui.SetForegroundWindow(getbrow)           ##������������ᵽ��ǰ

Qbox = (515,470,1020,488)               ##�}Ŀ����
Abox = (510,564,840,586)
Bbox = (510,590,840,612)
Cbox = (510,617,840,639)
Dbox = (510,644,840,666)
Pcbox = (630,760,690,785)           #�M�ȗl

#���x�c���Ĳ���
def click(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)

#�����ֵ�
output = open('hashdict.pkl', 'rb')
hashdata = pickle.load(output)

fullsc = ImageGrab.grab()               ##��ȫ�D������pick�����������ύ���ٽ؈D

saveQ = fullsc.crop(Qbox).save(wokingp + 'saveQ.jpg','JPEG')         #��ͼ�����憖�}
picQ = open(wokingp +'saveQ.jpg','rb')
Qmd5 = hashlib.md5(picQ.read()).hexdigest().upper()         ##Ӌ���}Ŀ��MD5
wQmd5 =  '%s' % Qmd5

#�������д𰸵�md5
saveA = fullsc.crop(Abox).save('tmpA.jpg','JPEG')
saveB = fullsc.crop(Bbox).save('tmpB.jpg','JPEG')
saveC = fullsc.crop(Cbox).save('tmpC.jpg','JPEG')
saveD = fullsc.crop(Dbox).save('tmpD.jpg','JPEG')
picA = open('tmpA.jpg','rb')
Amd5 = hashlib.md5(picA.read()).hexdigest().upper() 
picB = open('tmpA.jpg','rb')
Bmd5 = hashlib.md5(picB.read()).hexdigest().upper() 
picC = open('tmpA.jpg','rb')
Cmd5 = hashlib.md5(picC.read()).hexdigest().upper() 
picD = open('tmpA.jpg','rb')
Dmd5 = hashlib.md5(picD.read()).hexdigest().upper() 

def cNp()
    if wQmd5 in hashdata:           #check��Ŀ�Ƿ����
        getanswer = hashdata[wQmd5]
        if getanswer == Amd5:
            click(465,580)
            pNn()
        elif getanswer == Bmd5:
            click(465,605)
            pNn()
        elif getanswer == Cmd5:
            click(465,630)
            pNn()
        elif getanswer == Dmd5:
            click(465,655)
            pNn()
        else:
            print 'no answer!'
    else:
        print 'no this question in hashdict!'
    
    getProcess()

def getProcess():
    fullsc = ImageGrab.grab() 
    saveProcess = fullsc.crop(Pcbox).save(wokingp + 'Process.jpg','JPEG')         #��ͼ������
    picPc = open(wokingp +'Process.jpg','rb')
    Pmd5 = hashlib.md5(picPc.read()).hexdigest().upper()
    picPc.close()
    
    if Pmd5 != Pcmd5 :
    click(655,770)          #�����һ��
    cNp()            #����ѭ��
    
if __name__ == '__main__':
    cNp()