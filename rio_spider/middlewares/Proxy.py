import logging
import json
import random
import urllib3
from rio_spider import settings
from twisted.internet import defer
from twisted.internet.error import TimeoutError, DNSLookupError, \
    ConnectionRefusedError, ConnectionDone, ConnectError, \
    ConnectionLost, TCPTimedOutError
from twisted.web.client import ResponseFailed
from scrapy.core.downloader.handlers.http11 import TunnelError

'''
    Middleware: 代理随机Proxy 
'''


class MyProxyMiddleware(object):

    # IOError is raised by the HttpCompression middleware when trying to
    # decompress an empty response
    EXCEPTIONS_TO_RETRY = (defer.TimeoutError, TimeoutError, DNSLookupError,
                           ConnectionRefusedError, ConnectionDone, ConnectError,
                           ConnectionLost, TCPTimedOutError, ResponseFailed,
                           IOError, TunnelError)

    PROXY_ILLEGAL_STATUS = [408, 522, 524, 429, 500, 502, 503, 504]

    def __init__(self):
        self.http = urllib3.PoolManager()
        self.PROXY_POOL = self._proxy_pool_get(10)

    def _proxy_pool_get(self, num):
        res = self.http.request('GET', settings.PROXY_API.format(num))
        data = json.loads(res.data.decode())['data']
        if data['today_left_count'] < 1:
            return None
        else:
            return data['proxy_list']

    def _proxy_pool_update(self, request, exception, spider):
        logging.info('********_proxy_pool_update*********')
        try:
            proxy = self._proxy_pool_get(1)[0]
            self._proxy_pool_delete(request.meta['proxy'])
            self.PROXY_POOL.append(proxy)
            request.meta['proxy'] = 'https://' + proxy
            return request
        except Exception as e:
            logging.error(e)
            spider.crawler.engine.close_spider(spider, "代理ip消耗殆尽，关闭spider")

    def _proxy_pool_delete(self, proxy):
        if proxy[2:] in self.PROXY_POOL:
            self.PROXY_POOL.remove(proxy[2:])

    def process_request(self, request, spider):
        if len(self.PROXY_POOL) == 0:
            try:
                self.PROXY_POOL.extend(self._proxy_pool_get(6))
            except Exception as e:
                logging.error(e)
                spider.crawler.engine.close_spider(spider, "代理ip消耗殆尽，关闭spider")

        request.meta['proxy'] = 'http://115.223.126.226:8010'

    def process_response(self, request, response, spider):
        """
        对此次请求的响应进行处理。
        :param request:
        :param response:
        :param spider:
        :return:
        """
        # proxy失效，需要在settings中配置。

        if response.status in self.PROXY_ILLEGAL_STATUS or response.text in settings.ERR_MSG:
            return self._proxy_pool_update(request, None, spider)

        # 如果没有出现ip失效，直接将response向下传递后续的中间件。
        return response

    def process_exception(self, request, exception, spider):
        print('^^^^^^^^^^^^^^^^^^^^', exception)

        if isinstance(exception, self.EXCEPTIONS_TO_RETRY) or \
                isinstance(exception, TimeoutError) or \
                isinstance(exception, TCPTimedOutError):
            print("处理ing")

            return self._proxy_pool_update(request, exception, spider)
