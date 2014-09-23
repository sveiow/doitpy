#coding=utf-8
#version:2.0,美丽版本，基本完成任务，只需要字典强大，还差部分功能
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

#定義點擊的操作
def click(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)

#导入字典
output = open('hashdata.pkl', 'rb')
hashdata = pickle.load(output)			#此时hashdata已经是字典类型

#开始
def AutoAnswer():
    time.sleep(0.1)         #截图前等待
    fullsc = ImageGrab.grab()               ##截全圖，因爲是pick工作，所以提交答案再截圖
    
    saveQ = fullsc.crop(Qbox).save('tmpQ.jpg','JPEG')         #截图，保存問題
    picQ = open('tmpQ.jpg','rb')
    Qmd5 = hashlib.md5(picQ.read()).hexdigest().upper()         ##計算題目的MD5
    wQmd5 =  '%s' % Qmd5
    getanswer = hashdata.get(wQmd5)         #test1

    #计算所有答案的md5
    saveA = fullsc.crop(Abox).save('tmpA.jpg','JPEG')
    saveB = fullsc.crop(Bbox).save('tmpB.jpg','JPEG')
    saveC = fullsc.crop(Cbox).save('tmpC.jpg','JPEG')
    saveD = fullsc.crop(Dbox).save('tmpD.jpg','JPEG')
    picA = open('tmpA.jpg','rb')
    Amd5 = hashlib.md5(picA.read()).hexdigest().upper() 
    picB = open('tmpB.jpg','rb')
    Bmd5 = hashlib.md5(picB.read()).hexdigest().upper() 
    picC = open('tmpC.jpg','rb')
    Cmd5 = hashlib.md5(picC.read()).hexdigest().upper() 
    picD = open('tmpD.jpg','rb')
    Dmd5 = hashlib.md5(picD.read()).hexdigest().upper()

    ##print 'Q:%s'%Qmd5,'wQ:%s'%wQmd5,'getMd5:%s',getanswer         #test1
    ##print 'A:%s'%Amd5,'B:%s'%Bmd5,'C:%s'%Cmd5,'D:%s'%Dmd5         #test1



    print 'Q:%s'%Qmd5,'wQ:%s'%wQmd5,'getMd5:%s',getanswer         #test1
    print 'A:%s'%Amd5,'B:%s'%Bmd5,'C:%s'%Cmd5,'D:%s'%Dmd5         #test1
    if wQmd5 in hashdata:           #check题目是否存在
        if getanswer == Amd5:
            click(465,580)          #A
            click(505,715)          #post
        elif getanswer == Bmd5:
            click(465,605)
            click(505,715)          #post
        elif getanswer == Cmd5:
            click(465,630)
            click(505,715)          #post
        elif getanswer == Dmd5:
            click(465,655)
            click(505,715)          #post
        else:
            print 'no answer!'
    else:
        print 'no this question in hashdict!'
        click(655,770)          #next

    time.sleep(0.2)
    getProcess()

def getProcess():
    Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'
    fullsc = ImageGrab.grab()
    saveProcess = fullsc.crop(Pcbox).save('tmpProcess.jpg','JPEG')         #截图，保存
    picPc = open('tmpProcess.jpg','rb')
    Pmd5 = hashlib.md5(picPc.read()).hexdigest().upper()
    picPc.close()
    
    if Pmd5 != Pcmd5 :
        click(655,770)          #点击下一题
        AutoAnswer()            #查题循环
    else:
        print 'finish'
        
if __name__ == '__main__':
    AutoAnswer()
