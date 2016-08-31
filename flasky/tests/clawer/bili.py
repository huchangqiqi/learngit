import requests
import re
import json
import datetime
import asyncio


def get_info(uid):
    url_info = 'http://space.bilibili.com/ajax/member/GetInfo?mid='
    udi = str(uid)
    return loop.run_in_executor(None, requests.get, url_info+uid)


async def user_info(num):
    for uid in range(num, num + 10):
        info = await get_info(uid)
        info = json.loads(info.txt)['data']
        try:
            print("ok :", uid)
            print(info)
        except UnicodeDecodeError as e:
            print("UnicodeDecodeError:", e)
        except TypeError:
            print(info)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait([user_info(x) for x in range(1, 1000, 10)]))
except Exception as e:
    print("error :", e)
