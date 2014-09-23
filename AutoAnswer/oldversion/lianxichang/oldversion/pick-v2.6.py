#coding=gbk
#已優化，version:2.6
from PIL import Image
import ImageGrab

import os
import hashlib
import time

import win32gui
import win32con
import win32api

# class autoAnswer():
getbrow = win32gui.FindWindow("Chrome_WidgetWin_1","立秋·驾培-闯关王 - Google Chrome")         ##定义窗口
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##强行显示界面
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
win32gui.SetForegroundWindow(getbrow)           ##将浏览器窗口提到最前

Qbox = (515,470,1020,488)               ##題目盒子
Abox = (510,564,840,586)
Bbox = (510,590,840,612)
Cbox = (510,617,840,639)
Dbox = (510,644,840,666)
Pcbox = (630,760,690,785)           #進度條
Tipsbox = (690,705,705,725)

Amd5 = '2B964BCA9F554C660C5418561AFFF177'
Bmd5 = 'B34D3B3B460019BA8625BAE5EEFE91B1'
Cmd5 = 'BA8A8CF9E8669E09EDB63832B60338D7'
Dmd5 = 'D0C5378938E2CC34C6CB30867FD5C6BB'
Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'

shash = os.getcwd() + '/hash/1.dict'
hashp = os.getcwd() + '/hash'       ##os.getcwd獲取當前工作目錄
if os.path.exists(hashp):
    pass
else:
    os.mkdir('hash')  
wokingp = os.getcwd() + '/tmp/'
if os.path.exists(wokingp):
    pass
else:
    os.mkdir('tmp')

#定義點擊的操作
def click(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)

#建立字典
hashdic = {}
    #開始
def pickit():
    click(465,580)          ##点击A
    click(505,715)          ##提交答案

    time.sleep(0.2)

    fullsc = ImageGrab.grab()               ##截全圖，因爲是pick工作，所以提交答案再截圖

    saveQ = fullsc.crop(Qbox).save(wokingp + 'saveQ.jpg','JPEG')         #截图，保存
    picQ = open(wokingp +'saveQ.jpg','rb')
    Qmd5 = hashlib.md5(picQ.read()).hexdigest().upper()         ##計算題目Q的MD5

    saveTips = fullsc.crop(Tipsbox).save(wokingp + 'Tips.JPG','JPEG')         #截图，保存，提交答案之後查看正確答案
    Tips = open(wokingp +'Tips.JPG','rb')
    Tipsmd5 = hashlib.md5(Tips.read()).hexdigest().upper()

    def md5w():
        md5 = hashlib.md5(pic.read()).hexdigest().upper()           ##計算答案的MD5
        w = '%s:%s\n' % (Qmd5 ,md5)          ##寫入HASH至文件
        tk = open(shash,'a')
        tk.write(w)
        tk.close()
        pic.close()

    if Tipsmd5 == Amd5:
        saveA = fullsc.crop(Abox).save(wokingp + 'A.jpg','JPEG')
        pic = open(wokingp +'A.jpg','rb')
        md5w()
        
    elif Tipsmd5 == Bmd5:
        saveB = fullsc.crop(Bbox).save(wokingp + 'B.jpg','JPEG')
        pic = open(wokingp +'B.jpg','rb')
        md5w()
        
    elif Tipsmd5 == Cmd5:
        saveC = fullsc.crop(Cbox).save(wokingp + 'C.jpg','JPEG')
        pic = open(wokingp +'C.jpg','rb')
        md5w()
        
    elif Tipsmd5 == Dmd5:
        saveD = fullsc.crop(Dbox).save(wokingp + 'D.jpg','JPEG')
        pic = open(wokingp +'D.jpg','rb')
        md5w()
    else:
        print 'no answer!'

    getProcess()

    #判斷當前進度
def getProcess():
    fullsc = ImageGrab.grab() 
    saveProcess = fullsc.crop(Pcbox).save(wokingp + 'Process.jpg','JPEG')         #截图，保存
    picPc = open(wokingp +'Process.jpg','rb')
    Pmd5 = hashlib.md5(picPc.read()).hexdigest().upper()
    picPc.close()

    if Pmd5 != Pcmd5 :
        click(655,770)          #点击下一题
        pickit()
    else:
        print 'finish'

if __name__ == '__main__':
    pickit()
##    getProcess()
