#coding=utf-8

from PIL import Image

fullsc = ImageGrab.grab()
box = (515, 470, 1020, 488)
questions = fullsc.crop(box)
questions.show()
