#coding=utf-8
import pickle

def loadict(dictfile):
    output = open(dictfile, 'rb')
    data = pickle.load(output)
     print data
    print len(data)
    output.close()

loadict('DictS.KM')
loadict('DictP.KM')
