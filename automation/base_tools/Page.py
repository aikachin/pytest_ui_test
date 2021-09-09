#coding=utf-8
import time
import os.path
from  automation.base_tools import logger
from  automation.base_tools import Browser
from PIL import Image
import pytesseract
from automation.base_tools import ReadData

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log = logger.Logger().logger
browser = Browser.Browser()
driver = browser.openBrowser()
excelHandler = ReadData.ExcelHandler(path + '\\data\\basic.xls')


class Page(object):

      #查找元素
    def findElement(self,selector,eleName):
        element = None
        try:
            if selector == 'id':
                element = driver.find_element_by_id(eleName)
            elif selector =='xpath':
                element = driver.find_element_by_xpath(eleName)
            elif selector == 'class':
                element = driver.find_element_by_class_name(eleName)
            elif selector == 'tag':
                element = driver.find_elements_by_tag_name(eleName)
            elif selector == 'classes':
                element = driver.find_elements_by_class_name(eleName)
                print(element)
                log.info("找到元素" + eleName)
            return element
        except:
            log.info('没找到元素'+eleName)


    #输入元素
    def input(self,selector,eleName,txt):
        el = self.findElement(selector,eleName)
        try:
            el.send_keys(txt)
            log.info("输入框中输入元素"+txt)
        except NameError as e:
            log.error("写入输入框中失败")



    #点击
    def click(self,selector,eleName):
        el = self.findElement(selector, eleName)
        try:
            el.click()
            log.info("点击元素成功" )
        except NameError as e:
            log.error("写入输入框失败")

    #截图

    def take_screenshot(self):
        screen_dir = path + '\\screenshot\\'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = screen_dir + rq + '.png'
        try:
            driver.get_screenshot_as_file(screen_name)
            log.info("截图成功")
            return screen_name
        except Exception as e:
            log.error("截图失败", format(e))

    def isElementExist(self, xpath):
        flag = True
        try:
            driver.find_element_by_xpath(xpath)
            return flag
        except:
            flag = False
            return flag

    #获取登录验证码，由于识别率低，放弃不用
    def getCode(self):
        time.sleep(3)
        sreenName = self.take_screenshot()
        log.info("登录整个界面截图已保存")
        im = Image.open(sreenName)
        print(im.size)
        im.show()

        region = (1327,445,1438,552)
        nimg = im.crop(region)
        screen_dir = path + '\\screenshot\\'
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        pic_name = screen_dir + rq + '.png'
        nimg.save(pic_name)
        log.info("验证码区域已经保存")
        image = Image.open(pic_name)

        vcode = pytesseract.image_to_string(image,lang='chi_sim')
        return vcode


    #获取下拉框数据
    def getCheckBox(self,selector,elename,txt):
        # 处理标准下拉选择框,随机选择
        select1 = self.findElement(selector,elename)
        try:
            for s1 in select1:
                if  s1.get_attribute("title") == txt:
                    s1.click()
                    break
        except NameError as e:
            log.error("Failed to click the element with %s" % e)

    #获取菜单并跳转到相应的页面，根据class获取所有的菜单元素，由于不能直接点击隐藏的菜单， 所以只能从菜单的一级一级点击。最后一个参数是菜单路径，以-分割，如：指挥调度系统-生产计划-热源计划
    def getMenu(self,selector,elename,txt):
        # 处理标准下拉选择框,随机选择
        select1 = self.findElement(selector, elename)
        log.info(select1)
        menuName = txt.split('-')
        try:
            for s1 in select1:
                for name in menuName:
                    if s1.get_attribute("title") == name:
                        s1.click()

            time.sleep(1)
            self.take_screenshot()
        #点击完菜单之后把菜单恢复到原状，否则会有问题
            for s1 in select1:
                if s1.get_attribute("title") == menuName[0]:
                    s1.click()
        except NameError as e:
            log.error("Failed to click the element with %s" % e)
