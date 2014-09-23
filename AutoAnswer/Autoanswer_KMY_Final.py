#coding=gbk
#Introduction:20140917
from PIL import Image,ImageGrab
import win32gui
import win32con
import win32api
import logging
import os
import time
import hashlib
import pickle
from AAmodules import *

#�z�鹤��Ŀ�
if os.path.exists('kmy') == False: os.mkdir('kmy')
if os.path.exists('Dict') == False: os.mkdir('Dict')

try:
    DictS = loadict(os.path.join('Dict','DictS.K'))
    DictP = loadict(os.path.join('Dict','DictP.K'))
except IOError:
    win32api.MessageBox(0, str("û�ҵ��ֵ䣬��ʽ�˳���"), "����", win32con.MB_ICONINFORMATION)
    exit()

HashS = {}
HashP = {}

def PicHash(box,filepath):
    savepic = fullsc.crop(box).save(os.path.join('kmy',filepath),'JPEG')
    pic = open(os.path.join('kmy',filepath),'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5

def Answer():
    time.sleep(0.2)
    global fullsc
    fullsc = ImageGrab.grab()

    Qmd5 = PicHash(KMY.Qbox,'Qbox.jpg')
    #�������д𰸵�md5
    Amd5 = PicHash(KMY.Abox,'A.jpg')
    Bmd5 = PicHash(KMY.Bbox,'B.jpg')
    Cmd5 = PicHash(KMY.Cbox,'C.jpg')
    Dmd5 = PicHash(KMY.Dbox,'D.jpg')

    if Qmd5 in DictS:
        Gans1 = DictS.get(Qmd5)
        if Amd5 == Gans1:
            clickClient(getbrow,KMY.Axy)
            clickClient(getbrow,KMY.Submit)
        elif Bmd5 == Gans1:
            clickClient(getbrow,KMY.Bxy)
            clickClient(getbrow,KMY.Submit)
        elif Cmd5 == Gans1:
            clickClient(getbrow,KMY.Cxy)
            clickClient(getbrow,KMY.Submit)
        elif Dmd5 == Gans1:
            clickClient(getbrow,KMY.Dxy)
            clickClient(getbrow,KMY.Submit)
        else:
            time.sleep(0.5)
            Q2md5 = PicHash(KMY.Q2box,'Q2box.jpg')
            if Q2md5 in DictP:
                Gans2 = DictP.get(Q2md5)
                if Amd5 == Gans2:
                    clickClient(getbrow,KMY.Axy)
                    clickClient(getbrow,KMY.Submit)
                elif Bmd5 == Gans2:
                    clickClient(getbrow,KMY.Bxy)
                    clickClient(getbrow,KMY.Submit)
                elif Cmd5 == Gans2:
                    clickClient(getbrow,KMY.Cxy)
                    clickClient(getbrow,KMY.Submit)
                elif Dmd5 == Gans2:
                    clickClient(getbrow,KMY.Dxy)
                    clickClient(getbrow,KMY.Submit)
    else:
        time.sleep(0.5)
        Q2md5 = PicHash(KMY.Q2box,'Q2box.jpg')
        if Q2md5 in DictP:
            Gans2 = DictP.get(Q2md5)
            if Amd5 == Gans2:
                clickClient(getbrow,KMY.Axy)
                clickClient(getbrow,KMY.Submit)
            elif Bmd5 == Gans2:
                clickClient(getbrow,KMY.Bxy)
                clickClient(getbrow,KMY.Submit)
            elif Cmd5 == Gans2:
                clickClient(getbrow,KMY.Cxy)
                clickClient(getbrow,KMY.Submit)
            elif Dmd5 == Gans2:
                clickClient(getbrow,KMY.Dxy)
                clickClient(getbrow,KMY.Submit)

def Pick():
    time.sleep(1)
    global fullsc
    fullsc = ImageGrab.grab()

    Qmd5 = PicHash(KMY.Qbox,'tmpQbox.jpg')
    Q2md5 = PicHash(KMY.Q2box,'tmpQbox2.jpg')
    Tipsmd5 = PicHash(KMY.Tipsbox,'tmpTips.JPG')

    if Tipsmd5 == KMY.Amd5:
        HashS[Qmd5] = PicHash(KMY.Abox,'tmpA.jpg')
        HashP[Q2md5] = PicHash(KMY.Abox,'tmpA.jpg')

    elif Tipsmd5 == KMY.Bmd5:
        HashS[Qmd5] = PicHash(KMY.Bbox,'tmpB.jpg')
        HashP[Q2md5] = PicHash(KMY.Bbox,'tmpB.jpg')

    elif Tipsmd5 == KMY.Cmd5:
        HashS[Qmd5] = PicHash(KMY.Cbox,'tmpC.jpg')
        HashP[Q2md5] = PicHash(KMY.Cbox,'tmpC.jpg')

    elif Tipsmd5 == KMY.Dmd5:
        HashS[Qmd5] = PicHash(KMY.Dbox,'tmpD.jpg')
        HashP[Q2md5] = PicHash(KMY.Dbox,'tmpD.jpg')
    else:
        print "cant catch!"

#===============================================================================
def Do():
    for count in range (100):
        time.sleep(0.2)
        clickClient(getbrow,KMY.Axy)          ##���A
        clickClient(getbrow,KMY.Submit)          ##�ύ��
        clickClient(getbrow,KMY.Next)          ##��һ��
    time.sleep(0.2)
    clickClient(getbrow,(185,605))          ##���ص� 1��

def AutoAnswer():
    for count in range(100):
        Answer()
        clickClient(getbrow,KMY.Next)

def Pickit(x):
    x = raw_input('')
    for count in range(x):
        Do()
        for Qcount in range (100):
            Pick()
            clickClient(getbrow,KMY.Next)

        if KMY.BoxBlank in HashP:            #�жϡ�ɾ���հ�ͼƬ��KEY
            del HashP[KMY.BoxBlank]
        wdict('DictS.KM',HashS)
        wdict('DictP.KM',HashP)

        clickClient(getbrow,KMY.HnA)
        clickClient(getbrow,KMY.BT1)
        clickClient(getbrow,KMY.Confirm)
        clickClient(getbrow,KMY.HnA)

        print len(HashS);HashS.clear()
        print len(HashP);HashP.clear()

def OnePickit():
    clickClient(getbrow,KMY.Axy)          ##���A
    clickClient(getbrow,KMY.Submit)          ##�ύ��
    Pick()
    if KMY.BoxBlank in HashP:            #�жϡ�ɾ���հ�ͼƬ��KEY
        del HashP[KMY.BoxBlank]
    wdict('oneDictS.KMY',HashS)
    wdict('oneDictP.KMY',HashP)

getbrow = win32gui.FindWindow('Chrome_WidgetWin_1','ģ�⿼��flash�� - Google Chrome')

choice = """===== ��Ŀһģ�⿼�Գ�ʽ =====
����(1)�������Զ�����
����(2)�����뵥���ռ�
����(3)�����������ռ�
����(Q)���뿪

Enter choice:"""

choice = raw_input(choice).strip()[0].lower()
if choice == 'q' or choice not in ['1','2','3']:
    exit()
else:
    win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##ǿ����ʾ����
    win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##�������
    win32gui.SetForegroundWindow(getbrow)           ##������������ᵽǰ̨
    time.sleep(0.8)         #�ȴ�������ȫ����

cho = {
    '1':AutoAnswer,
    '2':OnePickit,
    '3':Pickit,
    }
cho.get(choice)()
