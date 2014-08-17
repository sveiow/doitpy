#coding=utf-8
#介绍：CHECHBOX FOR 练习场
from PIL import Image
import ImageGrab
import os
import time
import win32gui
import win32con
import win32api

getbrow = win32gui.FindWindow('Chrome_WidgetWin_1',u'立秋·驾培-闯关王 - Google Chrome')            ##定义窗口
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##强行显示界面
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
win32gui.SetForegroundWindow(getbrow)           ##将浏览器窗口提到最前
time.sleep(1)         #等待窗口完全彈出

#檢查工作目錄
if os.path.isdir('checking'):
    pass
else:
    os.mkdir('checking')
    
fullsc = ImageGrab.grab()
def savepic(boxname,filename):
    fullsc.crop(boxname).save(filename,'JPEG')

Qbox = (515,470,1020,488);savepic(Qbox,'checking/Qbox.jpg');
Q2box = (860,500,1050,655);savepic(Q2box,'checking/Qbox2.jpg');
Abox = (510,564,840,586);savepic(Abox,'checking/Abox.jpg');
Bbox = (510,590,840,612);savepic(Bbox,'checking/Bbox.jpg');
Cbox = (510,617,840,639);savepic(Cbox,'checking/Cbox.jpg');
Dbox = (510,644,840,666);savepic(Dbox,'checking/Dbox.jpg');
Tipsbox = (690,705,705,725);savepic(Tipsbox,'checking/Tipsbox.jpg');
button1 = (410,705,575,740);savepic(button1,'checking/button1.jpg');
