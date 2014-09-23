#coding=gbk
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

#檢查工作目錄
if os.path.exists('kmy') == False: os.mkdir('kmy')
if os.path.exists('Dict') == False: os.mkdir('Dict')

try:
    DictS = loadict(os.path.join('Dict','DictS.K'))
    DictP = loadict(os.path.join('Dict','DictP.K'))
except IOError:
    win32api.MessageBox(0, str("没找到字典，程式退出！"), "错误", win32con.MB_ICONINFORMATION)
    exit()

HashS = {}
HashP = {}

def PicHash(box,filepath):
    savepic = fullsc.crop(box).save(os.path.join('kmy',filepath),'JPEG')
    pic = open(os.path.join('kmy',filepath),'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5

def Answer():
    time.sleep(0.2)
    global fullsc
    fullsc = ImageGrab.grab()

    Qmd5 = PicHash(KMY.Qbox,'Qbox.jpg')
    #计算所有答案的md5
    Amd5 = PicHash(KMY.Abox,'A.jpg')
    Bmd5 = PicHash(KMY.Bbox,'B.jpg')
    Cmd5 = PicHash(KMY.Cbox,'C.jpg')
    Dmd5 = PicHash(KMY.Dbox,'D.jpg')

    if Qmd5 in DictS:
        Gans1 = DictS.get(Qmd5)
        if Amd5 == Gans1:
            clickClient(getbrow,KMY.Axy)
            clickClient(getbrow,KMY.Submit)
        elif Bmd5 == Gans1:
            clickClient(getbrow,KMY.Bxy)
            clickClient(getbrow,KMY.Submit)
        elif Cmd5 == Gans1:
            clickClient(getbrow,KMY.Cxy)
            clickClient(getbrow,KMY.Submit)
        elif Dmd5 == Gans1:
            clickClient(getbrow,KMY.Dxy)
            clickClient(getbrow,KMY.Submit)
        else:
            time.sleep(0.5)
            Q2md5 = PicHash(KMY.Q2box,'Q2box.jpg')
            if Q2md5 in DictP:
                Gans2 = DictP.get(Q2md5)
                if Amd5 == Gans2:
                    clickClient(getbrow,KMY.Axy)
                    clickClient(getbrow,KMY.Submit)
                elif Bmd5 == Gans2:
                    clickClient(getbrow,KMY.Bxy)
                    clickClient(getbrow,KMY.Submit)
                elif Cmd5 == Gans2:
                    clickClient(getbrow,KMY.Cxy)
                    clickClient(getbrow,KMY.Submit)
                elif Dmd5 == Gans2:
                    clickClient(getbrow,KMY.Dxy)
                    clickClient(getbrow,KMY.Submit)
    else:
        time.sleep(0.5)
        Q2md5 = PicHash(KMY.Q2box,'Q2box.jpg')
        if Q2md5 in DictP:
            Gans2 = DictP.get(Q2md5)
            if Amd5 == Gans2:
                clickClient(getbrow,KMY.Axy)
                clickClient(getbrow,KMY.Submit)
            elif Bmd5 == Gans2:
                clickClient(getbrow,KMY.Bxy)
                clickClient(getbrow,KMY.Submit)
            elif Cmd5 == Gans2:
                clickClient(getbrow,KMY.Cxy)
                clickClient(getbrow,KMY.Submit)
            elif Dmd5 == Gans2:
                clickClient(getbrow,KMY.Dxy)
                clickClient(getbrow,KMY.Submit)

def Pick():
    time.sleep(1)
    global fullsc
    fullsc = ImageGrab.grab()

    Qmd5 = PicHash(KMY.Qbox,'tmpQbox.jpg')
    Q2md5 = PicHash(KMY.Q2box,'tmpQbox2.jpg')
    Tipsmd5 = PicHash(KMY.Tipsbox,'tmpTips.JPG')

    if Tipsmd5 == KMY.Amd5:
        HashS[Qmd5] = PicHash(KMY.Abox,'tmpA.jpg')
        HashP[Q2md5] = PicHash(KMY.Abox,'tmpA.jpg')

    elif Tipsmd5 == KMY.Bmd5:
        HashS[Qmd5] = PicHash(KMY.Bbox,'tmpB.jpg')
        HashP[Q2md5] = PicHash(KMY.Bbox,'tmpB.jpg')

    elif Tipsmd5 == KMY.Cmd5:
        HashS[Qmd5] = PicHash(KMY.Cbox,'tmpC.jpg')
        HashP[Q2md5] = PicHash(KMY.Cbox,'tmpC.jpg')

    elif Tipsmd5 == KMY.Dmd5:
        HashS[Qmd5] = PicHash(KMY.Dbox,'tmpD.jpg')
        HashP[Q2md5] = PicHash(KMY.Dbox,'tmpD.jpg')
    else:
        print "cant catch!"

#===============================================================================
def Do():
    for count in range (100):
        time.sleep(0.2)
        clickClient(getbrow,KMY.Axy)          ##点击A
        clickClient(getbrow,KMY.Submit)          ##提交答案
        clickClient(getbrow,KMY.Next)          ##下一题
    time.sleep(0.2)
    clickClient(getbrow,(185,605))          ##返回第 1题

def AutoAnswer():
    for count in range(100):
        Answer()
        clickClient(getbrow,KMY.Next)

def Pickit(x):
    x = raw_input('')
    for count in range(x):
        Do()
        for Qcount in range (100):
            Pick()
            clickClient(getbrow,KMY.Next)

        if KMY.BoxBlank in HashP:            #判断、删除空白图片的KEY
            del HashP[KMY.BoxBlank]
        wdict('DictS.KM',HashS)
        wdict('DictP.KM',HashP)

        clickClient(getbrow,KMY.HnA)
        clickClient(getbrow,KMY.BT1)
        clickClient(getbrow,KMY.Confirm)
        clickClient(getbrow,KMY.HnA)

        print len(HashS);HashS.clear()
        print len(HashP);HashP.clear()

def OnePickit():
    clickClient(getbrow,KMY.Axy)          ##点击A
    clickClient(getbrow,KMY.Submit)          ##提交答案
    Pick()
    if KMY.BoxBlank in HashP:            #判断、删除空白图片的KEY
        del HashP[KMY.BoxBlank]
    wdict('oneDictS.KMY',HashS)
    wdict('oneDictP.KMY',HashP)

getbrow = win32gui.FindWindow('Chrome_WidgetWin_1','模拟考试flash版 - Google Chrome')

choice = """===== 科目一模拟考试程式 =====
输入(1)，进入自动答题
输入(2)，进入单题收集
输入(3)，进入整套收集
输入(Q)，离开

Enter choice:"""

choice = raw_input(choice).strip()[0].lower()
if choice == 'q' or choice not in ['1','2','3']:
    exit()
else:
    win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##强行显示界面
    win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
    win32gui.SetForegroundWindow(getbrow)           ##将浏览器窗口提到前台
    time.sleep(0.8)         #等待窗口完全彈出

cho = {
    '1':AutoAnswer,
    '2':OnePickit,
    '3':Pickit,
    }
cho.get(choice)()
