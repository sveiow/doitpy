#coding=utf-8
#Introduction:20140917
from PIL import Image,ImageGrab
import win32gui
import win32con
import win32api
import logging
import os
import time
import hashlib
import pickle
from AAmodules import *

getbrow = win32gui.FindWindow('Chrome_WidgetWin_1',u'立秋·驾培-闯关王 - Google Chrome')            ##定义窗口
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##强行显示界面
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
win32gui.SetForegroundWindow(getbrow)           ##将浏览器窗口提到前台
time.sleep(0.8)         #等待窗口完全彈出

if os.path.exists('ADtmp') == False: os.mkdir('ADtmp')

try:
    DictS = loadict('DictS.AD')
    DictP = loadict('DictP.AD')
except IOError:
    win32api.MessageBox(0, str("没找到字典，程式退出！"), "错误", win32con.MB_ICONINFORMATION)
    exit()

def PicHash(box,filepath):
    savepic = fullsc.crop(box).save(os.path.join('ADtmp',filepath),'JPEG')
    pic = open(os.path.join('ADtmp',filepath),'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5

def Answer():
    global fullsc
    time.sleep(0.3)
    fullsc = ImageGrab.grab()

    Qmd5 = PicHash(LXC.Qbox,'Qbox.jpg')
    #计算所有答案的md5
    Amd5 = PicHash(LXC.Abox,'A.jpg')
    Bmd5 = PicHash(LXC.Bbox,'B.jpg')
    Cmd5 = PicHash(LXC.Cbox,'C.jpg')
    Dmd5 = PicHash(LXC.Dbox,'D.jpg')

    if Qmd5 in DictS:           #check DictS 题目是否存在
        gas1 = DictS.get(Qmd5)
        if Amd5 == gas1:
            clickClient(getbrow,LXC.Axy)          #A
            clickClient(getbrow,LXC.Submit)          #post
        elif Bmd5 == gas1:
            clickClient(getbrow,LXC.Bxy)          #B
            clickClient(getbrow,LXC.Submit)          #post
        elif Cmd5 == gas1:
            clickClient(getbrow,LXC.Cxy)          #C
            clickClient(getbrow,LXC.Submit)          #post
        elif Dmd5 == gas1:
            clickClient(getbrow,LXC.Dxy)          #D
            clickClient(getbrow,LXC.Submit)          #post
        else:
            logging.info('no answer in DictS,check DictP')
            time.sleep(0.5)
            Q2md5 = PicHash(LXC.Q2box,'Qbox2.jpg')

            if Q2md5 in DictP:           #check DictP 题目是否存在
                gas2 = DictP.get(Q2md5)
                if Amd5 == gas2:
                    clickClient(getbrow,LXC.Axy)          #A
                    clickClient(getbrow,LXC.Submit)          #post
                elif Bmd5 == gas2:
                    clickClient(getbrow,LXC.Bxy)          #B
                    clickClient(getbrow,LXC.Submit)          #post
                elif Cmd5 == gas2:
                    clickClient(getbrow,LXC.Cxy)          #C
                    clickClient(getbrow,LXC.Submit)          #post
                elif Dmd5 == gas2:
                    clickClient(getbrow,LXC.Dxy)          #D
                    clickClient(getbrow,LXC.Submit)          #post
            else:
                logging.info('no answer in all dicts')
    else:
        time.sleep(0.5)
        Q2md5 = PicHash(LXC.Q2box,'Qbox2.jpg')

        if Q2md5 in DictP:           #check DictP 题目是否存在
            gas2 = DictP.get(Q2md5)
            if Amd5 == gas2:
                clickClient(getbrow,LXC.Axy)          #A
                clickClient(getbrow,LXC.Submit)          #post
            elif Bmd5 == gas2:
                clickClient(getbrow,LXC.Bxy)          #B
                clickClient(getbrow,LXC.Submit)          #post
            elif Cmd5 == gas2:
                clickClient(getbrow,LXC.Cxy)          #C
                clickClient(getbrow,LXC.Submit)          #post
            elif Dmd5 == gas2:
                clickClient(getbrow,LXC.Dxy)          #D
                clickClient(getbrow,LXC.Submit)          #post
        else:
            logging.info('no answer in DictP,no answer in all dicts')

#===============================================================================
def sendAD():
    count = 15
    while count > 0:
        clickClient(getbrow,(265,888))           #我要发言
        time.sleep(0.3)
        clickClient(getbrow,(256,775))           #点击对话框
        keyboard()          #SendMessage
        time.sleep(0.1)
        clickClient(getbrow,(212,892))           #发布
        time.sleep(0.3)
        count = count - 1

def AutoAnswer():
    sendAD()
    Answer()
    Pmd5 = PicHash(LXC.Pcbox,'Process.jpg')
    if Pmd5 != LXC.Pcmd5 :
        clickClient(getbrow,LXC.Next)
        AutoAnswer()
    else:
        clickClient(getbrow,LXC.Handin)
        time.sleep(1)
        clickClient(getbrow,LXC.BT1)          #未完成提示框的確認
        time.sleep(2)

        global fullsc
        fullsc = ImageGrab.grab()
        Buttunmd5 = PicHash(LXC.Button,'Button.JPG')
        if Buttunmd5 != LXC.ButtunBlank:
            clickClient(getbrow,LXC.BT2)          #練習下一個知識點
            AutoAnswer()
        else:
            logging.info('all this chapter finish!')
            exit()

AutoAnswer()
