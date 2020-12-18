# -*- coding: utf-8 -*-
from redis import StrictRedis

from music163.settings import REDIS_DB, REDIS_HOST, REDIS_PASSWORD, REDIS_PORT


class URLBuilder:
    def __init__(self):
        self.redis = StrictRedis(
            host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, db=REDIS_DB, decode_responses=True
        )

    def generate_url(self):
        song_id_list = range(59867, 59868)
        url_list = [f"https://music.163.com/song?id={song_id}" for song_id in song_id_list]
        self.redis.rpush(f"music163_music:start_urls", *url_list)


if __name__ == "__main__":
    URLBuilder().generate_url()
