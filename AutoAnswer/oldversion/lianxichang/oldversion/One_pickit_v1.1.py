#coding=utf-8
#Introduction:基於Pickit_a3.1，單題收集 ----- for:闯关王——练兵场,正式可用,20140819
#version:One_pickit_v1.1
#updata v1.1:修改字典部分，修改Q2BOX，修改TIPSBOS，修改TIPSMD5
#updata v1.0:修改鼠標模擬的方式，解決鼠標失控問題（側面解決死循環）
#updata a3.1:細節整理，穩定可用
#updata a3.0:减少代码数量，但是截图次数增加了，运行块的次序需要整理
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
dict1 = {}
dict2_fpto = {}

Qbox = (515,470,1020,488)
Q2box = (860,505,1050,655)
Abox = (510,564,840,586)
Bbox = (510,590,840,612)
Cbox = (510,617,840,639)
Dbox = (510,644,840,666)
Pcbox = (630,760,690,785)
Tipsbox = (690,710,705,725)

Amd5 = '7CA56AFFDB99389C7226FF8D94052123'
Bmd5 = 'C7120A8FB270149857FBBCD4B584268F'
Cmd5 = 'D7AECBB4A882D2D91EFD04BAFFA9D8FB'
Dmd5 = '3623FA6E08205C263CCBDEC0D37541B9'
Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'

def clickClient(handle,pos):
    coordinate = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(handle,win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)          #这里应该是控制前台还是后台模拟
    win32api.SendMessage(handle,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,coordinate)
    win32api.SendMessage(handle,win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,coordinate)
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
    clickClient(getbrow,(465,580))          ##点击A
    clickClient(getbrow,(505,715))          ##提交答案
    time.sleep(0.5)         #减速等待

    fullsc = ImageGrab.grab()

    Qmd5 = picmath(Qbox,'tmp/Qbox.jpg')
        #为解决相同题目產生錯誤的问题，加入QBox2，再生成MD5
    Q2md5 = picmath(Q2box,'tmp/Qbox2.jpg')
        #截图，保存，提交答案之後查看正確答案
    Tipsmd5 = picmath(Tipsbox,'tmp/Tips.JPG')

    if Tipsmd5 == Amd5:
        dict1[Qmd5] = picmath(Abox,'tmp/A.jpg')
        dict2_fpto[Q2md5] = picmath(Abox,'tmp/A.jpg')

    elif Tipsmd5 == Bmd5:
        dict1[Qmd5] = picmath(Bbox,'tmp/B.jpg')
        dict2_fpto[Q2md5] = picmath(Bbox,'tmp/B.jpg')

    elif Tipsmd5 == Cmd5:
        dict1[Qmd5] = picmath(Cbox,'tmp/C.jpg')
        dict2_fpto[Q2md5] = picmath(Cbox,'tmp/C.jpg')

    elif Tipsmd5 == Dmd5:
        dict1[Qmd5] = picmath(Dbox,'tmp/D.jpg')
        dict2_fpto[Q2md5] = picmath(Dbox,'tmp/D.jpg')
    else:
        print 'no answer! no tips! cant catch!'

    if '782D92C2D53C89E7E10955A6F0349567' in dict2_fpto:            #判断、删除空白图片的KEY
        del dict2_fpto['782D92C2D53C89E7E10955A6F0349567']

    wdict('hashdata_a.pkl',dict1)
    wdict('dict2_fpto.pkl',dict2_fpto)

if __name__ == '__main__':
    Pickit()
