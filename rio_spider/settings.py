# -*- coding: utf-8 -*-

# Scrapy settings for rio_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import datetime
import os

DIR_PATH = os.path.abspath(os.path.dirname(__file__))

BOT_NAME = 'rio_spider'

SPIDER_MODULES = ['rio_spider.spiders']
NEWSPIDER_MODULE = 'rio_spider.spiders'

# today = datetime.datetime.now()
# LOG_ENABLED = True
# LOG_ENCODING = 'utf-8'
# LOG_LEVEL = "INFO"
# LOG_FILE = 'rio_spider/log/spider_{}-{}-{}.log'.format(today.year, today.month, today.day)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'rio_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16
# DOWNLOAD_TIMEOUT = 10
# RETRY_ENABLED = False

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'rio_spider.middlewares.RioSpiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    #    'RioSpiderDownloaderMiddleware': 543,
    'rio_spider.middlewares.UserAgent.MyUserAgentMiddleware': 100,
    'rio_spider.middlewares.Cookies.MyCookiesMiddleware': 100,
    'rio_spider.middlewares.Proxy.MyProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'rio_spider.pipelines.RepeatFilter.RepeatFilterPipeline': 100,
    # 'rio_spider.pipelines.MovieItem.MovieItemPipeline': 200,
    # 'rio_spider.pipelines.CommentItem.CommentItemPipeline': 300,
    # 'rio_spider.pipelines.ReviewItem.ReviewItemPipeline': 500,
    # 'rio_spider.pipelines.OtherItem.OtherItemPipeline': 200,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# DATABASE mysql
MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_DBNAME = 'demo'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_CHARSET = 'utf8'

ACCOUNTS = [
    {'user': '13730551689', 'password': '135792468'},
    {'user': '18730957026', 'password': '135792468'},
    # {'user': '18340018316', 'password': '135792468'},

]

COOKIES_POOL = [
    {'__utmv': '30149280.21458', '__utmt': '1', '__utma': '30149280.6605842.1586051639.1586051639.1586051639.1',
     'push_noty_num': '0', 'ap_v': '0,6.0', 'push_doumail_num': '0', '_pk_ses.100001.8cb4': '*', 'bid': '-OfT37ptx9w',
     '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1586051638%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fsource%3Dmovie%22%5D',
     'ck': 'V2yG', '__utmb': '30149280.2.10.1586051639',
     '__utmz': '30149280.1586051639.1.1.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/passport/login',
     '_pk_id.100001.8cb4': 'dd5f1f836f484867.1586051638.1.1586051638.1586051638.', '__utmc': '30149280',
     'dbcl2': '"214585653:DdrpjfRYKFE"'},
]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENTS_POOL = [
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
]

PROXY_ADDRESS = 'http://127.0.0.1:5010/'

PROXY_API = 'https://dps.kdlapi.com/api/getdps/?orderid=998605446990168&num={}&pt=1&dedup=1&format=json&sep=1'

ERR_MSG = [
    "{'msg': '检测到有异常请求从您的IP发出，请求暂时被拒绝。如果请求行为被确认为有害您的账号可能会被执行封禁', 'r': 1}",
    "{'msg': '检测到有异常请求从您的IP发出，请登录再试!', 'r': 1}",
]
