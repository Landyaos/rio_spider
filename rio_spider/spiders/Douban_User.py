# -*- coding: utf-8 -*-
import scrapy


class DoubanUserSpider(scrapy.Spider):
    name = 'Douban_User'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/']

    def parse(self, response):
        pass

    def parse_user_index_douban(self, response):

        print('-------------------------------解析 用户界面，跳转短评list界面，跳转影评list界面----------------------------')

        user = response.meta['user']
        comment_url = 'https://movie.douban.com/people/{id}/collect?start={num}&sort=time&rating=all&filter=all&mode=grid'
        review_url = 'https://movie.douban.com/people/{id}/reviews'
        #
        # yield Request(
        #     url=comment_url.format(id=user['id_douban'], num=0),
        #     meta={'user': user},
        #     callback=self.parse_user_comment_douban,
        #     headers=self.header,
        #     cookies=self.cookies,
        # )
        # 处理短评
        for page in range(5):
            yield Request(
                url=comment_url.format(id=user['id_douban'], num=page * 15),
                meta={'user': user},
                callback=self.parse_user_comment_douban,
                headers=self.header,
                cookies=self.cookies,
            )

        # 跳转影评选项 （默认短评选项）
        yield Request(
            url=review_url.format(id=user['id_douban']),
            meta={'user': user},
            callback=self.parse_user_review_index_douban,
            headers=self.header,
            cookies=self.cookies,

        )

    def parse_user_review_index_douban(self, response):

        print('-------------------------------------用户界面解析影评list界面-------------------------')
        # 解析 影评
        user = response.meta['user']
        review_num = response.xpath('//*[@id="db-usr-profile"]/div[2]/h1/text()').extract_first().split('(')[1][:-1]
        review_url = 'https://movie.douban.com/people/{id}/reviews?start={num}'

        # 处理影评

        # yield Request(
        #     url=review_url.format(id=user['id_douban'], num=0),
        #     meta={'user': user},
        #     callback=self.parse_user_review_douban,
        #     headers=self.header,
        #     cookies=self.cookies,
        # )

        for page in range(1):
            yield Request(
                url=review_url.format(id=user['id'], num=page * 10),
                meta={'user': user},
                callback=self.parse_user_review_douban,
                headers=self.header,
                cookies=self.cookies,
            )

    def parse_user_review_douban(self, response):
        # 解析 用户影评
        print("---------------------------------解析 每一条影评，跳转详细内容界面----------------------")
        user = response.meta['user']

        review_list = response.xpath('//*[class="tlst clearfix"]')
        for each in review_list:
            review_url = each.xpath('.//*[contains(@href,"review")]/@href').extract_first()
            movie_url = each.xpath('.//*[contains(@href,"subject"]/href').extract_first()
            movie_id = movie_url.split('/')[-2]

            yield Request(
                url=review_url,
                meta={'user': user, 'movie_id': movie_id, 'movie_url': movie_url},
                callback=self.parse_review_detail_douban,
                headers=self.header,
                cookies=self.cookies,
            )

    def parse_user_comment_douban(self, response):

        print('---------------------------------解析 用户短评----------------------------')
        user = response.meta['user']

        comment_list = response.xpath('//*[@class="grid-view"]/div[@class="item"]')
        for each in comment_list:
            comment_content = each.xpath('.//*[@class="comment"]/text()').extract_first()
            comment_date = each.xpath('.//*[@class="date"]/text()').extract_first()
            rate_raw = each.xpath('.//*[contains(@class,"rating")]/@class').extract_first()
            rate = int(rate_raw[6]) if rate_raw else None

            movie_url = each.xpath(
                './/*[contains(@href,"subject")]/@href').extract_first()
            movie_id = movie_url.split('/')[-2]

            item_comment = items.Comment()
            item_comment['user_id'] = user['id_douban']
            item_comment['movie_id'] = movie_id
            item_comment['content'] = comment_content
            item_comment['date'] = comment_date
            item_comment['rate'] = rate
            item_comment['votes'] = 0
            yield item_comment