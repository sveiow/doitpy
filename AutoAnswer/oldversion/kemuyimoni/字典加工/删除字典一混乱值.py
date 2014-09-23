#coding=utf-8
#介紹：删除字典一混乱值
import pickle
def loadict(filename):
    output = open(filename, 'rb')
    data = pickle.load(output)
    output.close()
    return data
    
hashdata = loadict('hashdata_v1.pkl')
del hashdata['1E1A55A4583B498D7CF9B1296D0E0D02']
del hashdata['D55E1EFA7F3717352A32DF931A26E355']
del hashdata['4B880037CEB3621E10862F6E26D18867']
del hashdata['CBA1F6883EFD94331565D501E947CBC7']
del hashdata['C65C60B98911B4051AD61EDC71189615']
del hashdata['094B5EB473294874EF4D89EAA63B5218']
del hashdata['341FBF03707E4423910D5F362F8285FE']
del hashdata['469B85B7916A22B9880C18C25A6DA279']
del hashdata['63BD6013AE8CF977BB029612375DD078']

print  hashdata.get('1E1A55A4583B498D7CF9B1296D0E0D02')
print  hashdata.get('D55E1EFA7F3717352A32DF931A26E355')
print  hashdata.get('4B880037CEB3621E10862F6E26D18867')
print  hashdata.get('CBA1F6883EFD94331565D501E947CBC7')
print  hashdata.get('C65C60B98911B4051AD61EDC71189615')
print  hashdata.get('094B5EB473294874EF4D89EAA63B5218')
print  hashdata.get('341FBF03707E4423910D5F362F8285FE')
print  hashdata.get('469B85B7916A22B9880C18C25A6DA279')
print  hashdata.get('63BD6013AE8CF977BB029612375DD078')
##print hashdata
print len(hashdata)

with open('hashdata_v.pkl', 'wb') as output:
    pickle.dump(hashdata, output)
output.close()
