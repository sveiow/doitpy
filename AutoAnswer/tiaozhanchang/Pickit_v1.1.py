#coding=utf-8
#Introduction:題目收集-----for:闯关王——挑战场,測試可用,20140906
#version:Pickit_v1.1，for:闯关王——挑战场
#updata v1.0:修改鼠標模擬的方式，解決鼠標失控問題（側面解決死循環）
#updata 0.1:基于Pickit_a3.1改写
from PIL import Image,ImageGrab
import os,time
import hashlib,pickle
import win32gui,win32con,win32api

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
hashDictS = {}
hashDictP = {}

Qbox = (515,470,1020,488)
Q2box = (860,500,1050,655)
Abox = (510,564,840,586)
Bbox = (510,590,840,612)
Cbox = (510,617,840,639)
Dbox = (510,644,840,666)
Pcbox = (927,707,1059,744)
Tipsbox = (680,725,690,740)

Amd5 = '12BCBD3468A716E7FF9E62DD1BC8DEE5'
Bmd5 = '288E9FD1D078EC956B914D1BA045D647'
Cmd5 = '913C49EF5AC4435D729AFC9D49EA77F6'
Dmd5 = '12F6FA8780D2DC48F65B9774915779D3'
Pcmd5 = '38E53A7D5DD9FC87B8C74B6CD911C22D'

def clickClient(handle,pos):
    coordinate = win32api.MAKELONG(pos[0], pos[1])
    win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
    win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, coordinate)
    win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, coordinate)
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

def picmath(box,filepath):
    savepic = fullsc.crop(box).save(filepath,'JPEG')
    pic = open(filepath,'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5
    #結束

    #開始收集
def Pickit():
    time.sleep(1)         #减速 这里数值可以增大
    clickClient(getbrow,(465,580))          ##点击A
    clickClient(getbrow,(505,715))          ##提交答案
    time.sleep(1.5)         #减速等待
    global fullsc
    fullsc = ImageGrab.grab()

    Qmd5 = picmath(Qbox,'tmp/Qbox.jpg')
        #为解决相同题目產生錯誤的问题，加入QBox2，再生成MD5
    Q2md5 = picmath(Q2box,'tmp/Qbox2.jpg')
    AllQmd5 = hashlib.md5('%s%s' %(Qmd5,Q2md5)).hexdigest().upper()
        #截图，保存，提交答案之後查看正確答案
    Tipsmd5 = picmath(Tipsbox,'tmp/Tips.JPG')

    if Tipsmd5 == Amd5:
        hashDictS[Qmd5] = picmath(Abox,'tmp/A.jpg')
        hashDictP[AllQmd5] = picmath(Abox,'tmp/A.jpg')

    elif Tipsmd5 == Bmd5:
        hashDictS[Qmd5] = picmath(Bbox,'tmp/B.jpg')
        hashDictP[AllQmd5] = picmath(Bbox,'tmp/B.jpg')

    elif Tipsmd5 == Cmd5:
        hashDictS[Qmd5] = picmath(Cbox,'tmp/C.jpg')
        hashDictP[AllQmd5] = picmath(Cbox,'tmp/C.jpg')

    elif Tipsmd5 == Dmd5:
        hashDictS[Qmd5] = picmath(Dbox,'tmp/D.jpg')
        hashDictP[AllQmd5] = picmath(Dbox,'tmp/D.jpg')
    else:
        print 'no answer! no tips! cant catch!'

    #判斷當前進度
    Pmd5 = picmath(Pcbox,'tmp/Process.jpg')

    if Pmd5 != Pcmd5 :
        clickClient(getbrow,(990,725))          #点击下一题
        Pickit()            #查题循环
    else:
        wdict('hashDictS.tzc',hashDictS)
        wdict('hashDictP.tzc',hashDictP)
        print 'finish'

if __name__ == '__main__':
    Pickit()
