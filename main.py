from random import randint

import execjs
import time
import requests


def you(inp):
    url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    headers = {
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                      " (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Referer": "https://fanyi.youdao.com/",
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-839755876@10.169.0.102; OUTFOX_SEARCH_USER_ID_NCOO=743999617.3442072; JSESSIONID=aaabNtW3FwvJb4HKqmz2x; ___rl__test__cookies=1638952918194',
        'Host': 'fanyi.youdao.com',
        'Origin': 'https://fanyi.youdao.com'
    }
    f = open('spa/spa6_js.js', encoding='utf-8').read()
    ctx = execjs.compile(f)
    lts = int(time.time() * 1000)
    salt = str(lts) + str(randint(0, 10))
    print('5.0 '+headers["user_agent"])
    bv = ctx.call('md5', '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36')
    print(f"fanyideskweb{inp}{salt}Y2FYu%TNSbMCxc3t2u^XT")
    sign = ctx.call('md5', f"fanyideskweb{inp}{salt}Y2FYu%TNSbMCxc3t2u^XT")
    print(lts, salt, bv, sign)
    data = {
        'i': inp,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        # 'salt': str(salt),
        # 'sign': str(sign),
        # 'lts': str(lts),
        # 'bv': str(bv),
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
    }
    req = requests.post(url, headers=headers, data=data)
    print(req.status_code)
    print(req.json())


you("我来自中国")




