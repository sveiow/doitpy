#coding:gbk
import win32gui
import win32con
import win32api

getbrow = win32gui.FindWindow("Chrome_WidgetWin_1","�������-������ - Google Chrome")         ##���崰��
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##ǿ����ʾ����
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##�������
win32gui.SetForegroundWindow(getbrow)           ##������������ᵽ��ǰ

def click(x,y):
    win32api.SetCursorPos([x,y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)
    
#�c����һ�}
click(655,770)
