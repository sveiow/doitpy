#coding=utf-8
#version:Autoanswer_offical_v2.0，for:闯关王——练兵场
from PIL import Image
import ImageGrab

import os
import hashlib
import time
import pickle

import win32gui
import win32con
import win32api

getbrow = win32gui.FindWindow('Chrome_WidgetWin_1',u'立秋·驾培-闯关王 - Google Chrome')            ##定义窗口
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##强行显示界面
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
win32gui.SetForegroundWindow(getbrow)           ##将浏览器窗口提到最前
time.sleep(0.8)         #等待窗口完全彈出

#檢查工作目錄
if os.path.isdir('tmp'):
    pass
else:
    os.mkdir('tmp')

    #定義元素
#导入字典
output = open('hashdict_v2.pkl', 'rb')
hashdata = pickle.load(output)			#此时hashdata已经是字典类型

Qbox = (515,470,1020,488)
Q2box = (860,500,1050,655)
Abox = (510,564,840,586)
Bbox = (510,590,840,612)
Cbox = (510,617,840,639)
Dbox = (510,644,840,666)
Pcbox = (630,760,690,785)

def click(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)

def nextchapter():
    click(1020,865)          #交卷
    time.sleep(0.3)
##    click(560,680)          #未完成提示框的確認
    click(490,720)          #練習下一個知識點
    #結束

def AutoAnswer():
    time.sleep(0.3)         #截图前，降速等待窗口的显示，至少0.2秒
    fullsc = ImageGrab.grab()               ##截全圖，因爲是pick工作，所以提交答案再截圖

    saveQ = fullsc.crop(Qbox).save('tmp/tmpQbox.jpg','JPEG')
    picQ = open('tmp/tmpQbox.jpg','rb')
    Qmd5 = hashlib.md5(picQ.read()).hexdigest().upper()
    saveQ2 = fullsc.crop(Q2box).save('tmp/tmpQbox2.jpg','JPEG')
    picQ2 = open('tmp/tmpQbox2.jpg','rb')
    Q2md5 = hashlib.md5(picQ.read()).hexdigest().upper()
        #为解决相同题目问题，加入QBox2，再生成MD5
    AllQmd5 = '%s%s' %(Qmd5,Q2md5)
    AllQmd5 = hashlib.md5(AllQmd5).hexdigest().upper()
    wAllQmd5 =  '%s' % AllQmd5
    getanswer = hashdata.get(wAllQmd5)          #查询题目对应的答案

    #计算所有答案的md5
    saveA = fullsc.crop(Abox).save('tmp/tmpA.jpg','JPEG')
    saveB = fullsc.crop(Bbox).save('tmp/tmpB.jpg','JPEG')
    saveC = fullsc.crop(Cbox).save('tmp/tmpC.jpg','JPEG')
    saveD = fullsc.crop(Dbox).save('tmp/tmpD.jpg','JPEG')
    picA = open('tmp/tmpA.jpg','rb')
    Amd5 = hashlib.md5(picA.read()).hexdigest().upper()
    picA.close()
    picB = open('tmp/tmpB.jpg','rb')
    Bmd5 = hashlib.md5(picB.read()).hexdigest().upper()
    picB.close()
    picC = open('tmp/tmpC.jpg','rb')
    Cmd5 = hashlib.md5(picC.read()).hexdigest().upper()
    picC.close()
    picD = open('tmp/tmpD.jpg','rb')
    Dmd5 = hashlib.md5(picD.read()).hexdigest().upper()
    picD.close()

    if wAllQmd5 in hashdata:           #check题目是否存在
        if getanswer == Amd5:
            click(465,580)          #A
            click(505,715)          #post
        elif getanswer == Bmd5:
            click(465,605)          #B
            click(505,715)          #post
        elif getanswer == Cmd5:
            click(465,630)          #C
            click(505,715)          #post
        elif getanswer == Dmd5:
            click(465,655)          #D
            click(505,715)          #post
        else:
            print 'no answer!'
    else:
        print 'no this question in hashdict!'
        click(655,770)          #next

    getProcess()

def getProcess():
    Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'
    fullsc = ImageGrab.grab()
    saveProcess = fullsc.crop(Pcbox).save('tmp/tmpProcess.jpg','JPEG')         #截图，保存
    picPc = open('tmp/tmpProcess.jpg','rb')
    Pmd5 = hashlib.md5(picPc.read()).hexdigest().upper()
    picPc.close()

    if Pmd5 != Pcmd5 :
        click(655,770)          #点击下一题
        AutoAnswer()            #查题循环
    else:
        print 'finish'
        nextchapter()

if __name__ == '__main__':
    AutoAnswer()
