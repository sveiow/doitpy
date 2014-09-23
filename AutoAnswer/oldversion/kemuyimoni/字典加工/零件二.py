#coding=utf-8
#介紹：合併字典方式二
import pickle
hashdata = {}
def updata(filename):
    dic = open(filename, 'rb')
    newdata = pickle.load(dic)
    hashdata.update(newdata)
    
updata('DictS.kmy')
print len(hashdata)
updata('oneDictS.kmy')
print len(hashdata)

with open('DictS.pkl', 'wb') as output:
    pickle.dump(hashdata, output)
output.close()
