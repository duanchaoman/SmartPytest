from datetime import datetime
from Config import config
import requests

# 获取最新123级警情信息
def disAlarm_data():
    beginDate = datetime.strftime(datetime.now(), '%Y-%m-%d')
    endDate = datetime.strftime(datetime.now(), '%Y-%m-%d')
    headers = config.getuserinfo()
    sle_Alarm = 'http://' + config.setuip() + '/smartSecurityAPI/alarmMessages/alarm/getAlarmMessages?currentPage=1&pageSize=10&pushStatus=0,1&alarmSourceCode=&alarmLevelCode=&alarmMemo=&beginDate=' + beginDate + '+00:00:00&endDate=' + endDate + '+23:59:59&address=&importantEquip='
    sle_res = requests.get(url=sle_Alarm, headers=headers, params=None).json()
    alarm = sle_res.get('result').get('records')
    alarmI = alarm[0]
    alarmId = str(alarmI.get('alarmId'))
    return alarmId


# 获取最新4级警情信息
def disfourAlarm_data():
    beginDate = datetime.strftime(datetime.now(), '%Y-%m-%d')
    endDate = datetime.strftime(datetime.now(), '%Y-%m-%d')
    headers = config.getuserinfo()
    four_url = 'http://' +config.setuip()+ '/smartSecurityAPI/alarmMessages/alarm/getFourLevelAlarmMessages?currentPage=1&pageSize=10&pushStatus=0,1&alarmSourceCode=&alarmLevelCode=&alarmMemo=&beginDate='+beginDate+'+00:00:00&endDate='+endDate+'+23:59:59&address=&importantEquip='
    four_res = requests.get(url=four_url,headers=headers,params=None).json()
    alarm = four_res.get('result').get('records')
    if len(alarm) == 0:
        outmag='未查询到4级警情数据'
        return outmag
    else:
        alarmI = alarm[0]
        alarmId = str(alarmI.get('alarmId'))
        return alarmId

if __name__ == '__main__':
    disfourAlarm_data()