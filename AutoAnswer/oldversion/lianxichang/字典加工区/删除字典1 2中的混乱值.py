#coding=utf-8
#介紹：删除special文件夹下的图片在字典1中的MD5值，使其向字典2查询
import pickle
import os
import hashlib

def loadict(filename):
    output = open(filename, 'rb')
    data = pickle.load(output)
    output.close()
    return data

def delkey(x):
    if x in hashdata:
        print "ready del"
        del hashdata[x]

def mathmd5(filepath):
    pic = open(filepath,'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    pic.close()
    return md5

hashdata = loadict('dict1.pkl.part2')      #定义字典1
print len(hashdata)

dirpath = os.getcwd() + '\\special'
for files in os.listdir(dirpath):
    fp = dirpath+'\\'+files
    delkey(mathmd5(fp))
    
print len(hashdata)
with open('hashdata_v.pkl', 'wb') as output:
    pickle.dump(hashdata, output)
output.close()

#删除字典2的空白值
dict2 = loadict('hashdata_v1.pkl')      #定义字典2
print len(dict2)
delkey('782D92C2D53C89E7E10955A6F0349567')       #定义空白值
print len(dict2)

with open('hashdata_dict2.pkl', 'wb') as output2:
    pickle.dump(dict2, output2)
output.close()
