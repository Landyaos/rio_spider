import requests
from rio_spider import settings


def get_proxy():
    return requests.get(settings.PROXY_ADDRESS + "get/").json()


def delete_proxy(proxy):
    requests.get(settings.PROXY_ADDRESS+"delete/?proxy={}".format(proxy))
