# -*- coding: utf-8 -*-
BOT_NAME = "music163"

SPIDER_MODULES = ["music163.spiders"]
NEWSPIDER_MODULE = "music163.spiders"

MONGODB_URI = "mongodb://localhost:27017"
MONGODB_DATABASE = "music163"

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = None
REDIS_PARAMS = {
    "db": REDIS_DB,
    "password": REDIS_PASSWORD
}

# DOWNLOAD_DELAY = 1

DUPEFILTER_CLASS = "scrapy_redis_sentinel.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis_sentinel.scheduler.Scheduler"

ROBOTSTXT_OBEY = False

RETRY_ENABLED = True

DOWNLOAD_TIMEOUT = 30

LOG_LEVEL = "DEBUG"

COOKIES_ENABLED = False

DEFAULT_REQUEST_HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60",
    "content-type": "application/x-www-form-urlencoded",
    "accept": "*/*",
    "origin": "https://music.163.com",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8"
}

ITEM_PIPELINES = {
    "music163.pipelines.MongoDBPipeline": 100
}
