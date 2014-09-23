#coding=utf-8
#Introduction:AutoAnswer modules
from PIL import Image,ImageGrab
import win32gui,win32con,win32api
import logging,os,time
import hashlib,pickle

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

class KMY():
    Amd5 = '16BDFD6B3A116AA641D31562FE32C751'
    Bmd5 = '84B014D4C1FE3B01E3988EB5E5F7A7D5'
    Cmd5 = '192425926A9C14C09E9772030E824AB7'
    Dmd5 = '6C52EF5BF0C5F1A38C72EFD104EE9557'

    Qbox = (255,211,1070,226)
    Q2box = (867,290,1069,432)
    Abox = (245,303,600,318)
    Bbox = (245,330,600,345)
    Cbox = (245,357,600,372)
    Dbox = (245,384,600,399)
    Tipsbox = (401,413,421,426)

    Axy = (204,310)
    Bxy = (204,338)
    Cxy = (204,366)
    Dxy = (204,393)
    Submit = (270,425)
    Next = (340,565)

class LXC():
    Amd5 = '7CA56AFFDB99389C7226FF8D94052123'
    Bmd5 = 'C7120A8FB270149857FBBCD4B584268F'
    Cmd5 = 'D7AECBB4A882D2D91EFD04BAFFA9D8FB'
    Dmd5 = '3623FA6E08205C263CCBDEC0D37541B9'
    Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'
    BoxBlank = '782D92C2D53C89E7E10955A6F0349567'          #删除Q2box空白图片的KEY
    ButtunT = 'D5D6DCFB676ECB5E0F6EADFC7FB722DC'        #练习下一个知识点
    ButtunF = '9746ACEC9F40B01554E68B3A12D9F972'        #通关失败重做
    ButtunBlank = 'BE405EA30750B03FBA5B67921ACE2CBA'

    Qbox = (515,470,1020,488)
    Q2box = (860,505,1050,655)
    Abox = (510,564,840,586)
    Bbox = (510,590,840,612)
    Cbox = (510,617,840,639)
    Dbox = (510,644,840,666)
    Pcbox = (630,760,690,785)
    Tipsbox = (690,710,705,725)
    Button = (455,710,510,735)

    Axy = (465,580)
    Bxy = (465,605)
    Cxy = (465,630)
    Dxy = (465,655)
    Submit = (505,715)
    Next = (655,770)
    Handin = (1020,865)
    BT1 = (560,680)
    BT2 = (490,720)
