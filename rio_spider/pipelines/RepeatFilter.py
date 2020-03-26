import hashlib
import json
from rio_spider.settings import DIR_PATH
from scrapy.exceptions import DropItem
from rio_spider import settings, items


class RepeatFilterPipeline(object):
    def __init__(self):
        self.movie_set = set()
        self.user_set = set()
        self.genre_set = set()
        self.starring_set = set()
        self.directorScreenwriter_set = set()
        self.comment_set = set()
        self.review_set = set()

    def md5_utf8(self, str):
        m = hashlib.md5()
        m.update(str.encode("utf8"))
        return m.hexdigest()

    def close_spider(self, spider):
        with open(DIR_PATH + '/duplicate/movie_filter.txt', 'w', encoding='utf8') as f:
            f.write(json.dumps(list(self.movie_set)))
        with open(DIR_PATH + '/duplicate/user_filter.txt', 'w', encoding='utf8') as f:
            f.write(json.dumps(list(self.user_set)))
        with open(DIR_PATH + '/duplicate/genre_filter.txt', 'w', encoding='utf8') as f:
            f.write(json.dumps(list(self.genre_set)))
        with open(DIR_PATH + '/duplicate/starring_filter.txt', 'w', encoding='utf8') as f:
            f.write(json.dumps(list(self.starring_set)))
        with open(DIR_PATH + '/duplicate/directorScreenwriter_filter.txt', 'w', encoding='utf8') as f:
            f.write(json.dumps(list(self.directorScreenwriter_set)))
        with open(DIR_PATH + '/duplicate/comment_filter.txt', 'w', encoding='utf8') as f:
            f.write(json.dumps(list(self.comment_set)))
        with open(DIR_PATH + '/duplicate/review_filter.txt', 'w', encoding='utf8') as f:
            f.write(json.dumps(list(self.review_set)))

    def process_item(self, item, spider):
        if isinstance(item, items.Movie):
            key = self.md5_utf8(item['id_douban'])
            if key in self.movie_set:
                raise DropItem('Movie : %s Repeat !!!' % (item['name']))
            else:
                self.movie_set.add(key)

        elif isinstance(item, items.Comment):
            key = self.md5_utf8((item['user_id'] + item['movie_id']))
            if key in self.comment_set:
                raise DropItem('Comment : %s -> %s Repeat !!!' % (item['user_id'], item['movie_id']))
            else:
                self.comment_set.add(key)

        elif isinstance(item, items.Review):
            key = self.md5_utf8((item['user_id'] + item['movie_id']))
            if key in self.review_set:
                raise DropItem('Review : %s -> %s Repeat !!!' % (item['user_id'], item['movie_id']))
            else:
                self.review_set.add(key)
        elif isinstance(item, items.User):
            key = self.md5_utf8(item['id_douban'])
            if key in self.user_set:
                raise DropItem('User: %s !!!' % (item['id_douban']))
            else:
                self.user_set.add(key)

        elif isinstance(item, items.Starring):
            key = self.md5_utf8(item['name'])
            if key in self.starring_set:
                raise DropItem('Starring: %s !!!' % (item['name']))
            else:
                self.starring_set.add(key)

        elif isinstance(item, items.Genre):
            key = self.md5_utf8(item['name'])
            if key in self.genre_set:
                raise DropItem('Genre : %s Repeat !!!' % (item['name']))
            else:
                self.genre_set.add(key)
        return item
