from Config import config
import requests

# 民警信息
def plcinfo():
    departId = str(526101)
    headers = config.getuserinfo()
    url = 'http://'+config.setuip()+'/smartSecurityAPI/bus/person/findAll?departId='+departId
    res = requests.get(url=url,headers=headers,params=None).json()
    return res

# 实时警情
def plcrealtime():
    headers = config.getuserinfo()
    url = 'http://'+config.setuip()+'/smartSecurityAPI/zxw/getZxwBuildFloorTree'
    res =requests.get(url=url,headers=headers,params=None).json()
    return res

# 警情分析
def plcanal():
    headers = config.getuserinfo()
    url = 'http://'+config.setuip()+'/smartSecurityAPI/bus/dept/queryDepartStatistics'
    res =requests.get(url=url,headers=headers,params=None).json()
    return res

