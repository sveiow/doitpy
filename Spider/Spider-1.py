#coding=utf-8
#Introduction：练习爬虫，带COOKIE访问，登录爬取某学车网信息
import urllib,urllib2
import re
import cookielib
import time  
starttime = time.clock() 

CardNum = re.compile('<span\s+?id="ctl00_ContentPlaceHolder1_lblCardNum">(?P<content>.+?)</span>')
Name = re.compile('<span\s+?id="ctl00_ContentPlaceHolder1_lblName">(?P<content>.+?)</span>')
Sex = re.compile('<span\s+?id="ctl00_ContentPlaceHolder1_lblSex">(?P<content>.+?)</span>')
LinkTel = re.compile('<span\s+?id="ctl00_ContentPlaceHolder1_lblLinkTel">(?P<content>.+?)</span>')
Address = re.compile('<span\s+?id="ctl00_ContentPlaceHolder1_lblAddress">(?P<content>.+?)</span>')
CertificateNo = re.compile('<span\s+?id="ctl00_ContentPlaceHolder1_lblCertificateNo">(?P<content>.+?)</span>')
SchoolName = re.compile('<span\s+?id="ctl00_ContentPlaceHolder1_lblSchoolName">(?P<content>.+?)</span>')

box = (CardNum,Name,Sex,LinkTel,Address,CertificateNo,SchoolName)


class getit():
    for a in range(100,110):
        account = 'fs8800%s'%a
##        print account
        url = 登录地址
        read = 爬取地址

        agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'
        postdata = {'__VIEWSTATE' : '/wEPDwUKLTQwMzQ5MzE4OA9kFgJmD2QWAgIDD2QWAmYPZBYCAgMPFgIeC18hSXRlbUNvdW50AgEWAmYPZBYCZg8VBCIuLi9OZXdzX05DL0pEVDBISjY2ODY2VlRGNDZfMS5odG1sOjfmnIjpopjlupPljYfnuqfvvIznp5Hnm67kuIDlkoznp5Hnm67kuInlkITmlrDlop4xMDDpgZPpophRPGZvbnQgY29sb3I9cmVkPjfmnIjpopjlupPljYfnuqfvvIznp5Hnm67kuIDlkoznp5Hnm67kuInlkITmlrDlop4xMDDpgZPpopg8L2ZvbnQ+CTIwMTQvNy8zMWRk',
                    'ctl00$ContentPlaceHolder1$LoginView1$Login1$UserName' : account,
                    'ctl00$ContentPlaceHolder1$LoginView1$Login1$Password' : '123456',
                    'ctl00$ContentPlaceHolder1$LoginView1$Login1$BtnLogin' : ''}
        post = urllib.urlencode(postdata)
        headers = {'User-Agent': agent, 'DNT': 1}

        cookie = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))     #带COOKIE访问
        opener.addheaders = [('User-Agent',agent),('DNT','1')]
        req = urllib2.Request(url, post,)
        response = opener.open(req)
        req2 = urllib2.Request(read)
        htmlsource = opener.open(req2).read().decode("gbk")
    ##    return htmlsource

        def catch(name,htmlsource):
            try:
                math = re.search(name,htmlsource)
                content = math.group("content")
                return content
            except AttributeError:
                content = "NONE"

    ##    def run():
        print "CardNum =",catch(CardNum,htmlsource)
        print "Name =",catch(Name,htmlsource)
        print "Sex=",catch(Sex,htmlsource)
        print "LinkTel =",catch(LinkTel,htmlsource)
        print "LinkTel =",catch(Address,htmlsource)
        print "CertificateNo =",catch(CertificateNo,htmlsource)
        print "CertificateNo =",catch(SchoolName,htmlsource)
        print "= = = = ="
endtime = time.clock()  
print (endtime-starttime)
if __name__=="__main__":
    getit()
##    profile.run('getit()')

