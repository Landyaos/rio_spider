import logging
from rio_spider import settings
from rio_spider.tools.proxy import get_proxy, delete_proxy

'''
    Middleware: 代理随机Proxy 
'''


class MyProxyMiddleware(object):

    def process_request(self, request, spider):
        request.meta['proxy'] = get_proxy().get('proxy')

    def process_response(self, request, response, spider):
        """
        对此次请求的响应进行处理。
        :param request:
        :param response:
        :param spider:
        :return:
        """
        # proxy失效，需要在settings中配置。
        if response.status != 200 or response.text in settings.ERR_MSG:
            logging.warning(request.meta['proxy'], '失效')
            delete_proxy(request.meta['proxy'])
            request.meta['proxy'] = get_proxy().get('proxy')
            return request
        # 如果没有出现ip失效，直接将response向下传递后续的中间件。
        return response
