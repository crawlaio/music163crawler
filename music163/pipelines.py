# -*- coding: utf-8 -*-
from pymongo import MongoClient


class MongoDBPipeline(object):
    def __init__(self, mongodb_uri, mongodb_db):
        self.mongodb_uri = mongodb_uri
        self.mongodb_db = mongodb_db
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongodb_uri=crawler.settings.get("MONGODB_URI", "mongodb://localhost:27017"),
            mongodb_db=crawler.settings.get("MONGODB_DATABASE", "music163"),
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongodb_uri)
        self.db = self.client[self.mongodb_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[spider.name].update_one(
            filter={"comment_id": item["comment_id"], "song_id": item["song_id"]},
            update={"$setOnInsert": dict(item)},
            upsert=True,
        )
        return item
