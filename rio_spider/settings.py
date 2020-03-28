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

today = datetime.datetime.now()
# LOG_ENABLED = True
# LOG_ENCODING = 'utf-8'
# LOG_LEVEL = "INFO"
# LOG_FILE = 'log/spider_{}-{}-{}.log'.format(today.year, today.month, today.day)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'rio_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

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
    'rio_spider.middlewares.UserAgent.MyUserAgentMiddleware': 200,
    'rio_spider.middlewares.Cookies.MyCookiesMiddleware': 200,
    'rio_spider.middlewares.Proxy.MyProxyMiddleware': 200,

}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'rio_spider.pipelines.RepeatFilter.RepeatFilterPipeline': 100,
    'rio_spider.pipelines.MovieItem.MovieItemPipeline': 300,
    'rio_spider.pipelines.CommentItem.CommentItemPipeline': 300,
    'rio_spider.pipelines.ReviewItem.ReviewItemPipeline': 300,
    'rio_spider.pipelines.OtherItem.OtherItemPipeline': 300,
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
    # {'user': '18340018316', 'password': 'doubanspider'},
    # {'user': '13653399918', 'password': ''},
    # {'user': '18340018118', 'password': '1997XIAO'},
    # {'user': '13785902686', 'password': 'shijunyu'},
    # {'user': '17731939681', 'password': 'shijunyu'},
    # {'user': '18034556894', 'password': '123456789a'},
    # {'user': '17731939290', 'password': ''},
]

COOKIES_POOL = [
            {'push_noty_num': '0',
             'ap_v': '0,6.0',
             'push_doumail_num': '0',
             '__gads': 'ID=0dfdda91b09308a6:T=1585188907:S=ALNI_MZXeohVTVFQSSE9pRp9nFonGhVepg',
             '_pk_ses.100001.8cb4': '*',
             '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1585188907%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fsource%3Dmovie%22%5D',
             'ck': 'CZIX',
             '_pk_id.100001.8cb4': '4edf5f3a53f04c93.1585188907.1.1585188907.1585188907.',
             'dbcl2': '"208735309:XhvRwIpk2ik"',
             'bid': 'bYySfe7bvg4'},
            {'push_noty_num': '0',
             'ap_v': '0,6.0',
             'push_doumail_num': '0',
             '__yadk_uid': 'x7pHqxQkPmqroZSoqMtZa6fCROhP4TDd',
             '__gads': 'ID=38edaff0aacabc36:T=1585188916:S=ALNI_MaegKxqfja84peu9gjw1FQ7GKEsZQ',
             '_pk_ses.100001.8cb4': '*',
             '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1585188916%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fsource%3Dmovie%22%5D',
             'ck': 'ltbw',
             '_pk_id.100001.8cb4': 'fa5eaf0073e94a0d.1585188916.1.1585188916.1585188916.',
             'dbcl2': '"188523178:PdMhu8KbRxc"',
             'bid': 'zF4XlNXEYCk'},
            {'push_noty_num': '0',
             'push_doumail_num': '0',
             '__gads': 'ID=45cf638b12e1ef6f:T=1585189171:S=ALNI_MZJF7xPDJpHmFUThBTR8ipNWfQdkA',
             '_pk_ses.100001.8cb4': '*',
             'ap_v': '0,6.0',
             '_pk_id.100001.8cb4': '719e1d5351d0b0f5.1585189171.1.1585189171.1585189171.',
             '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1585189171%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fsource%3Dmovie%22%5D',
             'ck': 'ZfNf',
             'dbcl2': '"209146781:hi/wG/bD+Aw"',
             'bid': '-sdm4-BB3mY'},
            {'push_noty_num': '0',
             'ap_v': '0,6.0',
             'push_doumail_num': '0',
             '__gads': 'ID=190a13eec18e76a4:T=1585189755:S=ALNI_MZgdxqsDBRjurtcazeDeBLULjr-vA',
             '_pk_ses.100001.8cb4': '*',
             '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1585189755%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fsource%3Dmovie%22%5D',
             'ck': 'dPel',
             '_pk_id.100001.8cb4': '209311d9c7499737.1585189755.1.1585189755.1585189755.',
             'dbcl2': '"212636496:id9Ohv1Un5U"',
             'bid': 'IJSGaJIu83c'},
            {'push_noty_num': '0',
             'push_doumail_num': '0',
             '__gads': 'ID=96f14eeb7158d56a:T=1585189766:S=ALNI_Mb9_Ai6owYG_M4G3kWoqzUCbJg2nA',
             '_pk_ses.100001.8cb4': '*',
             'ap_v': '0,6.0',
             '_pk_id.100001.8cb4': '1e0756a31017d477.1585189766.1.1585189766.1585189766.',
             '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1585189766%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fsource%3Dmovie%22%5D',
             'ck': 'qX49',
             'dbcl2': '"212636713:UL1rkcUh2+w"',
             'bid': 'JqkZ_g_VUr0'},
            {'push_noty_num': '0',
             'ap_v': '0,6.0',
             'push_doumail_num': '0',
             '__yadk_uid': 'GJBkB1iZPJATf8XX2CKBj54Km0CVQz8q',
             '__gads': 'ID=14a02686b4e9dc38:T=1585189775:S=ALNI_MbaG_yBmzNYOP3nFvDcnwSb3f90LQ',
             '_pk_ses.100001.8cb4': '*',
             '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1585189775%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fsource%3Dmovie%22%5D',
             'ck': 'eFjf',
             '_pk_id.100001.8cb4': '4037bea330b16093.1585189775.1.1585189775.1585189775.',
             'dbcl2': '"212636852:jE+FrsUjoCw"',
             'bid': 'qOL4ksS4JY4'},
            {'push_noty_num': '0',
             'ap_v': '0,6.0',
             'push_doumail_num': '0',
             '__gads': 'ID=89de4b62c01120e1:T=1585189795:S=ALNI_MbKEQ8IwI0_7kia6b6V34zVYAnRIg',
             '_pk_ses.100001.8cb4': '*',
             '_pk_ref.100001.8cb4': '%5B%22%22%2C%22%22%2C1585189795%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%3Fsource%3Dmovie%22%5D',
             'ck': 'hIP8',
             '_pk_id.100001.8cb4': 'd22f8951589cd153.1585189795.1.1585189795.1585189795.',
             'dbcl2': '"214334353:l7Uh/GpWwMg"',
             'bid': 'qt7NG2ILR84'}
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

ERR_MSG = [
    "{'msg': '检测到有异常请求从您的IP发出，请求暂时被拒绝。如果请求行为被确认为有害您的账号可能会被执行封禁', 'r': 1}",
    "{'msg': '检测到有异常请求从您的IP发出，请登录再试!', 'r': 1}",
]
