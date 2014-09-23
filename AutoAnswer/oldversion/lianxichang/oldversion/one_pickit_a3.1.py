#coding=utf-8
#介紹：基於2.2.2的測試
#version:pickit_a3.1，for:闯关王——练兵场
#updata a3.1:細節整理，穩定可用
#updata a3.0:减少代码数量，但是截图次数增加了，运行块的次序需要整理
#updata 2.2.3:修改wdict()
#updata 2.2.2:修改字典更新方式
##import profile

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

    wdict('hashdata_v1.pkl',hashdict)
    wdict('hashdata_v2.pkl',hashdict_v2)

if __name__ == '__main__':
    Pickit()
##    profile.run('Pickit()')           #性能分析
