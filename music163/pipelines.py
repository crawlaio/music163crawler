# -*- coding: utf-8 -*-
import os
from urllib import parse

from pymongo import MongoClient
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline


class MongoDBPipeline(object):
    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get("MONGODB_URI", "mongodb://localhost:27017"),
            mongodb_db=crawler.settings.get("MONGODB_DATABASE", "items"),
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        """
        :param item: 传入的item数据
        :param spider: spider相关信息
        :return item:
        """
        self.db[spider.name].update_one(
            filter={"comment_id": item["comment_id"], "song_id": item["song_id"]},
            update={"$setOnInsert": dict(item)},
            upsert=True,
        )
        return item


class MyFilesPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        file_url = item.get("file_url", "")
        file_url_list = str(file_url).split(";")
        for file_url in file_url_list:
            if file_url:
                yield Request(file_url, meta={"item": item})

    def file_path(self, request, response=None, info=None):
        file_name = request.meta["item"].get("file_name", "")
        path = parse.urlparse(request.url).path
        file_path = f"{os.path.basename(file_name)}-{os.path.basename(path)}"
        return file_path
