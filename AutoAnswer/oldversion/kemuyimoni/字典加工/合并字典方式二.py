#coding=utf-8
#介紹：合併字典方式二
import pickle
import os
hashdataS = {}
hashdataP = {}
def updata(self,hashdic):
    dic = open(self, 'rb')
    newdata = cPickle.load(dic)
    hashdic.update(newdata)

def main(dict1,dict2,hashname,new):
    try:
        updata(dict1,hashname)      #载入
        print 'befor: %s' % len(hashname)
        updata(dict2,hashname)      #覆盖
        print len(hashname)

        with open(new, 'wb') as output:
            cPickle.dump(hashname, output)
        output.close()
    except IOError:
        pass

os.rename('DictS.K','DictS.old')
os.rename('DictP.K','DictP.old')
main('DictS.old','oneDictS.kmy',hashdataS,'DictS.K')
main('DictP.old','oneDictP.kmy',hashdataP,'DictP.K')
