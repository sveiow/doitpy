#coding=utf-8
import pickle
import random

hashdict = {

    }
for i in range (9):
    Qmd5 = '%s' % random.randrange(1,10)
    md5 = '%s' % random.randrange(1,100)
    hashdict[Qmd5] = md5
    
print Qmd5,md5

print hashdict

with open('hashdict.pk', 'a') as output:
    pickle.dump(hashdict, output)
