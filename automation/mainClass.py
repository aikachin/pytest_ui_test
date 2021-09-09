import os,pytest


if __name__ == "__main__":
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dir_report =root_path+'\\automation\\report'
    dir_result = root_path+'\\automation\\result'
   # dir_exe = root_path+'\\automation\\case\\test_case1.py::test_01'
    dir_exe = root_path + '\\automation\\case'
    #最后一个参数是运行执行的case
    pytest.main(['-v', '--alluredir', dir_result, dir_exe])
    #也可以自定义执行哪些case，如果有多个，用英文逗号隔开即可
    #pytest.main(['-v','--alluredir',dir_result,root_path + '\\automation\\case\\test_login.py',root_path + '\\automation\\case\\test_case2.py'])
    allure_cmd = 'allure generate '+ dir_result +' -o '+dir_report+' --clean'
    os.system(allure_cmd)



