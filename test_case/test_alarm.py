import os
import sys
import allure
import pytest
path=os.path.abspath(os.path.dirname('E:\pypro\SmartPytest\SmartApi'))
sys.path.append(path)
from SmartApi import AlarmApi

@allure.feature('人工警情')
class Test_AlarmPytest():
    @allure.title('添加一级警情')
    def test_addonealarm(self):
        res=AlarmApi.add_onealarm()
        assert res.get('msg') == 'OK'

    @allure.title('添加二级警情')
    def test_addtwoalarm(self):
        res=AlarmApi.add_twoalarm()
        assert res.get('msg') == 'OK'

    @allure.title('添加三级警情')
    def test_addthreealarm(self):
        res=AlarmApi.add_threealarm()
        assert res.get('msg') == 'OK'

    @allure.title('添加四级警情')
    def test_addfouralarm(self):
        res=AlarmApi.add_fouralarm()
        assert res.get('msg') == 'OK'

    @allure.title('补录')
    def test_recordalarm(self):
        res=AlarmApi.add_fouralarm()
        assert res.get('msg') =='OK'









if __name__ == '__main__':
    pytest.main(['-s', '-r', './test_case/test_alarm'])