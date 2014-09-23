#coding=utf-8
#介紹：合併字典方式二
import pickle
hashdata = {}
def updata(filename):
    output = open(filename, 'rb')
    data = pickle.load(output)
    hashdata.update(data)
    
updata('hashdict-part1.pkl')
updata('hashdict-part2.pkl')
updata('hashdict-part3.pkl')

print hashdata
print len(hashdata)

with open('hashdata.pkl', 'wb') as output:
    pickle.dump(hashdata, output)
output.close()
