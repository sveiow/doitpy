#coding=utf-8
#Introduction:自動刷屏，刷廣告
#version:AutoAD
import os,time,hashlib,pickle
import win32gui,win32con,win32api
from PIL import Image,ImageGrab
from AAmodules import *

getbrow = win32gui.FindWindow('Chrome_WidgetWin_1',u'立秋·驾培-闯关王 - Google Chrome')            ##定义窗口
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##强行显示界面
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
win32gui.SetForegroundWindow(getbrow)           ##将浏览器窗口提到最前
time.sleep(0.8)         #等待窗口完全彈出

def picmath(box,filepath):
    fullsc = ImageGrab.grab()
    savepic = fullsc.crop(box).save(filepath,'JPEG')
    pic = open(filepath,'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5

def nextone():
    pic = picmath((630,760,690,785),'Button.JPG')
    if str(pic) == '54F84561323AE11EE1AA1C28290D7A17' :
##        clickClient(getbrow,(1067,379))           #关闭
        return
    else:
        clickClient(getbrow,(656,771))           #下一题
        sendAD()

def sendAD():
    count = 3
    while count > 0:
        clickClient(getbrow,(265,888))           #我要发言
        time.sleep(0.2)
        clickClient(getbrow,(256,775))           #点击对话框
        keyboard()          #SendMessage
        clickClient(getbrow,(212,892))           #发布
        count = count - 1
    nextone()

if __name__ == '__main__':
    sendAD()

