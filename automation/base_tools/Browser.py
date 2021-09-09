from selenium import  webdriver
import configparser
import os
from  automation.base_tools import logger
import time

log = logger.Logger().logger

class Browser(object):

    #打开浏览器
    def openBrowser(self):
        # 获取浏览器驱动，这里只做了Chrome浏览器的
        self.driver = webdriver.Chrome(executable_path='chromedriver90.exe')
        log.info("获取浏览器的驱动")

        config = configparser.ConfigParser()
        dirpath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\config\\config.ini'
        config.read(dirpath)
        # #获取登录信息
        URL = config.get('login', 'urlName')
        log.info("读取配置文件URL的信息：" + URL)
        # 打开浏览器登录界面
        self.driver.get(URL)
        time.sleep(5)

        #设置浏览器窗口大小
        self.driver.set_window_size(1920, 1080)
        self.driver.maximize_window()
        return self.driver


    #打开url
    def openUrl(self,url):
        log.info('打开浏览器的页面')
        self.driver.get(url)

    #关闭浏览器
    def closeWindow(self):
        log.info('关闭浏览器的页面')
        self.driver.quit()

    #浏览器前进
    def fowardWindow(self):
        log.info('前进浏览器的页面')
        self.driver.forward()

    #浏览器后退
    def backWindow(self):
        log.info('后退浏览器的页面')
        self.driver.back()




