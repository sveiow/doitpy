#coding=utf-8
#Introduction:聚超值签到
from splinter import Browser
import time
import logging

def qd():
##    browser = Browser('firefox'
##        , profile='D:\UsersDocuments\FFmissions')
    browser = Browser('chrome')
    browser.visit(juchaozhi)
    time.sleep(1)
    browser.find_by_name('username').fill(username)
    browser.find_by_name('password').fill(password)
    browser.find_by_name('button').click()
    time.sleep(1)
    if browser.is_text_present(username, wait_time=1):
        print ('login success!')
        logging.info('login success!')
        browser.visit('http://best.pconline.com.cn/qiandao.html')
        time.sleep(1)
##        添加今天是否有签到的判断，主要判断口id="JBar"，或者判断CSS中的元素，如.signStatus,.isgnUps
        if browser.find_by_css('.signStatus').visible:
            print ('you had signed!')
            logging.info('you had signed!')
            browser.quit()
        else:
            browser.find_by_xpath('//*[@id="JSignBox"]/a').click()
            time.sleep(1)
            print ('mission success!')
            logging.info('mission success!')
            browser.quit()
    else:
        print ('login fail!!!')
        logging.info('login fail!!!')

def outputlog():
    logging.basicConfig(
        level = logging.INFO,
        format = '%(asctime)s ----- %(module)s ----- %(message)s',
        datefmt = '%m-%d %H:%M',
        filename = 'qdlogs.log',
        filemode = 'a')

##    这里的标注是，下面的部分原来是用来定义全局变量的，而上面的指一个个的模块，还有它们的执行方式，内容等等
if __name__ == '__main__':
    juchaozhi = 'http://my.pconline.com.cn/passport/login.jsp'
    username = raw_input('Enter login username: ')
    password = raw_input('Enter login password: ')
##    这里的顺序很重要，调换了就会报错，所以要认识到PY的执行顺序
    outputlog()
    qd()
