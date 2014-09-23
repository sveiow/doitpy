#coding=utf-8
#version:semiauto_pickit_a0.1
#updata a0.1:基於v0.5的重寫
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
hashdict = {}
hashdict_v2 = {}

Qbox = (515,470,1020,488)
Q2box = (860,500,1050,655)
Abox = (510,564,840,586)
Bbox = (510,590,840,612)
Cbox = (510,617,840,639)
Dbox = (510,644,840,666)
Pcbox = (630,760,690,785)
Tipsbox = (690,705,705,725)
Button = (410,705,575,740)

Amd5 = '2B964BCA9F554C660C5418561AFFF177'
Bmd5 = 'B34D3B3B460019BA8625BAE5EEFE91B1'
Cmd5 = 'BA8A8CF9E8669E09EDB63832B60338D7'
Dmd5 = 'D0C5378938E2CC34C6CB30867FD5C6BB'
Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'
ButtunT = 'BB54913D762C90152D4071BA66795C6A'
ButtunF = '0608E1F2485E0706D1DD7272A43F5A3F'

def click(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)
        #檢測字典是否已經存在
def wdict(dictfile,dic):
    if os.path.isfile(dictfile):
        oldict = open(dictfile,'rb')
        oldata = pickle.load(oldict)
        oldata.update(dic)
        output = open(dictfile,'wb')
        pickle.dump(oldata,output)
        output.close()
    else:
        with open(dictfile,'wb') as output:
            pickle.dump(dic,output)
        output.close()

def loadict(dictfile):
    output = open(dictfile, 'rb')
    hashdict = pickle.load(output)
    return hashdict

def nextclass():
    def picmath(box,filepath):
        savepic = fullsc.crop(box).save(filepath,'JPEG')
        pic = open(filepath,'rb')
        md5 = hashlib.md5(pic.read()).hexdigest().upper()
        pic.close()
        return md5

    click(1020,865)          #交卷
    time.sleep(0.3)
    click(560,680)          #未完成提示框的確認
    time.sleep(1)

    fullsc = ImageGrab.grab()
    Buttunmd5 = picmath(Button,'tmp/Button.JPG')
    if Buttunmd5 == ButtunT:
        click(490,720)          #練習下一個知識點
        Pickit()
    elif Buttunmd5 == ButtunF:
        click(490,720)          #失敗重做
        AutoAnswer()
    else:
        print 'all this chapter finish!'
        return
    #結束

#開始收集
def Pickit():
    def picmath(box,filepath):
        savepic = fullsc.crop(box).save(filepath,'JPEG')
        pic = open(filepath,'rb')
        md5 = hashlib.md5(pic.read()).hexdigest().upper()
        pic.close()
        return md5

    time.sleep(0.5)         #减速 这里数值可以增大
    click(465,580)          ##点击A
    click(505,715)          ##提交答案
    time.sleep(0.5)         #减速等待

    fullsc = ImageGrab.grab()

    Qmd5 = picmath(Qbox,'tmp/Qbox.jpg')
        #为解决相同题目產生錯誤的问题，加入QBox2，再生成MD5
    Q2md5 = picmath(Q2box,'tmp/Qbox2.jpg')
    AllQmd5 = hashlib.md5('%s%s' %(Qmd5,Q2md5)).hexdigest().upper()
        #截图，保存，提交答案之後查看正確答案
    Tipsmd5 = picmath(Tipsbox,'tmp/Tips.JPG')

    if Tipsmd5 == Amd5:
        hashdict[Qmd5] = picmath(Abox,'tmp/A.jpg')
        hashdict_v2[AllQmd5] = picmath(Abox,'tmp/A.jpg')

    elif Tipsmd5 == Bmd5:
        hashdict[Qmd5] = picmath(Bbox,'tmp/B.jpg')
        hashdict_v2[AllQmd5] = picmath(Bbox,'tmp/B.jpg')

    elif Tipsmd5 == Cmd5:
        hashdict[Qmd5] = picmath(Cbox,'tmp/C.jpg')
        hashdict_v2[AllQmd5] = picmath(Cbox,'tmp/C.jpg')

    elif Tipsmd5 == Dmd5:
        hashdict[Qmd5] = picmath(Dbox,'tmp/D.jpg')
        hashdict_v2[AllQmd5] = picmath(Dbox,'tmp/D.jpg')
    else:
        print 'no answer! no tips! cant catch!'

    #判斷當前進度
    Pmd5 = picmath(Pcbox,'tmp/Process.jpg')

    if Pmd5 != Pcmd5 :
        click(655,770)          #点击下一题
        Pickit()            #查题循环
    else:
        wdict('hashdata_v1.pkl',hashdict)
        wdict('hashdata_v2.pkl',hashdict_v2)
        print 'finish, next chapter!'
        nextclass()
#結束收集

#開始做題
def AutoAnswer():
    hashdictv1 = loadict('hashdata_v1.pkl')         #導入字典
    hashdictv2 = loadict('hashdata_v2.pkl')
    def picmath(box,filepath):
        savepic = fullsc.crop(box).save(filepath,'JPEG')
        pic = open(filepath,'rb')
        md5 = hashlib.md5(pic.read()).hexdigest().upper()
        pic.close()
        return md5

    time.sleep(0.5)         #截图前，降速等待窗口的显示，至少0.2秒
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
        click(655,770)          #点击下一题
        AutoAnswer()            #查题循环
    else:
        print 'finish, next chapter!'
        nextclass()
#結束做題

if __name__ == '__main__':
    Pickit()
