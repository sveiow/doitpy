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
if os.path.exists('lxc') == False: os.mkdir('lxc')
if os.path.exists('Dict') == False: os.mkdir('Dict')

try:
    DictS = loadict(os.path.join('Dict','DictS'))
    DictP = loadict(os.path.join('Dict','DictP'))
except IOError:
    win32api.MessageBox(0, str("û�ҵ��ֵ䣬��ʽ�˳���"), "����", win32con.MB_ICONINFORMATION)
    exit()

HashS = {}
HashP = {}

def PicHash(box,filepath):
    savepic = fullsc.crop(box).save((os.path.join('lxc',filepath)),'JPEG')
    pic = open((os.path.join('lxc',filepath)),'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5

def Answer():
    global fullsc
    time.sleep(0.3)
    fullsc = ImageGrab.grab()

    Qmd5 = PicHash(LXC.Qbox,'Qbox.jpg')
    #�������д𰸵�md5
    Amd5 = PicHash(LXC.Abox,'A.jpg')
    Bmd5 = PicHash(LXC.Bbox,'B.jpg')
    Cmd5 = PicHash(LXC.Cbox,'C.jpg')
    Dmd5 = PicHash(LXC.Dbox,'D.jpg')

    if Qmd5 in DictS:           #check DictS ��Ŀ�Ƿ����
        gas1 = DictS.get(Qmd5)
        if Amd5 == gas1:
            clickClient(getbrow,LXC.Axy)          #A
            clickClient(getbrow,LXC.Submit)          #post
        elif Bmd5 == gas1:
            clickClient(getbrow,LXC.Bxy)          #B
            clickClient(getbrow,LXC.Submit)          #post
        elif Cmd5 == gas1:
            clickClient(getbrow,LXC.Cxy)          #C
            clickClient(getbrow,LXC.Submit)          #post
        elif Dmd5 == gas1:
            clickClient(getbrow,LXC.Dxy)          #D
            clickClient(getbrow,LXC.Submit)          #post
        else:
            logging.info('no answer in DictS,check DictP')
            time.sleep(0.5)
            Q2md5 = PicHash(LXC.Q2box,'Qbox2.jpg')

            if Q2md5 in DictP:           #check DictP ��Ŀ�Ƿ����
                gas2 = DictP.get(Q2md5)
                if Amd5 == gas2:
                    clickClient(getbrow,LXC.Axy)          #A
                    clickClient(getbrow,LXC.Submit)          #post
                elif Bmd5 == gas2:
                    clickClient(getbrow,LXC.Bxy)          #B
                    clickClient(getbrow,LXC.Submit)          #post
                elif Cmd5 == gas2:
                    clickClient(getbrow,LXC.Cxy)          #C
                    clickClient(getbrow,LXC.Submit)          #post
                elif Dmd5 == gas2:
                    clickClient(getbrow,LXC.Dxy)          #D
                    clickClient(getbrow,LXC.Submit)          #post
            else:
                logging.info('no answer in all dicts')
    else:
        time.sleep(0.5)
        Q2md5 = PicHash(LXC.Q2box,'Qbox2.jpg')

        if Q2md5 in DictP:           #check DictP ��Ŀ�Ƿ����
            gas2 = DictP.get(Q2md5)
            if Amd5 == gas2:
                clickClient(getbrow,LXC.Axy)          #A
                clickClient(getbrow,LXC.Submit)          #post
            elif Bmd5 == gas2:
                clickClient(getbrow,LXC.Bxy)          #B
                clickClient(getbrow,LXC.Submit)          #post
            elif Cmd5 == gas2:
                clickClient(getbrow,LXC.Cxy)          #C
                clickClient(getbrow,LXC.Submit)          #post
            elif Dmd5 == gas2:
                clickClient(getbrow,LXC.Dxy)          #D
                clickClient(getbrow,LXC.Submit)          #post
        else:
            logging.info('no answer in DictP,no answer in all dicts')

    Pmd5 = PicHash(LXC.Pcbox,'Process.jpg')
    if Pmd5 == LXC.Pcmd5 or Pmd5 == LXC.Pwebdelay:
        pass
    else:
        clickClient(getbrow,LXC.Next)
        Answer()

def Pick():
    time.sleep(0.5)         #���� ������ֵ��������
    clickClient(getbrow,LXC.Axy)          ##���A
    clickClient(getbrow,LXC.Submit)          ##�ύ��
    time.sleep(1.5)         #���ٵȴ�

    global fullsc
    fullsc = ImageGrab.grab()
    Qmd5 = PicHash(LXC.Qbox,'tmpQbox.jpg')
    Q2md5 = PicHash(LXC.Q2box,'tmpQbox2.jpg')
    Tipsmd5 = PicHash(LXC.Tipsbox,'tmpTips.JPG')

    if Tipsmd5 == LXC.Amd5:
        HashS[Qmd5] = PicHash(LXC.Abox,'tmpA.jpg')
        HashP[Q2md5] = PicHash(LXC.Abox,'tmpA.jpg')

    elif Tipsmd5 == LXC.Bmd5:
        HashS[Qmd5] = PicHash(LXC.Bbox,'tmpB.jpg')
        HashP[Q2md5] = PicHash(LXC.Bbox,'tmpB.jpg')

    elif Tipsmd5 == LXC.Cmd5:
        HashS[Qmd5] = PicHash(LXC.Cbox,'tmpC.jpg')
        HashP[Q2md5] = PicHash(LXC.Cbox,'tmpC.jpg')

    elif Tipsmd5 == LXC.Dmd5:
        HashS[Qmd5] = PicHash(LXC.Dbox,'tmpD.jpg')
        HashP[Q2md5] = PicHash(LXC.Dbox,'tmpD.jpg')
    else:
        print 'no answer! no tips! cant catch!'

def Nextstep():
    clickClient(getbrow,LXC.Handin)
    time.sleep(1)
    clickClient(getbrow,LXC.BT1)          #δ�����ʾ��Ĵ_�J
    time.sleep(2)

    global fullsc
    fullsc = ImageGrab.grab()
    Buttunmd5 = PicHash(LXC.Button,'Button.JPG')
    if Buttunmd5 == LXC.ButtunT:
        clickClient(getbrow,LXC.BT2)          #�c��������һ��֪�R�c
        time.sleep(2)
        SemiautoPick()
    elif Buttunmd5 == LXC.ButtunF:
        clickClient(getbrow,LXC.BT2)          #�c��ʧ������
        Answer()
        Nextstep()
    else:
        print "all this chapter finish!"
        exit()

#===============================================================================
def AutoAnswer():
    Answer()
    #�M����һ��
    clickClient(getbrow,LXC.Handin)
    time.sleep(1)
    clickClient(getbrow,LXC.BT1)          #δ�����ʾ��Ĵ_�J
    time.sleep(2)

    global fullsc
    fullsc = ImageGrab.grab()
    Buttunmd5 = PicHash(LXC.Button,'Button.JPG')
    if Buttunmd5 == LXC.Bwebdelay or Buttunmd5 == LXC.ButtunT:  #==LXC.ButtunTΪ��̰��ģʽ��!=ButtunBlankʱΪ̰��ģʽ
        clickClient(getbrow,LXC.BT2)          #������һ��֪�R�c
        AutoAnswer()
    else:
        logging.info('all this chapter finish!')
        exit()

def Pickit():
    Pick()
    Pmd5 = PicHash(LXC.Pcbox,'Process.jpg')
    if Pmd5 != LXC.Pcmd5:
        clickClient(getbrow,LXC.Next)
        Pickit()            #����ѭ��
    else:
        if LXC.BoxBlank in HashP:            #�жϡ�ɾ���հ�ͼƬ��KEY
            del HashP[LXC.BoxBlank]
        wdict('DictS.part',HashS)
        wdict('DictP.part',HashP)
        print 'finish'

def OnePickit():
    Pick()
    if LXC.BoxBlank in HashP:            #�жϡ�ɾ���հ�ͼƬ��KEY
        del HashP[LXC.BoxBlank]
    wdict('oneDictS.part',HashS)
    wdict('oneDictP.part',HashP)
    print 'finish'

def SemiautoPick():
    Pickit()
    Nextstep()

getbrow = win32gui.FindWindow('Chrome_WidgetWin_1','�������-������ - Google Chrome')

choice = """====== ��������ϰ����ʽ =====
����(1)�������Զ�����
����(2)�����뵥���ռ�
����(3)�����������ռ�
����(P)�����������ռ�
����(Q)���뿪

Enter choice:"""

choice = raw_input(choice).strip()[0].lower()
if choice == 'q' or choice not in ['1','2','3','p']:
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
    'p':SemiautoPick,
    }
cho.get(choice)()
