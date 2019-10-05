# -*- coding: utf-8 -*-
import json
import math
from urllib import parse

from scrapy import Request, FormRequest
from scrapy_redis_sentinel.spiders import RedisSpider

from music163.items import Music163MusicItem
from music163.util import encrypt_data


class Music163MusicSpider(RedisSpider):
    name = "music163_music"
    redis_key = "start_urls:{0}".format(name)

    def parse(self, response):
        items = Music163MusicItem()
        if response.xpath("//div[@class='n-for404']"):
            return False
        items["song_id"] = str(response.url).split("=")[-1]
        items["song_name"] = response.xpath("//em[@class='f-ff2']/text()").extract_first()
        items["singer"] = response.xpath('//p[@class="des s-fc4"]/span/@title').extract_first()
        items["album"] = response.xpath('//p[@class="des s-fc4"]/a/text()').extract_first()
        items["album_url"] = parse.urljoin(
            response.url, response.xpath('//p[@class="des s-fc4"]/a/@href').extract_first()
        )
        try:
            song_info = response.xpath('//script[@type="application/ld+json"]/text()').extract_first()
            song_info = json.loads(song_info)
        except Exception as e:
            song_info = {}
        items["description"] = song_info.get("description")
        yield Request(
            url="http://music.163.com/api/song/lyric?os=pc&id={0}&lv=-1&kv=-1&tv=-1".format(items["song_id"]),
            dont_filter=True,
            callback=self.parse_lyrics,
            meta={"meta": items}
        )

    def parse_lyrics(self, response):
        items = response.meta.get("meta")
        items["lyric"] = json.loads(response.body_as_unicode()).get("lrc", {}).get("lyric", "")
        page = 1
        formdata = encrypt_data(song_id=items["song_id"], page=page)
        yield FormRequest(
            url="https://music.163.com/weapi/v1/resource/comments/R_SO_4_{0}?csrf_token=".format(items["song_id"]),
            method="POST",
            formdata=formdata,
            callback=self.parse_comments,
            meta={"meta": items, "page": page}
        )

    def parse_comments(self, response):
        items = response.meta.get("meta")
        page = response.meta.get("page")
        comments_json = json.loads(response.body_as_unicode())
        total = comments_json.get("total", 0)
        items["comment_total"] = total
        max_page = math.ceil(total / 20)
        if page == 1:
            hot_comments = comments_json.get("hotComments", [])
        else:
            hot_comments = []
        comments = comments_json.get("comments", []) + hot_comments
        for comment in comments:
            items["comment_id"] = comment.get("commentId")
            if items["comment_id"]:
                user = comment.get("user", {})
                items["user_id"] = user.get("userId", "")
                items["nickname"] = user.get("nickname", "")
                items["content"] = comment.get("content", None)
                items["time"] = comment.get("time", None)
                items["liked_count"] = comment.get("likedCount", None)
                yield items
        if page <= max_page:
            page += 1
            formdata = encrypt_data(song_id=items["song_id"], page=page)
            yield FormRequest(
                url="https://music.163.com/weapi/v1/resource/comments/R_SO_4_{0}?csrf_token=".format(items["song_id"]),
                method="POST",
                formdata=formdata,
                callback=self.parse_comments,
                meta={"meta": items, "page": page},
            )
