#coding=utf-8
import os
import hashlib

pic1 = open('TipsA.JPG','rb')
pic2 = open('TipsB.JPG','rb')

pic1md5 = hashlib.md5(pic1.read()).hexdigest().upper()
pic2md5 = hashlib.md5(pic2.read()).hexdigest().upper()

print 'pic1md5 is: %s'%pic1md5
print 'pic2md5 is: %s'%pic2md5

AllQmd5 = '%s%s' %(pic1md5,pic2md5)
AllQmd5 = hashlib.md5(AllQmd5).hexdigest().upper()
print 'md5 is: %s'%AllQmd5

compare = hashlib.md5('2B964BCA9F554C660C5418561AFFF177B34D3B3B460019BA8625BAE5EEFE91B1').hexdigest().upper()
print 'compare is: %s'%compare
