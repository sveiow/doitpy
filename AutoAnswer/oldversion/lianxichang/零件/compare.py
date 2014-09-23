#coding=utf-8
from PIL import Image

imageQ = Image.open('imageA.JPEG').convert('L')
tmpQ = Image.open('tmpD.JPEG').convert('L')

Pa = imageQ.histogram()
Pb = tmpQ.histogram()

if Pa == Pb:
    print 'same'
else:
    print 'differ'
