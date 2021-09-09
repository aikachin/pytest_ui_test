import xlrd
import openpyxl
import os

class ExcelHandler:
    def __init__(self, fpath):
        self.fpath = fpath

    #读取Excel中的数据，最终返回的结果是list，list中包含字典
    def read(self, sheet_name):
        # 打开文件
        wb = xlrd.open_workbook(self.fpath)
        # 获取工作表
        ws = wb.sheet_by_name(sheet_name)
        all_data = []
        values = ws.row_values(0)
        for i in range(1,ws.nrows):
            data = {}
            for j  in range(ws.ncols):
                data[values[j]] = ws.row_values(i)[j]
            all_data.append(data)
        return all_data

    def write(self, sheet_name, content, row, column):
        # 写入excel
        wb = openpyxl.load_workbook(self.fpath)
        ws = wb[sheet_name]
        ws.cell(row=row, column=column).value = content
        wb.save(self.fpath)

    #根据给定的sheet名称和sheet中对应的NAME字段的值，返回对应的selector和定位元素
    def readSpecialValue(self,sheet_name,name):
        all_data = self.read(sheet_name)
        type_ele = []
        for data in all_data:
            if data['NAME'] == name:
                type_ele.append(data['SELECTOR'])
                type_ele.append(data['ELEMENT'])
        return type_ele


# if __name__ == '__main__':
#     root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     dir_report = root_path + '\\data\\test_case1.xls'
#     excel = ExcelHandler(dir_report)
#     data = excel.readSpecialValue('login','login_name')
#
#     print(data[1])
