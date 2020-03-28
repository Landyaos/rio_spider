import random

from rio_spider import settings
import logging


class MyCookiesMiddleware(object):

    def __init__(self):
        self.cookiesPool = settings.COOKIES_POOL

    def process_request(self, request, spider):
        """
        request 更换随机cookie
        :param request:
        :param spider:
        :return:
        """
        request.cookies = random.choice(self.cookiesPool)

    def process_response(self, request, response, spider):
        """
        对此次请求的响应进行处理。
        :param request:
        :param response:
        :param spider:
        :return:
        """
        # 携带cookie进行页面请求时，可能会出现cookies失效的情况。访问失败会出现两种情况：1. 重定向302到登录页面；2. 也能会出现验证的情况；

        # 想拦截重定向请求，需要在settings中配置。
        if response.status in [302, 301]:
            # 如果出现了重定向，获取重定向的地址
            redirect_url = response.headers['location']
            if 'passport' in redirect_url:
                # 重定向到了登录页面，Cookie失效。
                print('Cookies Invaild!')
            if '验证页面' in redirect_url:
                # Cookies还能继续使用，针对账号进行的反爬虫。
                print('当前Cookie无法使用，需要认证。')

            # 如果出现重定向，说明此次请求失败，继续获取一个新的Cookie，重新对此次请求request进行访问。
            request.cookies = random.choice(self.cookiesPool)
            # 返回值request: 停止后续的response中间件，而是将request重新放入调度器的队列中重新请求。
            return request
        elif response.status == 200 and response.text in settings.ERR_MSG:
            logging.warning(response.text)
            request.cookies = random.choice(self.cookiesPool)
            return request

        # 如果没有出现重定向，直接将response向下传递后续的中间件。
        return response
