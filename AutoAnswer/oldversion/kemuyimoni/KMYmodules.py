#coding=utf-8
#Introduction:KMYmodules
from PIL import Image,ImageGrab
import win32gui,win32con,win32api
import logging,os,time
import hashlib,pickle

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

#檢測字典是否已經存在
def wdict(dictfile,dic):
    if os.path.isfile(dictfile):
        oldict = open(dictfile,'rb')
        oldata = pickle.load(oldict)
        oldata.update(dic)      #新信息覆盖旧信息
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

#重新再来

