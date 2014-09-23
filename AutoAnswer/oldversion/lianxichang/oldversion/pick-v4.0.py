#coding=utf-8
#version:4.0，缺题目校验，当前没问题
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
getbrow = win32gui.FindWindow('Chrome_WidgetWin_1',u'立秋·驾培-闯关王 - Google Chrome')            ##定义窗口
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

#建立字典
hashdict = {}
#檢測工作目錄
if os.path.isdir('tmp'):
    pass
else:
    os.mkdir('tmp')   
#檢測字典是否存在
if os.path.isfile('hashdict.pkl'):
    pass
##    oldict = open('hashdict.pkl', 'rb')
##    oldata = pickle.load(oldict)
else:
    setup = open('hashdict.pkl', 'wb')
    pickle.dump(hashdict,setup)
##    oldict = open('hashdict.pkl', 'rb')
##    oldata = pickle.load(oldict)
    
#定義點擊的操作
def click(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)

    #開始
def pickit():
    time.sleep(0.2)         #减速等待
    click(465,580)          ##点击A
    time.sleep(0.2)         #减速等待
    click(505,715)          ##提交答案

    time.sleep(0.2)         #减速等待
    fullsc = ImageGrab.grab()               ##截全圖，因爲是pick工作，所以提交答案再截圖

    saveQ = fullsc.crop(Qbox).save('tmp/saveQ.jpg','JPEG')         #截图，保存問題
    picQ = open('tmp/saveQ.jpg','rb')
    Qmd5 = hashlib.md5(picQ.read()).hexdigest().upper()         ##計算題目的MD5
    wQmd5 =  '%s' % Qmd5

    saveTips = fullsc.crop(Tipsbox).save('tmp/Tips.JPG','JPEG')         #截图，保存，提交答案之後查看正確答案
    Tips = open('tmp/Tips.JPG','rb')
    Tipsmd5 = hashlib.md5(Tips.read()).hexdigest().upper()

    def md5w():
        md5 = hashlib.md5(pic.read()).hexdigest().upper()           ##計算答案的MD5
        wmd5 = '%s' % md5
        hashdict[wQmd5] = wmd5
        pic.close()

    if Tipsmd5 == Amd5:
        saveA = fullsc.crop(Abox).save('tmp/A.jpg','JPEG')
        pic = open('tmp/A.jpg','rb')
        md5w()

    elif Tipsmd5 == Bmd5:
        saveB = fullsc.crop(Bbox).save('tmp/B.jpg','JPEG')
        pic = open('tmp/B.jpg','rb')
        md5w()

    elif Tipsmd5 == Cmd5:
        saveC = fullsc.crop(Cbox).save('tmp/C.jpg','JPEG')
        pic = open('tmp/C.jpg','rb')
        md5w()

    elif Tipsmd5 == Dmd5:
        saveD = fullsc.crop(Dbox).save('tmp/D.jpg','JPEG')
        pic = open('tmp/D.jpg','rb')
        md5w()
    else:
        print 'no answer!'

    getProcess()

    #判斷當前進度
def getProcess():
    fullsc = ImageGrab.grab()
    saveProcess = fullsc.crop(Pcbox).save('tmp/Process.jpg','JPEG')         #截图，保存
    picPc = open('tmp/Process.jpg','rb')
    Pmd5 = hashlib.md5(picPc.read()).hexdigest().upper()
    picPc.close()

    if Pmd5 != Pcmd5 :
        click(655,770)          #点击下一题
        pickit()            #查题循环
    else:
        oldict = open('hashdict.pkl', 'rb')
        oldata = pickle.load(oldict)
        hashdict.update(oldata)
        output = open('hashdict.pkl', 'wb')         #全部题目记录好了，然后就写入文件
        pickle.dump(hashdict,output)          ##寫入HASH至文件
        print 'finish'

if __name__ == '__main__':
    pickit()
