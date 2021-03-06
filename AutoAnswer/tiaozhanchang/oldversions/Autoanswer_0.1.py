#coding=utf-8
#version:Autoanswer_0.1，for:闯关王——挑战场
#updata 0.1:基於Autoanswer_a1.0的改寫
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
Pcmd5 = '38E53A7D5DD9FC87B8C74B6CD911C22D'

Qbox = (515,470,1020,488)
Q2box = (860,500,1050,655)
Abox = (510,564,840,586)
Bbox = (510,590,840,612)
Cbox = (510,617,840,639)
Dbox = (510,644,840,666)
Pcbox = (927,707,1059,744)

def loadict(dictfile):
    output = open(dictfile, 'rb')
    hashdict = pickle.load(output)
    return hashdict

def click(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)
    #結束

hashdictv1 = loadict('hashdata_v1.pkl')         #導入字典
hashdictv2 = loadict('hashdata_v2.pkl')

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

    if Qmd5 in hashdictv1:           #check dict1 题目是否存在
         ##第一次查询题目对应的答案
        getanswer1 = hashdictv1.get(Qmd5)
        if Amd5 == getanswer1:
            click(465,580)          #A
            click(505,715)          #post
        elif Bmd5 == getanswer1:
            click(465,605)          #B
            click(505,715)          #post
        elif Cmd5 == getanswer1:
            click(465,630)          #C
            click(505,715)          #post
        elif Dmd5 == getanswer1:
            click(465,655)          #D
            click(505,715)          #post
        else:
            time.sleep(0.7)
            Q2md5 = picmath(Q2box,'tmp/tmpQbox2.jpg')
            AllQmd5 = hashlib.md5('%s%s' %(Qmd5,Q2md5)).hexdigest().upper()

            if AllQmd5 in hashdictv2:           #check dict2 题目是否存在
                getanswer2 = hashdictv2.get(AllQmd5)
                if Amd5 == getanswer2:
                    click(465,580)          #A
                    click(505,715)          #post
                elif Bmd5 == getanswer2:
                    click(465,605)          #B
                    click(505,715)          #post
                elif Cmd5 == getanswer2:
                    click(465,630)          #C
                    click(505,715)          #post
                elif Dmd5 == getanswer2:
                    click(465,655)          #D
                    click(505,715)          #post
                else:
                    print 'no answer!'
            else:
                print 'no this question in hashdict!!'

    #判斷當前進度
    Pmd5 = picmath(Pcbox,'tmp/Process.jpg')
    if Pmd5 != Pcmd5 :
        click(990,725)          #点击下一题
        AutoAnswer()            #答题循环
    else:
        print 'finish!'
        click(265,880)          #交卷
        time.sleep(0.1)
##        click(570,680)          #最后确定

if __name__ == '__main__':
    AutoAnswer()
