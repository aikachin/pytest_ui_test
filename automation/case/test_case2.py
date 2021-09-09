from automation.case.test_login import p

from automation.case.test_login import path
from automation.case.test_login import log
from automation.case.test_login import excelHandler
import allure
import time


@allure.feature('任务单页面')
def test_operate2():
    # 打开菜单，需要读取Excel中的菜单信息
    all_data = excelHandler.read('menu')
    # 循环all_data列表，找到Excel中菜单对应的选择器和定位元素
    for data in all_data:
        if data['NAME'] == 'menuName':
            p.getMenu(data['SELECTOR'], data['ELEMENT'],'指挥调度系统-生产管理-任务单')
            time.sleep(1)
    for i in range(11, 20):
        print(i)

    assert 1 == 1



