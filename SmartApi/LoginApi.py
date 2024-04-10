import base64
import json

import requests
from Config import config
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pksc1_v1_5

def login(userAccount,password):
    input_userAccount = userAccount
    publicKey_url = "http://" + config.setuip() + '/smartSecurityAPI/userLogin/getPublicKey?userAccount=' + str(input_userAccount)
    res = requests.get(url=publicKey_url).json()
    public = res.get('result')
    publicKey = '-----BEGIN PUBLIC KEY-----\n' + public + '\n-----END PUBLIC KEY-----'
    rsakey = RSA.importKey(publicKey)
    cipher = Cipher_pksc1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(password.encode()))
    password=cipher_text.decode()
    payload = json.dumps({
        "userAccount": userAccount,
        "password": password
    })
    login_url = "http://" + config.setuip() +'/smartSecurityAPI/userLogin/login'
    res=requests.post(url=login_url, headers=config.setloginheaders(), data=payload).json()
    print(res)
    return res

if __name__ == '__main__':
    login('5229455','Admin@123')