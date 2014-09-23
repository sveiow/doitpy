#coding=utf-8
#合併字典
import pickle
import re
import os

rule = re.compile(r'^(.*)\.(pkl)$')
def loadict(dictfile):
    output = open(dictfile, 'rb')
    data = pickle.load(output)
    output.close()
    return data
    
hashdict = {}

for fp in os.listdir(os.getcwd()):
    if rule.match(fp):
        hashdict.update(loadict(fp))
        
print len(hashdict)
print type(hashdict)

with open('hashdata_v.pkl', 'wb') as output:
    pickle.dump(hashdict, output)

