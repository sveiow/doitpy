#coding=utf-8
#Introduction:
from PIL import Image,ImageGrab
import win32gui
import win32con
import win32api
import logging
import os
import time
import hashlib
import pickle
from LXCmodules import *
 
#檢查工作目錄
if os.path.isdir('lxc'):
    pass
else:
    os.mkdir('lxc')

DictS = loadict('DictS.AD')         #導入字典
DictP = loadict('DictP.AD')         #为图片题而设的字典
HashS = {}
HashP = {}

def picmath(box,filepath):
    savepic = fullsc.crop(box).save(filepath,'JPEG')
    pic = open(filepath,'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5

def Answer():
    global fullsc
    time.sleep(0.3)
    fullsc = ImageGrab.grab()

    Qmd5 = picmath(Qbox,'lxc/Qbox.jpg')
    #计算所有答案的md5
    Amd5 = picmath(Abox,'lxc/tmpA.jpg')
    Bmd5 = picmath(Bbox,'lxc/tmpB.jpg')
    Cmd5 = picmath(Cbox,'lxc/tmpC.jpg')
    Dmd5 = picmath(Dbox,'lxc/tmpD.jpg')

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
            Q2md5 = picmath(Q2box,'lxc/tmpQbox2.jpg')

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
        Q2md5 = picmath(Q2box,'lxc/tmpQbox2.jpg')

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

def Pick():
    time.sleep(0.5)         #减速 这里数值可以增大
    clickClient(getbrow,(465,580))          ##点击A
    clickClient(getbrow,(505,715))          ##提交答案
    time.sleep(1.5)         #减速等待

    global fullsc
    fullsc = ImageGrab.grab()
    Qmd5 = picmath(Qbox,'lxc/Qbox.jpg')
    Q2md5 = picmath(Q2box,'lxc/Qbox2.jpg')
    Tipsmd5 = picmath(Tipsbox,'lxc/Tips.JPG')

    if Tipsmd5 == Amd5:
        HashS[Qmd5] = picmath(Abox,'lxc/A.jpg')
        HashP[Q2md5] = picmath(Abox,'lxc/A.jpg')

    elif Tipsmd5 == Bmd5:
        HashS[Qmd5] = picmath(Bbox,'lxc/B.jpg')
        HashP[Q2md5] = picmath(Bbox,'lxc/B.jpg')

    elif Tipsmd5 == Cmd5:
        HashS[Qmd5] = picmath(Cbox,'lxc/C.jpg')
        HashP[Q2md5] = picmath(Cbox,'lxc/C.jpg')

    elif Tipsmd5 == Dmd5:
        HashS[Qmd5] = picmath(Dbox,'lxc/D.jpg')
        HashP[Q2md5] = picmath(Dbox,'lxc/D.jpg')
    else:
        print 'no answer! no tips! cant catch!'

def NextQ():
    #判斷當前進度
    Pmd5 = picmath(Pcbox,'lxc/Process.jpg')
    if Pmd5 != Pcmd5 :
        clickClient(getbrow,(655,770))          #点击下一题
        Answer()            #查题循环
    else:
        pass

def Nextstep():
    clickClient(getbrow,(1020,865))          #交卷
    time.sleep(0.5)
    clickClient(getbrow,(560,680))          #未完成提示框的確認
    time.sleep(2.5)
    global fullsc
    fullsc = ImageGrab.grab()

    Buttunmd5 = picmath(Button,'tmp/Button.JPG')
    if Buttunmd5 == ButtunT:
        clickClient(getbrow,(490,720))          #點擊練習下一個知識點
        time.sleep(2)
        Pickit()
    elif Buttunmd5 == ButtunF:
        clickClient(getbrow,(490,720))          #點擊失敗重做
        AutoAnswer()
    else:
        print "all this chapter finish!"
        return
##########

def AutoAnswer():
    Answer()
    NextQ()

    #進入下一節
    clickClient(getbrow,(1020,865))          #交卷
    time.sleep(1)
    clickClient(getbrow,(560,680))          #未完成提示框的確認
    time.sleep(1.5)

    fullsc = ImageGrab.grab()
    Buttunmd5 = picmath(Button,'lxc/Button.JPG')
    if Buttunmd5 == ButtunT:
        clickClient(getbrow,(490,720))          #練習下一個知識點
        Answer()
    else:
        logging.info('all this chapter finish!')
        return

def Pickit():
    Pick()
    Pmd5 = picmath(Pcbox,'lxc/Process.jpg')
    if Pmd5 != Pcmd5 :
        clickClient(getbrow,(655,770))          #点击下一题
        Pickit()            #查题循环
    else:
        if Blank in HashP:            #判断、删除空白图片的KEY
            del HashP[Blank]
        wdict('DictS.part',HashS)
        wdict('DictP.part',HashP)
        print 'finish'

def OnePickit():
    Pick()
    if Blank in HashP:            #判断、删除空白图片的KEY
        del HashP[Blank]
    wdict('DictS.part',HashS)
    wdict('DictP.part',HashP)
    print 'finish'

def SemiautoPick():
    Pickit()
    Nextstep()

def AutoAD():
    ADcount = 10
    while ADcount > 0:
        clickClient(getbrow,(265,888))           #我要发言
        time.sleep(0.3)
        clickClient(getbrow,(256,775))           #点击对话框
        keyboard()          #SendMessage
        time.sleep(0.1)
        clickClient(getbrow,(212,892))           #发布
        time.sleep(0.3)
        ADcount = ADcount - 1

    Answer()
    Pmd5 = picmath(Pcbox,'lxc/Process.jpg')
    if Pmd5 != Pcmd5 :
        clickClient(getbrow,(655,770))          #点击下一题
        AutoAD()            #查题循环
    else:
    #進入下一節
        clickClient(getbrow,(1020,865))          #交卷
        time.sleep(1)
        clickClient(getbrow,(560,680))          #未完成提示框的確認
        time.sleep(1.5)

        fullsc = ImageGrab.grab()
        Buttunmd5 = picmath(Button,'lxc/Button.JPG')
        if Buttunmd5 == ButtunT:
            clickClient(getbrow,(490,720))          #練習下一個知識點
            AutoAD()
        else:
            logging.info('all this chapter finish!')


getbrow = win32gui.FindWindow('Chrome_WidgetWin_1',u'立秋·驾培-闯关王 - Google Chrome')            ##定义窗口

choice = """
输入1，进入自动答题
输入2，进入整节收集
输入3，进入单题收集
输入p，进入整章收集
输入a，进入发广告模式
输入q，离开

Enter choice:"""

try:
    choice = raw_input(choice).strip()[0].lower()
except(EOFError,KeyboardInterrupt):
    choice = 'q'
if choice == 'q':exit()    

win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##强行显示界面
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
win32gui.SetForegroundWindow(getbrow)
##    win32gui.SetWindowPos(getbrow,win32con.HWND_TOPMOST,0,0,
##                          win32con.SWP_NOSIZE,win32con.SWP_NOSIZE,
##                          win32con.SWP_NOZORDER)           ##将浏览器窗口提到最前
##    win32gui.SetForegroundWindow(getbrow)            ##强行显示界面
time.sleep(0.8)         #等待窗口完全彈出

##if choice == '1':AutoAnswer()
##if choice == '2':Pickit()
##if choice == '3':OnePickit()
##if choice == 'p':SemiautoPick()
##if choice == 'a':AutoAD()

chos = {
    '1':AutoAnswer,
    '2':Pickit,
    '3':OnePickit,
    'p':SemiautoPick,
    'a':AutoAD,
    }
chos.get(choice)()
