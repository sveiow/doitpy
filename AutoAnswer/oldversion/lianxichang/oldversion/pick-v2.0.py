#coding:gbk
#pick1沒問題版，待優化，version:1.0

import win32gui
import win32con

getbrow = win32gui.FindWindow("Chrome_WidgetWin_1","立秋·驾培-闯关王 - Google Chrome")         ##定义窗口
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##强行显示界面
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
win32gui.SetForegroundWindow(getbrow)           ##将浏览器窗口提到最前

from PIL import Image
import ImageGrab
import os
import hashlib

shash = os.getcwd() + '/hash/1.dict'
hashp = os.getcwd() + '/hash'       ##os.getcwd獲取當前工作目錄
if os.path.exists(hashp):
    pass
else:
    os.mkdir('hash')
    
wokingp = os.getcwd() + '/tmp/'
if os.path.exists(wokingp):
    pass
else:
    os.mkdir('tmp')
    
import win32api

def getit():
    ##def click(x,y)          #测试一
    ##    win32api.SetCursorPos([x,y])
    ##    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    ##    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)


    ##点击A
    ##A = (465,580)          #测试一
    ##A.click()
    Ax = 465          #方法一
    Ay = 580
    win32api.SetCursorPos([Ax,Ay])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,Ax,Ay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,Ax,Ay)

    import time

    ##提交答案
    put_x = 505
    put_y = 715
    win32api.SetCursorPos([put_x,put_y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,put_x,put_y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,put_x,put_y)

    time.sleep(0.5)

    fullsc = ImageGrab.grab()               ##截全圖
    Qbox = (515,470,1020,488)               ##題目盒子
    Abox = (510,564,840,586)
    Bbox = (510,590,840,612)
    Cbox = (510,617,840,639)
    Dbox = (510,644,840,666)
    Tipsbox = (690,705,705,725)

    simageQ = fullsc.crop(Qbox).save(wokingp + 'imageQ.jpg','JPEG')         #截图，保存
    picQ = open(wokingp +'imageQ.jpg','rb')
    Qmd5 = hashlib.md5(picQ.read()).hexdigest()         ##計算題目Q的MD5

    ##getipsc = ImageGrab.grab()          ##为获取答案而截图

    sTips = fullsc.crop(Tipsbox).save(wokingp + 'Tips.JPG','JPEG')         #截图，保存，提交答案之後查看正確答案
    Tips = open(wokingp +'Tips.JPG','rb')
    Tipsmd5 = hashlib.md5(Tips.read()).hexdigest().upper()
    Amd5 = '2B964BCA9F554C660C5418561AFFF177'
    Bmd5 = 'B34D3B3B460019BA8625BAE5EEFE91B1'
    Cmd5 = 'BA8A8CF9E8669E09EDB63832B60338D7'
    Dmd5 = 'D0C5378938E2CC34C6CB30867FD5C6BB'


    if Tipsmd5 == Amd5:
        simageA = fullsc.crop(Abox).save(wokingp + 'imageA.jpg','JPEG')
        picA = open(wokingp +'imageA.jpg','rb')
        Amd5 = hashlib.md5(picA.read()).hexdigest()         ##計算答案A的MD5
        w = '%s : %s \n' % (Qmd5 ,Amd5)          ##寫入HASH至文件
        tk = open(shash,'a')
        tk.write(w)
        tk.close()
        picA.close()
        
    elif Tipsmd5 == Bmd5:
        simageB = fullsc.crop(Bbox).save(wokingp + 'imageB.jpg','JPEG')
        picB = open(wokingp +'imageB.jpg','rb')
        Bmd5 = hashlib.md5(picB.read()).hexdigest()         ##計算答案B的MD5
        w = '%s : %s \n' % (Qmd5 ,Bmd5)          ##寫入HASH至文件
        tk = open(shash,'a')
        tk.write(w)
        tk.close()
        picB.close()
        
    elif Tipsmd5 == Cmd5:
        simageC = fullsc.crop(Cbox).save(wokingp + 'imageC.jpg','JPEG')
        picC = open(wokingp +'imageC.jpg','rb')
        Cmd5 = hashlib.md5(picC.read()).hexdigest()         ##計算答案C的MD5
        w = '%s : %s \n' % (Qmd5 ,Cmd5)          ##寫入HASH至文件
        tk = open(shash,'a')
        tk.write(w)
        tk.close()
        picC.close()
        
    elif Tipsmd5 == Dmd5:
        simageD = fullsc.crop(Dbox).save(wokingp + 'imageD.jpg','JPEG')
        picD = open(wokingp +'imageD.jpg','rb')
        Dmd5 = hashlib.md5(picD.read()).hexdigest()         ##計算答案D的MD5
        w = '%s : %s \n' % (Qmd5 ,Dmd5)          ##寫入HASH至文件
        tk = open(shash,'a')
        tk.write(w)
        tk.close()
        picD.close()
    else:
        print 'no answer!'

    #判斷當前進度
fullsc = ImageGrab.grab()               ##截全圖
Pcbox = (630,760,690,785)           #進度條
sProcess = fullsc.crop(Pcbox).save(wokingp + 'Process.jpg','JPEG')         #截图，保存
Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'
picPc = open(wokingp +'Process.jpg','rb')
Pmd5 = hashlib.md5(picPc.read()).hexdigest().upper()
picPc.close()

if Pmd5 != Pcmd5 :
    nextx = 655          #点击下一题
    nexty = 770
    win32api.SetCursorPos([nextx,nexty])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,nextx,nexty)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,nextx,nexty)
    getit()
else:
    print 'finish'
