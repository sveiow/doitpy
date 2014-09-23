#coding=utf-8
#Introduction:AutoAnswer modules
from PIL import Image,ImageGrab
import win32gui,win32con,win32api
import logging,os,time
import hashlib,pickle

Amd5 = '7CA56AFFDB99389C7226FF8D94052123'
Bmd5 = 'C7120A8FB270149857FBBCD4B584268F'
Cmd5 = 'D7AECBB4A882D2D91EFD04BAFFA9D8FB'
Dmd5 = '3623FA6E08205C263CCBDEC0D37541B9'
Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'
ButtunT = 'BB54913D762C90152D4071BA66795C6A'
ButtunF = '0608E1F2485E0706D1DD7272A43F5A3F'

Qbox = (515,470,1020,488)
Q2box = (860,505,1050,655)
Abox = (510,564,840,586)
Bbox = (510,590,840,612)
Cbox = (510,617,840,639)
Dbox = (510,644,840,666)
Pcbox = (630,760,690,785)
Tipsbox = (690,710,705,725)
Button = (410,705,575,740)

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

#载入字典
def loadict(dictfile):
    output = open(dictfile, 'rb')
    hashdict = pickle.load(output)
    return hashdict

#鼠标模拟
def clickClient(handle,pos):
    coordinate = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(handle,win32con.WM_ACTIVATE,win32con.WA_ACTIVE,0)          #这里应该是控制前台还是后台模拟
    win32api.SendMessage(handle,win32con.WM_LBUTTONDOWN,win32con.MK_LBUTTON,coordinate)
    win32api.SendMessage(handle,win32con.WM_LBUTTONUP,win32con.MK_LBUTTON,coordinate)

#键盘模拟
def keyboard():
    win32api.keybd_event(17,0,0,0)
    win32api.keybd_event(86,0,0,0)
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

#导出日志
def oplog():
    logging.basicConfig(
        filename = os.path.join(os.getcwd(),'tmp', 'log.txt'),
        level = logging.INFO,
        datefmt = '%m-%d %H:%M',
        format = '%(asctime)s : %(message)s',
        filemode = 'a')
