#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json
import re

class Getid:
    def __init__(self, link):
        self.link = str(link)
    def get_pid(self):
        try:
            pattern = re.compile('(?<=&id=)[\d]*(?=&)')
            taobao = re.compile("taobao.com")
            tmall = re.compile("tmall.com")
            pid = re. search(pattern, self.link).group(0)
            if re. search(taobao, self.link) != None:
                return (pid, 1)
            if re. search(tmall, self.link) != None:
                return (pid, 2)
        except:
            pattern = re.compile('(?<=\?id=)[\d]*(?=&)')
        
    def get_sellerid(self):
        pattern = re.compile('(?<=sellerId:")[\d]*(?=")')
        r = requests.get(self.link).text.encode("utf-8")
        sellerid = re. search(pattern, r)
        return sellerid.group(0)

def getview_taobao(sellerid, pid):
    pagenum = 1
    while 1:
        """"userNumId 指卖家id , auctionNumId 指商品id， currentPageNum 指页码"""
        headers = {"User-Agent": "Mozilla/5.0 AppleWebKit/537.36 Chrome/33.0.1750.58 Safari/537.36"}
        page = requests.get("http://rate.taobao.com/feedRateList.htm?userNumId={}&auctionNumId={}&currentPageNum={}".format(sellerid, pid, pagenum), headers=headers)
        page = page.text.strip()[1:-1].encode("utf8")
        pagejson = json.loads(page, parse_constant=True)
##        with open("tb_"+str(pagenum), "w") as p:
##                p.write(page)

        user = [i["user"] for i in pagejson["comments"]]
        contents = [i["content"] for i in pagejson["comments"]]
        date = [i["date"] for i in pagejson["comments"]]
        nick = [i["nick"] for i in list(user)]
        rank = [i["rank"] for i in list(user)]
        w = zip(nick, rank, date, contents)
        for i in w:
            a = "%s, %s, %s, %s"%(i[0], i[1], i[2], i[3])
            a = a.encode("utf8")
            with open("tb_"+str(pid), "a") as p:
                p.write("%s \n\n"%a)
        pagenum += 1

def getview_tmall(sellerid, pid):
    pagenum = 1
    while 1:
        headers = {"User-Agent": "Mozilla/5.0 AppleWebKit/537.36 Chrome/33.0.1750.58 Safari/537.36"}
        page = requests.get("http://rate.tmall.com/list_detail_rate.htm?sellerId={}&itemId={}&currentPage={}".format(sellerid, pid, pagenum), headers=headers)
        page = page.text.strip()[13:].encode("utf8")
        pagejson = json.loads(page, parse_constant=True)
##        with open("tmall_"+str(pagenum), "w") as p:
##                p.write(page)

        displayUserNick = [j["displayUserNick"] for j in pagejson["rateList"]]
        rateDate = [j["rateDate"] for j in pagejson["rateList"]]
        rateContent = [j["rateContent"] for j in pagejson["rateList"]]
        w = zip(displayUserNick, rateDate, rateContent)
        for i in w:
                a = "%s, %s, %s"%(i[0], i[1], i[2])
                a = a.encode("utf8")
                with open("tmall_"+str(pid), "a") as p:
                    p.write("%s \n\n"%a)

        lastpage = pagejson['paginator']['lastPage']
        if pagenum != lastpage:
                pagenum += 1
                continue
        else:
            break

def main():
    print u"""请输入链接："""
    url = str(raw_input(""))
    pid = Getid(url).get_pid()[0]
    mode = Getid(url).get_pid()[1]
    sellerid = Getid(url).get_sellerid()
    if mode == 1:
        getview_taobao(sellerid, pid)
    if mode == 2:
        getview_tmall(sellerid, pid)

if __name__ == "__main__":
    main()
