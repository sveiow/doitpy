#coding=utf-8
#Introduction:题目收集 ----- for:闯关王——科目一,20140909
#version:Pickit_k0.2
from PIL import Image,ImageGrab
import win32gui,win32con,win32api
import logging,os,time
import hashlib,pickle
from KMYmodules import *

getbrow = win32gui.FindWindow('Chrome_WidgetWin_1',u'模拟考试flash版 - Google Chrome')            ##定义窗口
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##强行显示界面
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
win32gui.SetForegroundWindow(getbrow)           ##将浏览器窗口提到最前
time.sleep(0.8)         #等待窗口完全彈出

#檢查工作目錄
if os.path.isdir('kmy'):
    pass
else:
    os.mkdir('kmy')

DictS = {}
DictP = {}

def do():
    count = 0;
    for count in range (100):
        time.sleep(0.2)
        clickClient(getbrow,(204,310))          ##点击A
        clickClient(getbrow,(270,425))          ##提交答案
        clickClient(getbrow,(340,565))          ##下一题
    time.sleep(0.2)
    clickClient(getbrow,(185,605))          ##返回第 1题

def picmath(box,filepath):
    savepic = fullsc.crop(box).save(filepath,'JPEG')
    pic = open(filepath,'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5

def OnePick():
    time.sleep(1)
    global fullsc
    fullsc = ImageGrab.grab()

    Qmd5 = picmath(Qbox,'kmy/Qbox.jpg')
    Q2md5 = picmath(Q2box,'kmy/Qbox2.jpg')
    Tipsmd5 = picmath(Tipsbox,'kmy/Tips.JPG')

    if Tipsmd5 == Amd5:
        DictS[Qmd5] = picmath(Abox,'kmy/A.jpg')
        DictP[Q2md5] = picmath(Abox,'kmy/A.jpg')

    elif Tipsmd5 == Bmd5:
        DictS[Qmd5] = picmath(Bbox,'kmy/B.jpg')
        DictP[Q2md5] = picmath(Bbox,'kmy/B.jpg')

    elif Tipsmd5 == Cmd5:
        DictS[Qmd5] = picmath(Cbox,'kmy/C.jpg')
        DictP[Q2md5] = picmath(Cbox,'kmy/C.jpg')

    elif Tipsmd5 == Dmd5:
        DictS[Qmd5] = picmath(Dbox,'kmy/D.jpg')
        DictP[Q2md5] = picmath(Dbox,'kmy/D.jpg')
    else:
        print "cant catch!"

    if '674D6AEA2013C3019B9B6B02E32D647B' in DictP:            #判断、删除空白图片的KEY
        del DictP['674D6AEA2013C3019B9B6B02E32D647B']
    wdict('DictS.kmy',DictS)
    wdict('DictP.kmy',DictP)

#開始收集
def Pickit():
    time.sleep(1)
    global fullsc
    fullsc = ImageGrab.grab()

    Qmd5 = picmath(Qbox,'kmy/Qbox.jpg')
    Q2md5 = picmath(Q2box,'kmy/Qbox2.jpg')
    Tipsmd5 = picmath(Tipsbox,'kmy/Tips.JPG')

    if Tipsmd5 == Amd5:
        DictS[Qmd5] = picmath(Abox,'kmy/A.jpg')
        DictP[Q2md5] = picmath(Abox,'kmy/A.jpg')

    elif Tipsmd5 == Bmd5:
        DictS[Qmd5] = picmath(Bbox,'kmy/B.jpg')
        DictP[Q2md5] = picmath(Bbox,'kmy/B.jpg')

    elif Tipsmd5 == Cmd5:
        DictS[Qmd5] = picmath(Cbox,'kmy/C.jpg')
        DictP[Q2md5] = picmath(Cbox,'kmy/C.jpg')

    elif Tipsmd5 == Dmd5:
        DictS[Qmd5] = picmath(Dbox,'kmy/D.jpg')
        DictP[Q2md5] = picmath(Dbox,'kmy/D.jpg')
    else:
        print "no answer! no tips! cant catch!"

    time.sleep(0.3)
    clickClient(getbrow,(340,565))          ##下一题
#結束收集

def main():
    do()
    count = 0
    for count in range (100):
        Pickit()

    if '674D6AEA2013C3019B9B6B02E32D647B' in DictP:            #判断、删除空白图片的KEY
        del DictP['674D6AEA2013C3019B9B6B02E32D647B']
    wdict('DictS.kmy',DictS)
    wdict('DictP.kmy',DictP)

    clickClient(getbrow,(985,565))          ##交卷
    clickClient(getbrow,(575,480))          ##时间未到
    clickClient(getbrow,(635,480))          ##确认
    clickClient(getbrow,(985,565))          ##重来
    time.sleep(2)

    print len(DictS);DictS.clear()
    print len(DictP);DictP.clear()

if __name__ == '__main__':
    print u"""
按題收集，按 1
按套收集，按 2
离开，随便按
"""
    cho = raw_input('')
    if cho == '1':
        OnePick()
    elif cho =='2':
        count = 0
        for count in range(10):
            main()
            print count
    else:
        exit()

