import json
from datetime import datetime,timedelta


def add_onealarm_data():
    this_time=datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
    alarm_data=json.dumps(
        {
            "createTime": "",
            "handledTime": "",
            "alarmTime": this_time,
            "address": "监一栋",
            "alarmMemo": "非法翻越",
            "alarmLevelCode": "01",
            "alarmPerson": "姓名",
            "alarmPersonTel": "13111111111",
            "alarmDescription": "描述",
            "receiverUserId": "2d07169d5a434e20b0a4742bb43bd8ff",
            "result": "",
            "positionCode": "5223010030090300080020000000001000000000",
            "alarmAddressFloorId": "",
            "alarmCoordinate": "{\"longitude\":104.91862652518513,\"latitude\":25.13830092226664,\"altitude\":65.78760467021766}",
            "inRoom": 2,
            "addressId": "522301-f05257da869443379d54b6117c7e9ca2",
            "alarmSourceCode": "02",
            "status": "0"
        }
    )
    return alarm_data
def add_twoalarm_data():
    this_time = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
    alarm_data =json.dumps(
        {
            "createTime": "",
            "handledTime": "",
            "alarmTime": this_time,
            "address": "监一栋",
            "alarmMemo": "非法翻越",
            "alarmLevelCode": "02",
            "alarmPerson": "姓名",
            "alarmPersonTel": "13111111111",
            "alarmDescription": "描述",
            "receiverUserId": "2d07169d5a434e20b0a4742bb43bd8ff",
            "result": "",
            "positionCode": "5223010030090300080020000000001000000000",
            "alarmAddressFloorId": "",
            "alarmCoordinate": "{\"longitude\":104.91862652518513,\"latitude\":25.13830092226664,\"altitude\":65.78760467021766}",
            "inRoom": 2,
            "addressId": "522301-f05257da869443379d54b6117c7e9ca2",
            "alarmSourceCode": "02",
            "status": "0"
        }
    )
    return alarm_data

def add_threealarm_data():
    this_time = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
    alarm_data = json.dumps(
        {
            "createTime": "",
            "handledTime": "",
            "alarmTime": this_time,
            "address": "监一栋",
            "alarmMemo": "非法翻越",
            "alarmLevelCode": "03",
            "alarmPerson": "姓名",
            "alarmPersonTel": "13111111111",
            "alarmDescription": "描述",
            "receiverUserId": "2d07169d5a434e20b0a4742bb43bd8ff",
            "result": "",
            "positionCode": "5223010030090300080020000000001000000000",
            "alarmAddressFloorId": "",
            "alarmCoordinate": "{\"longitude\":104.91862652518513,\"latitude\":25.13830092226664,\"altitude\":65.78760467021766}",
            "inRoom": 2,
            "addressId": "522301-f05257da869443379d54b6117c7e9ca2",
            "alarmSourceCode": "02",
            "status": "0"
        }
    )
    return alarm_data

def add_fouralarm_data():
    this_time = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
    alarm_data = json.dumps(
        {
            "createTime": "",
            "handledTime": "",
            "alarmTime": this_time,
            "address": "监一栋",
            "alarmMemo": "非法翻越",
            "alarmLevelCode": "04",
            "alarmPerson": "姓名",
            "alarmPersonTel": "13111111111",
            "alarmDescription": "描述",
            "receiverUserId": "2d07169d5a434e20b0a4742bb43bd8ff",
            "result": "",
            "positionCode": "5223010030090300080020000000001000000000",
            "alarmAddressFloorId": "",
            "alarmCoordinate": "{\"longitude\":104.91862652518513,\"latitude\":25.13830092226664,\"altitude\":65.78760467021766}",
            "inRoom": 2,
            "addressId": "522301-f05257da869443379d54b6117c7e9ca2",
            "alarmSourceCode": "02",
            "status": "0"
        }
    )
    return alarm_data

def add_recordalarm_data():
    createTime = datetime.strftime(datetime.now(),'%Y-%m-%d')+' 00:00:00'
    handledTime = datetime.strftime(datetime.now(),'%Y-%m-%d')+' 23:59:59'
    alarmTime = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
    alarm_data =json.dumps(
        {
            "createTime": createTime,
            "handledTime": handledTime,
            "alarmTime": alarmTime,
            "address": "监一栋",
            "alarmMemo": "区域入侵",
            "alarmLevelCode": "04",
            "alarmPerson": "姓名",
            "alarmPersonTel": "13333333333",
            "alarmDescription": "描述",
            "receiverUserId": "2d07169d5a434e20b0a4742bb43bd8ff",
            "result": "处置结果",
            "positionCode": "5223010030090300080020000000001000000000",
            "alarmAddressFloorId": "",
            "alarmCoordinate": "{\"longitude\":104.91863733105808,\"latitude\":25.138334593467683,\"altitude\":65.78797080499216}",
            "inRoom": 2,
            "addressId": "522301-f05257da869443379d54b6117c7e9ca2",
            "alarmSourceCode": "03",
            "status": "3"
        }
    )
    return alarm_data

if __name__ == '__main__':
   print(add_recordalarm_data())