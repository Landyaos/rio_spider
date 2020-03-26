import random

from rio_spider import settings


class MyUserAgentMiddleware(object):

    def __init__(self):
        self.userAgentsPool = settings.USER_AGENTS_POOL

    def process_request(self, request, spider):

        agent = random.choice(self.userAgentsPool)
        request.headers['User-Agent'] = agent
