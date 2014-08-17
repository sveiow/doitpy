#coding:gbk
import win32con
import win32api

##点击A
Ax = 465
Ay = 580
win32api.SetCursorPos([Ax,Ay])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,Ax,Ay)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,Ax,Ay)

##点击B
Bx = 465
By = 605
win32api.SetCursorPos([Bx,By])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,Bx,By)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,Bx,By)

##点击C
Cx = 465
Cy = 630
win32api.SetCursorPos([Cx,by])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,Cx,Cy)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,Cx,Cy)

##点击D
Dx = 465
Dy = 655
win32api.SetCursorPos([Dx,Dy])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,Dx,Dy)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,Dx,Dy)

##提交答案
put_x = 505
put_y = 715
win32api.SetCursorPos([put_x,put_y])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,put_x,put_y)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,put_x,put_y)

##下一题
next_x = 655
next_y = 770
win32api.SetCursorPos([next_x,next_y])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,next_x,next_y)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,next_x,next_y)

##交卷
post_x = 1020
post_y = 865
win32api.SetCursorPos([post_x,post_y])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,post_x,post_y)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,post_x,post_y)
