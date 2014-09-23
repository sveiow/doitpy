def wdict(dictfile,dict):
    if os.path.isfile(dictfile):
        oldict = open(dictfile,'rb')
        oldata = pickle.load(oldict)
        oldata.updata(dict)
        output = open(dictfile,'wb')
        pick.dump(oldata,output)
        output.close()
    else:
        with open(dictfile,'wb') as output:
            pickle.dump(dict,output)
        output.close()
        
def md5w(box,filepath):
    savepic = fullsc.crop(box).save(filepath,'JPEG')
    pic = open(filepath,'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    hashdict[Qmd5] = md5           #單單題目區
    hashdict_v2[AllQmd5] = md5            #圖片區+題目區
    pic.close()
    
def picmath(box,filepath,slef):
    fullsc = ImageGrab.grab()
    savepic = fullsc.crop(box).save(filepath,'JPEG')
    pic = open(filepath,'rb')
    md5 = hashlib.md5(pic.read()).hexdigest().upper()
    return md5
 