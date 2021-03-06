#coding=utf-8
#Introduction:自動答題 ----- for:闯关王——练兵场,正式可用,20140825
#version:Autoanswer_a2.0
#updata 20140825:修改了print至logging
#updata a2.0:修改Q2BOX,修改字典部分
#updata a1.5:修改鼠標模擬的方式，解決鼠標失控問題（側面解決死循環）
#updata a1.0:基於v2.2的重寫
from PIL import Image
import ImageGrab

import logging
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
Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'
ButtunT = 'BB54913D762C90152D4071BA66795C6A'

Qbox = (515,470,1020,488)
Q2box = (860,505,1050,655)
Abox = (510,564,840,586)
Bbox = (510,590,840,612)
Cbox = (510,617,840,639)
Dbox = (510,644,840,666)
Pcbox = (630,760,690,785)
Button = (410,705,575,740)

def loadict(dictfile):
    output = open(dictfile, 'rb')
    hashdict = pickle.load(output)
    return hashdict

def clickClient(handle,pos):
    coordinate = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(handle,win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)          #这里应该是控制前台还是后台模拟
    win32api.SendMessage(handle,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,coordinate)
    win32api.SendMessage(handle,win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,coordinate)

def oplog():
    logging.basicConfig(
        filename = os.path.join(os.getcwd(),'tmp', 'log.txt'),
        level = logging.INFO,
        datefmt = '%m-%d %H:%M',
        format = '%(asctime)s : %(message)s',
        filemode = 'a')
    #結束

DictS = loadict('DictS.part1')         #導入字典
DictP = loadict('DictP.part1')           #为图片题而设的字典

def AutoAnswer():
    def picmath(box,filepath):
        savepic = fullsc.crop(box).save(filepath,'JPEG')
        pic = open(filepath,'rb')
        md5 = hashlib.md5(pic.read()).hexdigest().upper()
        pic.close()
        return md5

    time.sleep(0.3)         #截图前，降速等待窗口的显示，至少0.2秒
    fullsc = ImageGrab.grab()

    Qmd5 = picmath(Qbox,'tmp/Qbox.jpg')
    #计算所有答案的md5
    Amd5 = picmath(Abox,'tmp/tmpA.jpg')
    Bmd5 = picmath(Bbox,'tmp/tmpB.jpg')
    Cmd5 = picmath(Cbox,'tmp/tmpC.jpg')
    Dmd5 = picmath(Dbox,'tmp/tmpD.jpg')

    if Qmd5 in DictS:           #check DictS 题目是否存在
        gas1 = DictS.get(Qmd5)
        if Amd5 == gas1:
            clickClient(getbrow,(465,580))          #A
            clickClient(getbrow,(505,715))          #post
        elif Bmd5 == gas1:
            clickClient(getbrow,(465,605))          #B
            clickClient(getbrow,(505,715))          #post
        elif Cmd5 == gas1:
            clickClient(getbrow,(465,630))          #C
            clickClient(getbrow,(505,715))          #post
        elif Dmd5 == gas1:
            clickClient(getbrow,(465,655))          #D
            clickClient(getbrow,(505,715))          #post
        else:
            logging.info('no answer in DictS,check DictP')

            time.sleep(0.5)
            Q2md5 = picmath(Q2box,'tmp/tmpQbox2.jpg')

            if Q2md5 in DictP:           #check DictP 题目是否存在
                gas2 = DictP.get(Q2md5)
                if Amd5 == gas2:
                    clickClient(getbrow,(465,580))          #A
                    clickClient(getbrow,(505,715))          #post
                elif Bmd5 == gas2:
                    clickClient(getbrow,(465,605))          #B
                    clickClient(getbrow,(505,715))          #post
                elif Cmd5 == gas2:
                    clickClient(getbrow,(465,630))          #C
                    clickClient(getbrow,(505,715))          #post
                elif Dmd5 == gas2:
                    clickClient(getbrow,(465,655))          #D
                    clickClient(getbrow,(505,715))          #post
                else:
                    logging.info('no answer in all dicts')
    else:
        time.sleep(0.5)
        Q2md5 = picmath(Q2box,'tmp/tmpQbox2.jpg')

        if Q2md5 in DictP:           #check DictP 题目是否存在
            gas2 = DictP.get(Q2md5)
            if Amd5 == gas2:
                clickClient(getbrow,(465,580))          #A
                clickClient(getbrow,(505,715))          #post
            elif Bmd5 == gas2:
                clickClient(getbrow,(465,605))          #B
                clickClient(getbrow,(505,715))          #post
            elif Cmd5 == gas2:
                clickClient(getbrow,(465,630))          #C
                clickClient(getbrow,(505,715))          #post
            elif Dmd5 == gas2:
                clickClient(getbrow,(465,655))          #D
                clickClient(getbrow,(505,715))          #post
            else:
                logging.info('no answer in DictP,no answer in all dicts')

    #判斷當前進度
    Pmd5 = picmath(Pcbox,'tmp/Process.jpg')
    if Pmd5 != Pcmd5 :
        clickClient(getbrow,(655,770))          #点击下一题
        AutoAnswer()            #查题循环
    else:
##        print 'finish, next chapter!'
    #進入下一節
        clickClient(getbrow,(1020,865))          #交卷
        time.sleep(1)
        clickClient(getbrow,(560,680))          #未完成提示框的確認
        time.sleep(1.5)

        fullsc = ImageGrab.grab()
        Buttunmd5 = picmath(Button,'tmp/Button.JPG')
        if Buttunmd5 == ButtunT:
            clickClient(getbrow,(490,720))          #練習下一個知識點
            AutoAnswer()
        else:
            logging.info('all this chapter finish!')
            return

if __name__ == '__main__':
    oplog()
    AutoAnswer()
