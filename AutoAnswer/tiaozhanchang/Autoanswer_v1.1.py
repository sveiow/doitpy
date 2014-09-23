#coding=utf-8
#Introduction:自動答題 ----- for:闯关王——挑战场,正式可用,20140906
#version:Autoanswer_v1.1
#updata v1.0:修改鼠標模擬的方式，解決鼠標失控問題（側面解決死循環）
#updata 0.1:基於Autoanswer_a1.0的改寫
from PIL import Image,ImageGrab
import os,time
import hashlib,pickle
import win32gui,win32con,win32api

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

def clickClient(handle,pos):
    coordinate = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, coordinate)
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, coordinate)

def picmath(box,filepath):
    savepic = fullsc.crop(box).save(filepath,'JPEG')
    pic = open(filepath,'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5
    #結束

hashDictS = loadict('hashDictS.tzc')         #導入字典
hashDictP = loadict('hashDictP.tzc')

def AutoAnswer():
    time.sleep(0.5)         #截图前，降速等待窗口的显示，至少0.2秒
    global fullsc
    fullsc = ImageGrab.grab()

    Qmd5 = picmath(Qbox,'tmp/Qbox.jpg')
    #计算所有答案的md5
    Amd5 = picmath(Abox,'tmp/tmpA.jpg')
    Bmd5 = picmath(Bbox,'tmp/tmpB.jpg')
    Cmd5 = picmath(Cbox,'tmp/tmpC.jpg')
    Dmd5 = picmath(Dbox,'tmp/tmpD.jpg')

    if Qmd5 in hashDictS:           #check dict1 题目是否存在
         ##第一次查询题目对应的答案
        getanswer1 = hashDictS.get(Qmd5)
        if Amd5 == getanswer1:
            clickClient(getbrow,(465,580))          #A
            clickClient(getbrow,(505,715))          #post
        elif Bmd5 == getanswer1:
            clickClient(getbrow,(465,605))          #B
            clickClient(getbrow,(505,715))          #post
        elif Cmd5 == getanswer1:
            clickClient(getbrow,(465,630))          #C
            clickClient(getbrow,(505,715))          #post
        elif Dmd5 == getanswer1:
            clickClient(getbrow,(465,655))          #D
            clickClient(getbrow,(505,715))          #post
        else:
            time.sleep(0.5)
            Q2md5 = picmath(Q2box,'tmp/tmpQbox2.jpg')
            AllQmd5 = hashlib.md5('%s%s' %(Qmd5,Q2md5)).hexdigest().upper()

            if AllQmd5 in hashDictP:           #check dict2 题目是否存在
                getanswer2 = hashDictP.get(AllQmd5)
                if Amd5 == getanswer2:
                    clickClient(getbrow,(465,580))          #A
                    clickClient(getbrow,(505,715))          #post
                elif Bmd5 == getanswer2:
                    clickClient(getbrow,(465,605))          #B
                    clickClient(getbrow,(505,715))          #post
                elif Cmd5 == getanswer2:
                    clickClient(getbrow,(465,630))          #C
                    clickClient(getbrow,(505,715))          #post
                elif Dmd5 == getanswer2:
                    clickClient(getbrow,(465,655))          #D
                    clickClient(getbrow,(505,715))          #post
            else:
                print 'no answer!'
    else:
        print 'no this question in hashdict!!'

    #判斷當前進度
    Pmd5 = picmath(Pcbox,'tmp/Process.jpg')
    if Pmd5 != Pcmd5 :
        clickClient(getbrow,(990,725))          #点击下一题
        AutoAnswer()            #答题循环
    else:
        print 'finish!'
        clickClient(getbrow,(265,880))          #交卷
        time.sleep(0.1)
        clickClient(getbrow,(570,680))          #最后确定

if __name__ == '__main__':
    AutoAnswer()
