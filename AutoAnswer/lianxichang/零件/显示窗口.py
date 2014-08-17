#coding:gbk
import win32gui
import win32con

getbrow = win32gui.FindWindow("Chrome_WidgetWin_1","立秋·驾培-闯关王 - Google Chrome")
win32gui.ShowWindow(getbrow,win32con.SW_RESTORE)            ##窗口恢复
win32gui.ShowWindow(getbrow,win32con.SW_MAXIMIZE)           ##窗口最大化
win32gui.SetForegroundWindow(getbrow) 
