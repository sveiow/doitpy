#coding=utf-8
#Introduction:题目收集 ----- for:闯关王——科目一
#version:Pickit_k0.1
from PIL import Image
import ImageGrab
import win32gui,win32con,win32api
import os,time,hashlib
import pickle

getbrow = win32gui.FindWindow('Chrome_WidgetWin_1',u'模拟考试flash版 - Google Chrome')            ##定义窗口
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
DictS = {}
DictP = {}

Qbox = (255,211,1070,226)
Q2box = (867,290,1069,432)
Abox = (245,303,600,318)
Bbox = (245,330,600,345)
Cbox = (245,357,600,372)
Dbox = (245,384,600,399)
Tipsbox = (401,413,421,426)

Amd5 = '16BDFD6B3A116AA641D31562FE32C751'
Bmd5 = '84B014D4C1FE3B01E3988EB5E5F7A7D5'
Cmd5 = '192425926A9C14C09E9772030E824AB7'
Dmd5 = '6C52EF5BF0C5F1A38C72EFD104EE9557'

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
        oldata.update(dic)      #新信息覆盖旧信息
        output = open(dictfile,'wb')
        pickle.dump(oldata,output)
        output.close()
    else:
        with open(dictfile,'wb') as output:
            pickle.dump(dic,output)
        output.close()

def loadict(dictfile):
    output = open(dictfile, 'rb')
    hashdict = pickle.load(output)
    return hashdict
    #結束

def do():
    count=0;
    for count in range (100):
        time.sleep(0.1);clickClient(getbrow,(204,310))          ##点击A
        time.sleep(0.1);clickClient(getbrow,(270,425))          ##提交答案
        time.sleep(0.1);clickClient(getbrow,(340,565))          ##下一题
    time.sleep(0.1);clickClient(getbrow,(185,605))          ##返回第 1题

#開始收集
def Pickit():
    def picmath(box,filepath):
        savepic = fullsc.crop(box).save(filepath,'JPEG')
        pic = open(filepath,'rb')
        md5 = hashlib.md5(pic.read()).hexdigest().upper()
        pic.close()
        return md5

    do()
    count=0;
    for count in range (100):
        time.sleep(1)         #减速 这里数值可以增大
        fullsc = ImageGrab.grab()

        Qmd5 = picmath(Qbox,'tmp/Qbox.jpg')
            #为解决相同题目產生錯誤的问题，加入QBox2，再生成MD5
        Q2md5 = picmath(Q2box,'tmp/Qbox2.jpg')
            #截图，保存，提交答案之後查看正確答案
        Tipsmd5 = picmath(Tipsbox,'tmp/Tips.JPG')

        if Tipsmd5 == Amd5:
            DictS[Qmd5] = picmath(Abox,'tmp/A.jpg')
            DictP[Q2md5] = picmath(Abox,'tmp/A.jpg')

        elif Tipsmd5 == Bmd5:
            DictS[Qmd5] = picmath(Bbox,'tmp/B.jpg')
            DictP[Q2md5] = picmath(Bbox,'tmp/B.jpg')

        elif Tipsmd5 == Cmd5:
            DictS[Qmd5] = picmath(Cbox,'tmp/C.jpg')
            DictP[Q2md5] = picmath(Cbox,'tmp/C.jpg')

        elif Tipsmd5 == Dmd5:
            DictS[Qmd5] = picmath(Dbox,'tmp/D.jpg')
            DictP[Q2md5] = picmath(Dbox,'tmp/D.jpg')
        else:
            print "no answer! no tips! cant catch!"
        time.sleep(0.1);clickClient(getbrow,(340,565))          ##下一题

    if '674D6AEA2013C3019B9B6B02E32D647B' in DictP:            #判断、删除空白图片的KEY
        del DictP['674D6AEA2013C3019B9B6B02E32D647B']
    wdict('DictS.kmy',DictS)
    wdict('DictP.kmy',DictP)
#結束收集

if __name__ == '__main__':
    Pickit()
