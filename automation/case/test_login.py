from automation.base_tools import Page
from automation.base_tools.ReadData import ExcelHandler
from automation.base_tools.logger import Logger
import allure
import os
import pytest
import time
import configparser


path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p = Page.Page()
log = Logger().logger
excelHandler = ExcelHandler(path + '\\data\\basic.xls')


@allure.feature('页面登录功能')
@pytest.mark.run(order=1) #优先执行登录功能
def test_login():
    config = configparser.ConfigParser()
    dirPath = path + '\\config\\config.ini'
    config.read(dirPath)

    # 从配置文件config.ini获取登录信息
    username = config.get('login', 'username')
    password = config.get('login', 'password')
    env = config.get('login', 'env').encode('GBK').decode('utf-8')
    code = config.get('login', 'code')

    # 登录操作，读取Excel中名为login的sheet页
    all_data = excelHandler.read('login')
    # 循环all_data列表，找到登录名、密码、验证码、环境对应的选择器和定位元素
    for data in all_data:
        if data['NAME'] == 'login_name':
            p.input(data['SELECTOR'], data['ELEMENT'], username)
        elif data['NAME'] == 'login_pass':
            p.input(data['SELECTOR'], data['ELEMENT'], password)
        elif data['NAME'] == 'login_code':
            p.input(data['SELECTOR'], data['ELEMENT'], code)
        elif data['NAME'] == 'login_click_env':
            p.click(data['SELECTOR'], data['ELEMENT'])
        elif data['NAME'] == 'select_env':
            p.getCheckBox(data['SELECTOR'], data['ELEMENT'], env)
        elif data['NAME'] == 'login_sub':
            p.click(data['SELECTOR'], data['ELEMENT'])
    log.info('登录成功！')
    time.sleep(1)




