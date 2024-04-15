from Config import config
from datetime import datetime
import requests
import json
from SmartData import Plcenter_data

#查询123级警情
def getAlarmMessages():
    beginDate = datetime.strftime(datetime.now(),'%Y-%m-%d')
    endDate = datetime.strftime(datetime.now(),'%Y-%m-%d')
    url = 'http://'+config.setuip()+'/smartSecurityAPI/alarmMessages/alarm/getAlarmMessages?currentPage=1&pageSize=10&pushStatus=0,1&alarmSourceCode=&alarmLevelCode=&alarmMemo=&beginDate='+beginDate+'+00:00:00&endDate='+endDate+'+23:59:59&address=&importantEquip='
    headers = config.getuserinfo()
    res = requests.get(url=url,headers=headers,params=None).json()
    print(res)

#处理123级警情
def disAlarm():
    url = 'http://' + config.setuip() + '/smartSecurityAPI/alarmHandler/alarmHandled'
    headers = config.getuserinfo()
    data = json.dumps(
        {
            "alarmHandlingCode": "2",
            "handleResult": "处置",
            "action": 0,
            "alarmId": Plcenter_data.disAlarm_data()
        }
    )
    res = requests.post(url=url,headers=headers,data=data).json()
    print(res)

# 查询4级警情
def getFourLevelAlarmMessages():
    beginDate = datetime.strftime(datetime.now(),'%Y-%m-%d')
    endDate = datetime.strftime(datetime.now(),'%Y-%m-%d')
    url = 'http://'+config.setuip()+'/smartSecurityAPI/alarmMessages/alarm/getFourLevelAlarmMessages?currentPage=1&pageSize=10&pushStatus=0,1&alarmSourceCode=&alarmLevelCode=&alarmMemo=&beginDate='+beginDate+'+00:00:00&endDate='+endDate+'+23:59:59&address=&importantEquip='
    headers = config.getuserinfo()
    res =requests.get(url=url,headers=headers,params=None).json()
    print(res)

# 处置4级警情
def disfourAlarm():
    res=Plcenter_data.disfourAlarm_data()
    if res == '未查询到4级警情数据':
        print(res)
    else:
        url = 'http://' + config.setuip() + '/smartSecurityAPI/alarmHandler/alarmHandled'
        headers = config.getuserinfo()
        data = json.dumps(
            {
                "alarmHandlingCode": "4",
                "handleResult": "处置",
                "action": 0,
                "alarmId": Plcenter_data.disfourAlarm_data()
            }
        )
        diefourAlarm_res = requests.post(url=url, headers=headers, data=data).json()
        print(diefourAlarm_res)
        return diefourAlarm_res

if __name__ == '__main__':
    getFourLevelAlarmMessages()