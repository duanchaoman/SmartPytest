import os
import sys
import allure
import pytest
path=os.path.abspath(os.path.dirname('E:\pypro\SmartPytest\SmartApi'))
sys.path.append(path)
from SmartApi import Plcmag

@allure.feature('警员管理')
class Test_PlcmagPytest():
    @allure.title('民警信息')
    def test_plcinfo(self):
        res=Plcmag.plcinfo()
        assert res.get('msg') == 'OK'

    @allure.title('实时警力')
    def test_plcrealtime(self):
        res=Plcmag.plcrealtime()
        assert res.get('msg') == 'OK'

    @allure.title('警情分析')
    def test_plcanal(self):
        res=Plcmag.plcanal()
        assert res.get('msg') == 'OK'



if __name__ == '__main__':
    pytest.main(['-s', '-r', './test_case/test_plcmag'])