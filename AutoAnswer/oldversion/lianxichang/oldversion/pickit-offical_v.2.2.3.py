#coding=utf-8
#介紹：基於2.2.2的測試
#version:pickit_offical_v2.2.3，for:闯关王——练兵场
#updata 2.2.3:修改wdict()
#updata 2.2.2:修改字典更新方式
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

Amd5 = '2B964BCA9F554C660C5418561AFFF177'
Bmd5 = 'B34D3B3B460019BA8625BAE5EEFE91B1'
Cmd5 = 'BA8A8CF9E8669E09EDB63832B60338D7'
Dmd5 = 'D0C5378938E2CC34C6CB30867FD5C6BB'
Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'

def click(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)

        #檢測字典是否已經存在
def wdict(dictfile,dict):
    if os.path.isfile(dictfile):
        oldict = open(dictfile,'rb')
        oldata = pickle.load(oldict)
        oldata.update(dict)
        output = open(dictfile,'wb')
        pickle.dump(oldata,output)
        output.close()
    else:
        with open(dictfile,'wb') as output:
            pickle.dump(dict,output)
        output.close()
    #結束

    #開始收集
def pickit():
    time.sleep(0.5)         #减速 这里数值可以增大
    click(465,580)          ##点击A
    click(505,715)          ##提交答案

    time.sleep(0.5)         #减速等待
    fullsc = ImageGrab.grab()               ##截全圖，因爲是pick工作，所以提交答案再截圖

    saveQ = fullsc.crop(Qbox).save('tmp/Qbox.jpg','JPEG')
    picQ = open('tmp/Qbox.jpg','rb')
    Qmd5 = hashlib.md5(picQ.read()).hexdigest().upper()

        #为解决相同题目產生錯誤的问题，加入QBox2，再生成MD5
    saveQ2 = fullsc.crop(Q2box).save('tmp/Qbox2.jpg','JPEG')
    picQ2 = open('tmp/Qbox2.jpg','rb')
    Q2md5 = hashlib.md5(picQ.read()).hexdigest().upper()
    AllQmd5 = '%s%s' %(Qmd5,Q2md5)
    picQ.close(),picQ2.close()

    saveTips = fullsc.crop(Tipsbox).save('tmp/Tips.JPG','JPEG')         #截图，保存，提交答案之後查看正確答案
    Tips = open('tmp/Tips.JPG','rb')
    Tipsmd5 = hashlib.md5(Tips.read()).hexdigest().upper()
    Tips.close()

        #计算答案MD5
    def md5w():
        md5 = hashlib.md5(pic.read()).hexdigest().upper()
        hashdict[Qmd5] = md5           #單單題目區
        hashdict_v2[AllQmd5] = md5            #圖片區+題目區
        pic.close()

    if Tipsmd5 == Amd5:
        saveA = fullsc.crop(Abox).save('tmp/A.jpg','JPEG')
        pic = open('tmp/A.jpg','rb')
        md5w()

    elif Tipsmd5 == Bmd5:
        saveB = fullsc.crop(Bbox).save('tmp/B.jpg','JPEG')
        pic = open('tmp/B.jpg','rb')
        md5w()

    elif Tipsmd5 == Cmd5:
        saveC = fullsc.crop(Cbox).save('tmp/C.jpg','JPEG')
        pic = open('tmp/C.jpg','rb')
        md5w()

    elif Tipsmd5 == Dmd5:
        saveD = fullsc.crop(Dbox).save('tmp/D.jpg','JPEG')
        pic = open('tmp/D.jpg','rb')
        md5w()
    else:
        print 'no answer! no tips! cant catch!'

    getProcess()

    #判斷當前進度
def getProcess():
    fullsc = ImageGrab.grab()
    saveProcess = fullsc.crop(Pcbox).save('tmp/Process.jpg','JPEG')         #截图，保存
    picPc = open('tmp/Process.jpg','rb')
    Pmd5 = hashlib.md5(picPc.read()).hexdigest().upper()
    picPc.close()

    if Pmd5 != Pcmd5 :
        click(655,770)          #点击下一题
        pickit()            #查题循环
    else:
        wdict('hashdata_v1.pkl',hashdict)
        wdict('hashdata_v2.pkl',hashdict_v2)
        print 'finish'

if __name__ == '__main__':
    pickit()
