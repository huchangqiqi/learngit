

import requests
import os
import json

import time
from bs4 import BeautifulSoup


def login():
    url = 'http://www.zhihu.com'
    loginUrl = 'http://www.zhihu.com/login/email'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
        "Referer": "https://www.zhihu.com/",
        "Host": "www.zhihu.com",
    }
    data = {
        'email': 'huchangqiqi@gmail.com',
        'password': 'Hu7intheend7',
        'rememberme': "true",
    }
    s = requests.session()
    if os.path.exists('cookiefile'):
        with open('cookiefile') as f:
            cookie = json.load(f)
        s.cookies.update(cookie)
        req = s.get(url, headers=headers)
        soup = BeautifulSoup(req.text, "html.parser")
        xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')
    else:
        req = s.get(url, headers=headers)
        soup = BeautifulSoup(req.text, "html.parser")
        xsrf = soup.find('input', {'name': '_xsrf', 'type': 'hidden'}).get('value')
        data['_xsrf'] = xsrf

        timestamp = int(time.time() * 1000)
        captchaUrl = 'http://www.zhihu.com/captcha.git?=' + str(timestamp)
        print(captchaUrl)
        with open('zhihucpatcha.gif', 'wb') as f:
            captchaReq = s.get(captchaUrl, headers=headers)
            f.write(captchaReq.content)
        loginCaptcha = input('input captcha:\n').strip()
        data['captcha'] = loginCaptcha
        print(data)
        loginReq = s.post(loginUrl, headers=headers, data=data)
        if not loginReq.json()['r']:
            print(s.cookies.get_dict())
            with open('cookiefile', 'wb') as f:
                json.dump(s.cookies.get_dict(), f)
        else:
            print('login fail')

if __name__ == '__main__':
    login()