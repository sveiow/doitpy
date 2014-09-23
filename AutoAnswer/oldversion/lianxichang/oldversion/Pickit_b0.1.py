#coding=utf-8
#Introduction:题目收集-----for:闯关王——练兵场,正式可用,20140819
#version:Pickit_b0.1
#updata b0.1:合并两个Pick
from PIL import Image,ImageGrab
import win32gui,win32con,win32api
import logging,os,time
import hashlib,pickle
from AAmodules import *

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

def picmath(box,filepath):
    savepic = fullsc.crop(box).save(filepath,'JPEG')
    pic = open(filepath,'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5

DictS = {}
DictP = {}

#單節收集
def Pickit():
    time.sleep(0.5)         #减速 这里数值可以增大
    clickClient(getbrow,(465,580))          ##点击A
    clickClient(getbrow,(505,715))          ##提交答案
    time.sleep(1)         #减速等待

    global fullsc
    fullsc = ImageGrab.grab()
    Qmd5 = picmath(Qbox,'tmp/Qbox.jpg')
    Q2md5 = picmath(Q2box,'tmp/Qbox2.jpg')
    Tipsmd5 = picmath(Tipsbox,'tmp/Tips.JPG')

    if Tipsmd5 == Amd5:
        DictS[Qmd5] = picmath(Abox,'tmp/A.jpg')
        DictP[Q2md5] = picmath(Abox,'tmp/A.jpg')

    elif Tipsmd5 == Bmd5:
        DictS[Qmd5] = picmath(Bbox,'tmp/B.jpg')
        DictP[Q2md5] = picmath(Bbox,'tmp/B.jpg')

    elif Tipsmd5 == Cmd5:
        DictS[Qmd5] = picmath(Cbox,'tmp/C.jpg')
        DictP[Q2md5] = picmath(Cbox,'tmp/C.jpg')

    elif Tipsmd5 == Dmd5:
        DictS[Qmd5] = picmath(Dbox,'tmp/D.jpg')
        DictP[Q2md5] = picmath(Dbox,'tmp/D.jpg')
    else:
        print 'no answer! no tips! cant catch!'

    #判斷當前進度
    Pmd5 = picmath(Pcbox,'tmp/Process.jpg')

    if Pmd5 != Pcmd5 :
        clickClient(getbrow,(655,770))          #点击下一题
        Pickit()            #查题循环
    else:
        if '782D92C2D53C89E7E10955A6F0349567' in DictP:            #判断、删除空白图片的KEY
            del DictP['782D92C2D53C89E7E10955A6F0349567']
        wdict('DictS.part',DictS)
        wdict('DictP.part',DictP)
        print 'finish'

def OnePickit():
    time.sleep(0.5)         #减速 这里数值可以增大
    clickClient(getbrow,(465,580))          ##点击A
    clickClient(getbrow,(505,715))          ##提交答案
    time.sleep(1)         #减速等待

    global fullsc
    fullsc = ImageGrab.grab()
    Qmd5 = picmath(Qbox,'tmp/Qbox.jpg')
    Q2md5 = picmath(Q2box,'tmp/Qbox2.jpg')
    Tipsmd5 = picmath(Tipsbox,'tmp/Tips.JPG')

    if Tipsmd5 == Amd5:
        DictS[Qmd5] = picmath(Abox,'tmp/A.jpg')
        DictP[Q2md5] = picmath(Abox,'tmp/A.jpg')

    elif Tipsmd5 == Bmd5:
        DictS[Qmd5] = picmath(Bbox,'tmp/B.jpg')
        DictP[Q2md5] = picmath(Bbox,'tmp/B.jpg')

    elif Tipsmd5 == Cmd5:
        DictS[Qmd5] = picmath(Cbox,'tmp/C.jpg')
        DictP[Q2md5] = picmath(Cbox,'tmp/C.jpg')

    elif Tipsmd5 == Dmd5:
        DictS[Qmd5] = picmath(Dbox,'tmp/D.jpg')
        DictP[Q2md5] = picmath(Dbox,'tmp/D.jpg')
    else:
        print 'no answer! no tips! cant catch!'

    if '782D92C2D53C89E7E10955A6F0349567' in DictP:            #判断、删除空白图片的KEY
        del DictP['782D92C2D53C89E7E10955A6F0349567']
    wdict('DictS.part',DictS)
    wdict('DictP.part',DictP)

if __name__ == '__main__':
    print u"""
    小节收集，按 1
    单题收集，按 2
    离开，随便按
    """
    cho = raw_input(' ')
    if cho == '1':
        Pickit()
    elif cho =='2':
        OnePickit()
    else:
        exit()
        
