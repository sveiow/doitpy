#coding:gbk
import win32gui
import win32con

getbrow = win32gui.FindWindow("Chrome_WidgetWin_1","立秋·驾培-闯关王 - Google Chrome")         ##定义窗口
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##强行显示界面
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
win32gui.SetForegroundWindow(getbrow)           ##将浏览器窗口提到最前


from PIL import Image
import ImageGrab

fullsc = ImageGrab.grab()

Qbox = (515,470,1020,488)
Abox = (510,564,840,586)
Bbox = (510,590,840,612)
Cbox = (510,617,840,639)
Dbox = (510,644,840,666)
imageQ = fullsc.crop(Qbox)
imageA = fullsc.crop(Abox)
imageB = fullsc.crop(Bbox)
imageC = fullsc.crop(Cbox)
imageD = fullsc.crop(Dbox)
imageQ.save("imageQ","JPEG")
imageA.save("imageA","JPEG")
imageB.save("imageB","JPEG")
imageC.save("imageC","JPEG")
imageD.save("imageD","JPEG")
