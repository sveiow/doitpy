#coding:gbk
import win32gui
import win32con

getbrow = win32gui.FindWindow("Chrome_WidgetWin_1","�������-������ - Google Chrome")
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##���ڻָ�
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##�������
win32gui.SetForegroundWindow(getbrow) 
