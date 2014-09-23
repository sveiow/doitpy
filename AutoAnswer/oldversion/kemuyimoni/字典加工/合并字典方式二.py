#coding=utf-8
#介紹：合併字典方式二
import pickle
import os
hashdataS = {}
hashdataP = {}
def updata(self,hashdic):
    dic = open(self, 'rb')
    newdata = pickle.load(dic)
    hashdic.update(newdata)

def main(dict1,dict2,hashname,new):
    try:
        updata(dict1,hashname)
        print len(hashname)
        updata(dict2,hashname)
        print len(hashname)

        with open(new, 'wb') as output:
            pickle.dump(hashname, output)
        output.close()
    except IOError:
        pass

os.rename('DictS.K','DictS.kmy')
os.rename('DictP.K','DictP.kmy')
main('DictS.kmy','oneDictS.kmy',hashdataS,'DictS.K')
main('DictP.kmy','oneDictP.kmy',hashdataP,'DictP.K')
