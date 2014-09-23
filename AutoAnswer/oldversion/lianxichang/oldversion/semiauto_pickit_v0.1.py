#coding=utf-8
#version:semiauto_pickit_v0.1
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
button = (410,705,575,740)

Amd5 = '2B964BCA9F554C660C5418561AFFF177'
Bmd5 = 'B34D3B3B460019BA8625BAE5EEFE91B1'
Cmd5 = 'BA8A8CF9E8669E09EDB63832B60338D7'
Dmd5 = 'D0C5378938E2CC34C6CB30867FD5C6BB'
Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'
buttonT = 'BB54913D762C90152D4071BA66795C6A'
buttonF = '0608E1F2485E0706D1DD7272A43F5A3F'

def click(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)

        #檢測字典是否已經存在
def wdict():
    #dict1
    if os.path.isfile('hashdata_v1.pkl'):
        oldict = open('hashdata_v1.pkl', 'rb')
        oldata = pickle.load(oldict)
        hashdict.update(oldata)
        output = open('hashdata_v1.pkl', 'wb')         #全部题目记录好了，然后就写入文件
        pickle.dump(hashdict,output)          ##寫入HASH至文件
        output.close()
    else:
        with open('hashdata_v1.pkl', 'wb') as output:         #全部题目记录好了，然后就写入文件
            pickle.dump(hashdict,output)          ##寫入HASH至文件
        output.close()

        #dict2
    if os.path.isfile('hashdata_v2.pkl'):
        oldict2box = open('hashdata_v2.pkl', 'rb')
        oldata2box = pickle.load(oldict2box)
        hashdict_v2.update(oldata2box)
        output2box = open('hashdata_v2.pkl', 'wb')         #全部题目记录好了，然后就写入文件
        pickle.dump(hashdict_v2,output2box)          ##寫入HASH至文件
        output2box.close()
    else:
        with open('hashdata_v2.pkl', 'wb') as output2box:         #全部题目记录好了，然后就写入文件
            pickle.dump(hashdict_v2,output2box)          ##寫入HASH至文件
        output2box.close()

def nextclass():
    click(1020,865)          #交卷
    time.sleep(0.3)
    click(560,680)          #未完成提示框的確認

    time.sleep(0.5)
    fullsc = ImageGrab.grab()
    savebutton = fullsc.crop(button).save('tmp/button.JPG','JPEG')         #截图，保存，提交答案之後查看正確答案
    button = open('tmp/button.JPG','rb')
    buttonmd5 = hashlib.md5(button.read()).hexdigest().upper()
    button.close()

    if buttonmd5 == buttonT:
        click(490,720)          #練習下一個知識點
        pickit()
    elif buttonmd5 == buttonF:
        click(490,720)          #失敗重做
        AutoAnswer()
    else:
        print 'this chapter all finish!'
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
    wQmd5 =  '%s' % Qmd5

        #为解决相同题目產生錯誤的问题，加入QBox2，再生成MD5
    saveQ2 = fullsc.crop(Q2box).save('tmp/Qbox2.jpg','JPEG')
    picQ2 = open('tmp/Qbox2.jpg','rb')
    Q2md5 = hashlib.md5(picQ.read()).hexdigest().upper()
    AllQmd5 = '%s%s' %(Qmd5,Q2md5)
    AllQmd5 = hashlib.md5(AllQmd5).hexdigest().upper()
    wAllQmd5 =  '%s' % AllQmd5
    picQ.close(),picQ2.close()

    saveTips = fullsc.crop(Tipsbox).save('tmp/Tips.JPG','JPEG')         #截图，保存，提交答案之後查看正確答案
    Tips = open('tmp/Tips.JPG','rb')
    Tipsmd5 = hashlib.md5(Tips.read()).hexdigest().upper()
    Tips.close()

        #计算答案MD5
    def md5w():
        md5 = hashlib.md5(pic.read()).hexdigest().upper()
        md5 = '%s' % md5
        hashdict[wQmd5] = md5           #單單題目區
        hashdict_v2[wAllQmd5] = md5            #圖片區+題目區
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

    getProcessPit()
#結束收集

#開始做題
def AutoAnswer():
    #导入字典
        ##dict1
    output = open('hashdata_v1.pkl', 'rb')
    hashdict = pickle.load(output)			#此时hashdata已经是字典类型
        ##dict2
    output2box = open('hashdata_v2.pkl', 'rb')
    hashdict_v2 = pickle.load(output2box)			#此时hashdata已经是字典类型

    time.sleep(0.5)         #截图前，降速等待圖片的显示，至少0.2秒
    fullsc = ImageGrab.grab()               ##截全圖，因爲是pick工作，所以提交答案再截圖

    saveQ = fullsc.crop(Qbox).save('tmp/tmpQbox.jpg','JPEG')
    picQ = open('tmp/tmpQbox.jpg','rb')
    Qmd5 = hashlib.md5(picQ.read()).hexdigest().upper()
    picQ.close()
    wQmd5 =  '%s' %Qmd5
    getanswer1 = hashdict.get(wQmd5)            ##第一次查询题目对应的答案

    #计算所有答案的md5
    saveA = fullsc.crop(Abox).save('tmp/tmpA.jpg','JPEG')
    saveB = fullsc.crop(Bbox).save('tmp/tmpB.jpg','JPEG')
    saveC = fullsc.crop(Cbox).save('tmp/tmpC.jpg','JPEG')
    saveD = fullsc.crop(Dbox).save('tmp/tmpD.jpg','JPEG')
    picA = open('tmp/tmpA.jpg','rb')
    Amd5 = hashlib.md5(picA.read()).hexdigest().upper()
    picB = open('tmp/tmpB.jpg','rb')
    Bmd5 = hashlib.md5(picB.read()).hexdigest().upper()
    picC = open('tmp/tmpC.jpg','rb')
    Cmd5 = hashlib.md5(picC.read()).hexdigest().upper()
    picD = open('tmp/tmpD.jpg','rb')
    Dmd5 = hashlib.md5(picD.read()).hexdigest().upper()
    picA.close(),picB.close(),picC.close(),picD.close()

    if wQmd5 in hashdict:           #check dict1 题目是否存在
        if getanswer1 == Amd5:
            click(465,580)          #A
            click(505,715)          #post
        elif getanswer1 == Bmd5:
            click(465,605)          #B
            click(505,715)          #post
        elif getanswer1 == Cmd5:
            click(465,630)          #C
            click(505,715)          #post
        elif getanswer1 == Dmd5:
            click(465,655)          #D
            click(505,715)          #post
        else:
                #为解决相同题目问题，加入QBox2，再生成MD5
            saveQ2 = fullsc.crop(Q2box).save('tmp/tmpQbox2.jpg','JPEG')
            picQ2 = open('tmp/tmpQbox2.jpg','rb')
            Q2md5 = hashlib.md5(picQ2.read()).hexdigest().upper()
            picQ2.close()
            AllQmd5 = '%s%s' %(Qmd5,Q2md5)
            AllQmd5 = hashlib.md5(AllQmd5).hexdigest().upper()
            wAllQmd5 =  '%s' %AllQmd5
            getanswer2 = hashdict_v2.get(wAllQmd5)          #第二次查询题目对应的答案

            if wAllQmd5 in hashdict_v2:           #check dict2 题目是否存在
                if getanswer2 == Amd5:
                    click(465,580)          #A
                    click(505,715)          #post
                elif getanswer2 == Bmd5:
                    click(465,605)          #B
                    click(505,715)          #post
                elif getanswer2 == Cmd5:
                    click(465,630)          #C
                    click(505,715)          #post
                elif getanswer2 == Dmd5:
                    click(465,655)          #D
                    click(505,715)          #post
                else:
                    print 'no answer!!'
            else:
                print 'no answer! no this question in hashdict!!'
    else:
        print 'no this question in hashdict!'

    getProcessAns()
#結束做題

    #判斷當前進度
def getProcessPit():
    fullsc = ImageGrab.grab()
    saveProcess = fullsc.crop(Pcbox).save('tmp/Process.jpg','JPEG')         #截图，保存
    picPc = open('tmp/Process.jpg','rb')
    Pmd5 = hashlib.md5(picPc.read()).hexdigest().upper()
    picPc.close()

    if Pmd5 != Pcmd5 :
        click(655,770)          #点击下一题
        pickit()            #查题循环
    else:
        wdict()
        print 'pickit finish'
        nextclass()

def getProcessAns():
    Pcmd5 = '54F84561323AE11EE1AA1C28290D7A17'
    fullsc = ImageGrab.grab()
    saveProcess = fullsc.crop(Pcbox).save('tmp/tmpProcess.jpg','JPEG')         #截图，保存
    picPc = open('tmp/tmpProcess.jpg','rb')
    Pmd5 = hashlib.md5(picPc.read()).hexdigest().upper()
    picPc.close()

    if Pmd5 != Pcmd5 :
        click(655,770)          #点击下一题
        AutoAnswer()            #查题循环
    else:
        print 'AutoAnswer finish'
        nextchapter()

if __name__ == '__main__':
    pickit()
