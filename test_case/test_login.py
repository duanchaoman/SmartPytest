import os
import sys

import pytest

path=os.path.abspath(os.path.dirname('E:\pypro\SmartPytest\SmartApi'))
sys.path.append(path)
import allure
from SmartApi import LoginApi

@allure.feature('登录')
class Test_Pytest():
    @allure.title('正常登录')
    def test_login(self):
        res=LoginApi.login('5229455','Admin@123')
        msg=res.get('msg')
        assert msg =='OK'

    @allure.title('异常登录')
    def test_errlogin(self):
        res=LoginApi.login('123','123')
        msg = res.get('msg')
        assert msg == 'OK'

if __name__ == '__main__':
    pytest.main(['-s', '-r', './test_case/test_login','nu1'])