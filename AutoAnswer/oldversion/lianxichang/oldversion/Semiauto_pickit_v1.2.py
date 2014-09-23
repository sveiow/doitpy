#coding=utf-8
#Introduction:一章一章收集 ----- for:闯关王——练兵场,正式可用,20140905
#version:Semiauto_pickit_v1.2
#updata v1.2:模块化修改
#updata v1.1:根据Pickit_a4.0和Autoanswer_a2.0，作出修改
#updata v1.0:修改鼠標模擬的方式，解決鼠標失控問題（側面解決死循環）
#updata a0.1:基於v0.5的重寫
from PIL import Image,ImageGrab
import win32gui,win32con,win32api
import logging,os,time
import hashlib,pickle
from AAmodules import *

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
DictS = {}
DictP = {}

def picmath(box,filepath):
    savepic = fullsc.crop(box).save(filepath,'JPEG')
    pic = open(filepath,'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5

def nextclass():
    clickClient(getbrow,(1020,865))          #交卷
    time.sleep(1)
    clickClient(getbrow,(560,680))          #未完成提示框的確認
    time.sleep(1.5)
    global fullsc
    fullsc = ImageGrab.grab()
    
    Buttunmd5 = picmath(Button,'tmp/Button.JPG')
    if Buttunmd5 == ButtunT:
        clickClient(getbrow,(490,720))          #練習下一個知識點
        time.sleep(3)
        Pickit()
    elif Buttunmd5 == ButtunF:
        clickClient(getbrow,(490,720))          #失敗重做
        AutoAnswer()
    else:
        print "all this chapter finish!"
        return
    #結束

#開始收集
def Pickit():
    time.sleep(1)         #减速 这里数值可以增大
    clickClient(getbrow,(465,580))          ##点击A
    clickClient(getbrow,(505,715))          ##提交答案
    time.sleep(2.5)         #减速等待
    global fullsc
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

    #判斷當前進度
    Pmd5 = picmath(Pcbox,'tmp/Process.jpg')

    if Pmd5 != Pcmd5 :
        clickClient(getbrow,(655,770))          #点击下一题
        Pickit()            #查题循环
    else:
        if '782D92C2D53C89E7E10955A6F0349567' in DictP:            #判断、删除空白图片的KEY
            del DictP['782D92C2D53C89E7E10955A6F0349567']
        wdict('DictS',DictS)
        wdict('DictP',DictP)
        print "Pickit finish, next chapter!"
        nextclass()
#結束收集

#開始做題
def AutoAnswer():
    hashDictS = loadict('DictS')         #導入字典
    hashDictP = loadict('DictP')

    time.sleep(0.3)         #截图前，降速等待窗口的显示，至少0.2秒
    global fullsc
    fullsc = ImageGrab.grab()

    Qmd5 = picmath(Qbox,'tmp/Qbox.jpg')
    #计算所有答案的md5
    Amd5 = picmath(Abox,'tmp/tmpA.jpg')
    Bmd5 = picmath(Bbox,'tmp/tmpB.jpg')
    Cmd5 = picmath(Cbox,'tmp/tmpC.jpg')
    Dmd5 = picmath(Dbox,'tmp/tmpD.jpg')

    if Qmd5 in hashDictS:           #check DictS 题目是否存在
         ##第一次查询题目对应的答案
        gas1 = hashDictS.get(Qmd5)
        if Amd5 == gas1:
            clickClient(getbrow,(465,580))          #A
            clickClient(getbrow,(505,715))          #post
        elif Bmd5 == gas1:
            clickClient(getbrow,(465,605))          #B
            clickClient(getbrow,(505,715))          #post
        elif Cmd5 == gas1:
            clickClient(getbrow,(465,630))          #C
            clickClient(getbrow,(505,715))          #post
        elif Dmd5 == gas1:
            clickClient(getbrow,(465,655))          #D
            clickClient(getbrow,(505,715))          #post
        else:
            print 'no answer in DictS'
            time.sleep(0.5)
            Q2md5 = picmath(Q2box,'tmp/tmpQbox2.jpg')

            if Q2md5 in hashDictP:           #check DictP 题目是否存在
                gas2 = hashDictP.get(Q2md5)
                if Amd5 == gas2:
                    clickClient(getbrow,(465,580))          #A
                    clickClient(getbrow,(505,715))          #post
                elif Bmd5 == gas2:
                    clickClient(getbrow,(465,605))          #B
                    clickClient(getbrow,(505,715))          #post
                elif Cmd5 == gas2:
                    clickClient(getbrow,(465,630))          #C
                    clickClient(getbrow,(505,715))          #post
                elif Dmd5 == gas2:
                    clickClient(getbrow,(465,655))          #D
                    clickClient(getbrow,(505,715))          #post
                else:
                    print 'no answer in all dict'
    else:
        time.sleep(0.5)
        Q2md5 = picmath(Q2box,'tmp/tmpQbox2.jpg')

        if Q2md5 in hashDictP:           #check DictP 题目是否存在
            gas2 = hashDictP.get(Q2md5)
            if Amd5 == gas2:
                clickClient(getbrow,(465,580))          #A
                clickClient(getbrow,(505,715))          #post
            elif Bmd5 == gas2:
                clickClient(getbrow,(465,605))          #B
                clickClient(getbrow,(505,715))          #post
            elif Cmd5 == gas2:
                clickClient(getbrow,(465,630))          #C
                clickClient(getbrow,(505,715))          #post
            elif Dmd5 == gas2:
                clickClient(getbrow,(465,655))          #D
                clickClient(getbrow,(505,715))          #post
        else:
            print 'no answer in DictP'

    #判斷當前進度
    Pmd5 = picmath(Pcbox,'tmp/Process.jpg')
    if Pmd5 != Pcmd5 :
        clickClient(getbrow,(655,770))          #点击下一题
        AutoAnswer()            #查题循环
    else:
        print "AutoAnswer finish, next chapter!"
        nextclass()
#結束做題

if __name__ == '__main__':
    Pickit()
