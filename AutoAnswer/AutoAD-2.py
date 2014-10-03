#coding=gbk
#Introduction：AutoAD-2 for Web
import urllib,urllib2
import re
import cookielib
import sys

class AutoAD():
    url = 'http://www.example.cn/public/Default.aspx'
    posturl = 'http://www.example.cn/StaticPage/subject/comments.aspx '

    agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0'
    headers = {'User-Agent': agent,'DNT':'1','X-Forwarded-For':'127.0.0.1'}
    postdata = {'__VIEWSTATE' : '',         #需捉POST
                'ctl00$ContentPlaceHolder1$LoginView1$Login1$UserName' : '',        #登录帐号
                'ctl00$ContentPlaceHolder1$LoginView1$Login1$Password' : '',        #登录密码
                'ctl00$ContentPlaceHolder1$LoginView1$Login1$BtnLogin' : ''}
    post = urllib.urlencode(postdata)

    wenzi = ''      #广告语

    cookie = cookielib.CookieJar()
    brower = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))     #带COOKIE访问

    req = urllib2.Request(url ,post ,headers)       #对url进行post
    response = brower.open(req).read()

    for Qnumber in xrange(1,2573):
        postAData = {'__EVENTTARGET' : 'btn_commit',
              'hid_Id' : Qnumber,
              'txt_comments':wenzi}
        postAD = urllib.urlencode(postAData)

        req = urllib2.Request(posturl ,postAD ,headers)
        response = brower.open(req).read()

        sys.stdout.write("Completing: %i%%\r" %(Qnumber*100/2573))
        sys.stdout.flush()

if __name__=="__main__":
    AutoAD()
