from datetime import datetime,timedelta
from Config import config
from SmartData import Alarm_data
import requests

def add_onealarm():
    url = 'http://' + config.setuip() + '/smartSecurityAPI/alarmMessages/alarm/addRecord'
    headers = config.getuserinfo()
    data = Alarm_data.add_onealarm_data()
    res=requests.post(url=url,headers=headers,data=data).json()
    print(res)
    return res
def add_twoalarm():
    url = 'http://' +config.setuip() +'/smartSecurityAPI/alarmMessages/alarm/addRecord'
    headers = config.getuserinfo()
    data = Alarm_data.add_twoalarm_data()
    res = requests.post(url=url,headers=headers,data=data).json()
    print(res)
    return res

def add_threealarm():
    url = 'http://' + config.setuip() + '/smartSecurityAPI/alarmMessages/alarm/addRecord'
    headers = config.getuserinfo()
    data = Alarm_data.add_threealarm_data()
    res = requests.post(url=url, headers=headers, data=data).json()
    print(res)
    return res

def add_fouralarm():
    url = 'http://' + config.setuip() + '/smartSecurityAPI/alarmMessages/alarm/addRecord'
    headers = config.getuserinfo()
    data = Alarm_data.add_fouralarm_data()
    res = requests.post(url=url, headers=headers, data=data).json()
    print(res)
    return res

def add_recordalarm():
    url ='http://' +config.setuip() +'/smartSecurityAPI/alarmMessages/alarm/addRecord'
    headers =config.getuserinfo()
    data = Alarm_data.add_recordalarm_data()
    res = requests.post(url=url,headers=headers,data=data).json()
    print(res)
    return res


if __name__ == '__main__':
    add_recordalarm()

