#coding=utf-8
#Introduction:自動答題 ----- for:for:闯关王——科目一
#version:Autoanswer_k0.1
from PIL import Image,ImageGrab
import win32gui,win32con,win32api
import os,time,hashlib
import pickle

getbrow = win32gui.FindWindow('Chrome_WidgetWin_1',u'模拟考试flash版 - Google Chrome')       ##定义窗口
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##强行显示界面
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
win32gui.SetForegroundWindow(getbrow)           ##将浏览器窗口提到最前
time.sleep(0.8)         #等待窗口完全彈出

#檢查工作目錄
if os.path.isdir('kmy'):
    pass
else:
    os.mkdir('kmy')

    #定義元素
Qbox = (255,211,1070,226)
Q2box = (867,290,1069,432)
Abox = (245,303,600,318)
Bbox = (245,330,600,345)
Cbox = (245,357,600,372)
Dbox = (245,384,600,399)

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

hashDS = loadict('DictS.kmy')
hashDP = loadict('DictP.kmy')

def AutoAnswer():
    time.sleep(0.3)
    global fullsc
    fullsc = ImageGrab.grab()

    Qmd5 = picmath(Qbox,'kmy/Qbox.jpg')
    #计算所有答案的md5
    Amd5 = picmath(Abox,'kmy/A.jpg')
    Bmd5 = picmath(Bbox,'kmy/B.jpg')
    Cmd5 = picmath(Cbox,'kmy/C.jpg')
    Dmd5 = picmath(Dbox,'kmy/D.jpg')

    if Qmd5 in hashDS:
        Gans1 = hashDS.get(Qmd5)
        if Amd5 == Gans1:
            clickClient(getbrow,(204,310));clickClient(getbrow,(270,425))
        elif Bmd5 == Gans1:
            clickClient(getbrow,(204,338));clickClient(getbrow,(270,425))
        elif Cmd5 == Gans1:
            clickClient(getbrow,(204,366));clickClient(getbrow,(270,425))
        elif Dmd5 == Gans1:
            clickClient(getbrow,(204,393));clickClient(getbrow,(270,425))
        else:
            time.sleep(0.5)
            Q2md5 = picmath(Q2box,'kmy/Q2box.jpg')
            if Q2md5 in hashDP:
                Gans2 = hashDP.get(Q2md5)
                if Amd5 == Gans2:
                    clickClient(getbrow,(204,310));clickClient(getbrow,(270,425))
                elif Bmd5 == Gans2:
                    clickClient(getbrow,(204,338));clickClient(getbrow,(270,425))
                elif Cmd5 == Gans2:
                    clickClient(getbrow,(204,366));clickClient(getbrow,(270,425))
                elif Dmd5 == Gans2:
                    clickClient(getbrow,(204,393));clickClient(getbrow,(270,425))
    else:
        time.sleep(0.5)
        Q2md5 = picmath(Q2box,'kmy/Q2box.jpg')
        if Q2md5 in hashDP:
            Gans2 = hashDP.get(Q2md5)
            if Amd5 == Gans2:
                clickClient(getbrow,(204,310));clickClient(getbrow,(270,425))
            elif Bmd5 == Gans2:
                clickClient(getbrow,(204,338));clickClient(getbrow,(270,425))
            elif Cmd5 == Gans2:
                clickClient(getbrow,(204,366));clickClient(getbrow,(270,425))
            elif Dmd5 == Gans2:
                clickClient(getbrow,(204,393));clickClient(getbrow,(270,425))

    clickClient(getbrow,(340,565))


if __name__ == '__main__':
    count = 1
    for count in range(100):
        AutoAnswer()
