import json
import urllib3
from rio_spider import settings
from rio_spider.tools.selenium_tool import SeleniumLogin


def storeCookies():
    cookies_pool = []
    with open('./cookies.txt', 'w') as f:
        for item in settings.ACCOUNTS:
            print('Login User : ', item['user'])
            status, cookies = SeleniumLogin().login_douban(item['user'], item['password'])
            print('Login Success : ', cookies)
            cookies_pool.append(cookies)
        f.write(json.dumps(cookies_pool))


def getCookies():
    cookies_pool = []
    with open('cookies.txt', 'r') as f:
        cookies_pool = json.loads(f.read())
        print(cookies_pool)


# storeCookies()
# getCookies()

http = urllib3.PoolManager()
