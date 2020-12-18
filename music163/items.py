# -*- coding: utf-8 -*-
import scrapy


class Music163MusicItem(scrapy.Item):
    song_id = scrapy.Field()
    song_name = scrapy.Field()
    singer = scrapy.Field()
    album = scrapy.Field()
    album_url = scrapy.Field()
    description = scrapy.Field()
    lyric = scrapy.Field()
    comment_id = scrapy.Field()
    user_id = scrapy.Field()
    nickname = scrapy.Field()
    content = scrapy.Field()
    time = scrapy.Field()
    liked_count = scrapy.Field()
    comment_total = scrapy.Field()
