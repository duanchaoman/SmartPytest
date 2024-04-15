from SmartApi import LoginApi


def setuip():
    uip = '192.168.1.253'
    return uip

def getuserinfo():
    res=LoginApi.login('5229455','Admin@123')
    headers=res[1]
    return headers

