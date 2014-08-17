#coding=utf-8
#Introduction:小米签到
from splinter import Browser
import logging
##import time
##import sys

def qd():
    browser = Browser('firefox',
    profile = 'D:\UsersDocuments\FFmissions',
    user_agent = "Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en)")
    browser.visit(xiaomi)
##    time.sleep(1)
    browser.find_by_id('username').fill(username)
    browser.find_by_id('userPwd').fill(password)
    browser.find_by_id('login_button').click()
##    time.sleep(1)
    if browser.is_text_present(username, wait_time=1):
        print ('login success!!')
        logging.info('%s login success!!'%username)
        browser.visit('http://bbs.xiaomi.cn/qiandao/')
##        time.sleep(1)
##        添加今天是否有签到的判断，有很多判断方式by_xpath，by_id，by_class
        if browser.find_by_id("qdbn2").visible:
            print ('you had signed!')
            logging.info('you had signed!')
        else:
            browser.find_by_id('share').click()
##            time.sleep(1)
            print ('qd success!!')
            logging.info('qd success!!')
##        browser.visit('http://bbs.xiaomi.cn/forum.php?mobile=no') 
        browser.visit('http://home.xiaomi.cn/home.php?mod=task&do=apply&id=81')
        if browser.is_text_present(u'\u672c\u671f\u60a8\u5df2\u7533\u8bf7\u8fc7\u6b64\u4efb\u52a1'):
            print ('done!')
            logging.info('done!')
            browser.quit()
        else:
            browser.visit('http://home.xiaomi.cn/home.php?mod=task&do=draw&id=81')
            if browser.is_text_present(u'\u4efb\u52a1\u5df2\u6210\u529f\u5b8c\u6210'):
                print ('mission success!!')
                logging.info('mission success!!')
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
        
if __name__ == '__main__':
    xiaomi = 'https://account.xiaomi.com/pass/serviceLogin'
    username = raw_input('Enter login username: ')
    password = raw_input('Enter login password: ')
##    这里的顺序很重要，调换了就会报错，所以要认识到PY的执行顺序
    outputlog()
    qd()

