import os
import sys

import pytest

path=os.path.abspath(os.path.dirname('E:\pypro\SmartPytest\SmartApi'))
sys.path.append(path)
import allure
from SmartApi import PlcenterApi

@allure.feature('警情中心')
class Test_Pytest():
    @allure.title('获取123级警情信息')
    def test_getAlarmMessages(self):
        res = PlcenterApi.getAlarmMessages()
        assert res.get('msg') == 'OK'

    @allure.title('处置123级警情')
    def test_disAlarm(self):
        res = PlcenterApi.disAlarm()
        assert res.get('msg') =='OK'

    @allure.title('获取4级警情信息')
    def test_getFourLevelAlarmMessages(self):
        res = PlcenterApi.getFourLevelAlarmMessages()
        assert res.get('msg') =='OK'

    @allure.title('处置4级警情')
    def test_disfourAlarm(self):
        res = PlcenterApi.disfourAlarm()
