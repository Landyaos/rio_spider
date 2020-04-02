import ast
from rio_spider import settings
from rio_spider.tools.selenium_tool import SeleniumLogin


def storeCookies():
    with open('./cookies.txt', 'w') as f:
        for item in settings.ACCOUNTS:
            print('Login User : ', item['user'])
            status, cookies = SeleniumLogin().login_douban(item['user'], item['password'])
            f.write(str(cookies))
            f.write(',')


def getCookies():
    with open('cookies.txt', 'r') as f:
        for each in f.read().split(','):
            print(each+',')

storeCookies()
