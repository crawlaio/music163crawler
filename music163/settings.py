# -*- coding: utf-8 -*-

# Scrapy settings for music163 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# ------------------------------项目配置----------------------------------------

BOT_NAME = 'music163'

SPIDER_MODULES = ['music163.spiders']
NEWSPIDER_MODULE = 'music163.spiders'
# -----------------------------参数配置----------------------------------------

# MongoDB 配置
MONGODB_URI = "mongodb://localhost:27017"
MONGODB_DATABASE = "music163"

# # -----------------------------Redis 单机模式----------------------------------------
# Redis 单机地址
REDIS_HOST = "localhost"
REDIS_PORT = 7002

# REDIS 单机模式配置参数
REDIS_PARAMS = {
    "db": 0
}

# -----------------------------Redis 哨兵模式----------------------------------------
# Redis 哨兵地址
REDIS_SENTINELS = [
    ('localhost', 5000),
    ('localhost', 5001),
    ('localhost', 5002)
]

# REDIS_SENTINEL_PARAMS 哨兵模式配置参数。
REDIS_SENTINEL_PARAMS = {
    "service_name": "mymaster",
    "db": 0
}

# -----------------------------Redis 集群模式 - ---------------------------------------

# Redis 集群地址
REDIS_MASTER_NODES = [
    {"host": "localhost", "port": "7000"},
    {"host": "localhost", "port": "7001"},
    {"host": "localhost", "port": "7002"},
    {"host": "localhost", "port": "7003"},
    {"host": "localhost", "port": "7004"},
    {"host": "localhost", "port": "7005"},
]

# REDIS_CLUSTER_PARAMS 集群模式配置参数
REDIS_CLUSTER_PARAMS = {}

# -----------------------------------全局并发数的一些配置-----------------------------------

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 1、下载器总共最大处理的并发请求数,默认值 16
# CONCURRENT_REQUESTS = 32  # 并发数量

# 默认 Item 并发数：100
# CONCURRENT_ITEMS = 100

# The download delay setting will honor only one of:
# 默认每个域名的并发数：8
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 每个IP的最大并发数：0 表示忽略
# CONCURRENT_REQUESTS_PER_IP = 0

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 如果没有开启智能限速，这个值就代表一个规定死的值，代表对同一网址延迟请求的秒数
# 最小延迟
# DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
# 每个域名能够被执行的最大并发请求数目，默认值 8
# CONCURRENT_REQUESTS_PER_DOMAIN = 16

# 能够被单个 IP 处理的并发请求数，默认值 0，代表无限制，需要注意两点
# I、如果不为零，那 CONCURRENT_REQUESTS_PER_DOMAIN 将被忽略，即并发数的限制是按照每个 IP 来计算，而不是每个域名
# II、该设置也影响 DOWNLOAD_DELAY，如果该值不为零，那么 DOWNLOAD_DELAY 下载延迟是限制每个 IP 而不是每个域
# CONCURRENT_REQUESTS_PER_IP = 16


# --------------------------scrapy-redis配置----------------------------------------

# 调度器队列
# 访问 URL 去重
# 确保所有的爬虫通过 Redis 去重，使用 scrapy-redis-sentinel 的去重组件,不再使用 scrapy 的去重组件
DUPEFILTER_CLASS = "scrapy_redis_sentinel.dupefilter.RFPDupeFilter"
# 启用Redis调度存储请求队列，使用Scrapy-Redis的调度器,不再使用scrapy的调度器
SCHEDULER = "scrapy_redis_sentinel.scheduler.Scheduler"

# 爬取深度与爬取方式
# 爬虫允许的最大深度，可以通过meta查看当前深度；0表示无深度
# DEPTH_LIMIT = 3

# 爬取时，0表示深度优先Lifo(默认)；1表示广度优先FiFo

# 后进先出，深度优先
# DEPTH_PRIORITY = 0
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleLifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.LifoMemoryQueue'
# 先进先出，广度优先

# DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeue.PickleFifoDiskQueue'
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeue.FifoMemoryQueue'

# 指定排序爬取地址时使用的队列，
# 默认的 按优先级排序(Scrapy默认)，由 sorted set 实现的一种非 FIFO、LIFO 方式。
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis_sentinel.queue.SpiderPriorityQueue'
# 可选的 按先进先出排序（FIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis_sentinel.queue.SpiderStack'
# 可选的 按后进先出排序（LIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis_sentinel.queue.SpiderStack'
# 在 redis 中保持 scrapy-redis 用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理 redis queues
# SCHEDULER_PERSIST = True
# 只在使用 SpiderQueue 或者 SpiderStack 是有效的参数，指定爬虫关闭的最大间隔时间
# SCHEDULER_IDLE_BEFORE_CLOSE = 10

# -----------------------------robots协议、请求配置---------------------------------------------
# 是否遵循爬虫协议
# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 不遵守网络爬虫规则 :)

# 客户端 User-Agent 请求头
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 它定义了在抓取网站所使用的用户代理，默认值：“Scrapy / VERSION“
# USER_AGENT = 'music163 (+http://www.yourdomain.com)'

# 对于失败的 HTTP 请求(如超时)进行重试会降低爬取效率，当爬取目标基数很大时，舍弃部分数据不影响大局，提高效率
RETRY_ENABLED = True

DOWNLOAD_TIMEOUT = 260  # 请求超时时间

# --------------------------------日志文件配置-----------------------------------
# 默认: True,是否启用 logging。
# LOG_ENABLED = True
# 默认: 'utf-8',logging使用的编码。
# LOG_ENCODING = 'utf-8'
# 它是利用它的日志信息可以被格式化的字符串。默认值：'%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'
# 它是利用它的日期/时间可以格式化字符串。默认值： '%Y-%m-%d %H:%M:%S'
# LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'
# 日志文件名
# LOG_FILE = "dg.log"
# 日志文件级别,默认值：“DEBUG”,log的最低级别。可选的级别有: CRITICAL、 ERROR、WARNING、INFO、DEBUG 。
LOG_LEVEL = "DEBUG"  # 日志等级  注意: 调试时可以将此句注释或改为 'DEBUG'；运行为‘INFO’

# ----------------------redis的地址配置-------------------------------------
# 指定 redis 数据库的连接参数
# Specify the full Redis URL for connecting (optional).
# If set, this takes precedence over the REDIS_HOST and REDIS_PORT settings.
# 指定用于连接 redis 的 URL（可选）
# 如果设置此项，则此项优先级高于设置的 REDIS_HOST 和 REDIS_PORT
# REDIS_URL = 'redis://root:密码@主机ＩＰ:端口'
# REDIS_URL = 'redis://root:123456@127.0.0.1:6379'
# REDIS_URL = 'redis://root:%s@%s:%s' % (password_redis, host_redis, port_redis)
# 自定义的 redis 参数（连接超时之类的）
# REDIS_PARAMS = {'db': db_redis}
# Specify the host and port to use when connecting to Redis (optional).
# 指定连接到 redis 时使用的端口和地址（可选）

# ----------------------redis的存储相关配置-------------------------------------

# 序列化项目管道作为 redis Key 存储
# REDIS_ITEMS_KEY = '%(spider)s:items'

# 默认使用 ScrapyJSONEncoder 进行项目序列化
# You can use any importable path to a callable object.
# REDIS_ITEMS_SERIALIZER = 'json.dumps'

# 自定义 redis 客户端类
# REDIS_PARAMS['redis_cls'] = 'music163.RedisClient'

# 如果为 True，则使用 redis 的 'spop' 进行操作。
# 如果需要避免起始网址列表出现重复，这个选项非常有用。开启此选项urls必须通过sadd添加，否则会出现类型错误。
# REDIS_START_URLS_AS_SET = False

# RedisSpider 和 RedisCrawlSpider 默认 start_usls 键
# REDIS_START_URLS_KEY = '%(name)s:start_urls'

# 设置 redis 使用 utf-8 之外的编码
# REDIS_ENCODING = 'latin1'

# ---------------------------------------下载参数配置-------------------------------

# 这是响应的下载器下载的最大尺寸，默认值：1073741824 (1024MB)
# DOWNLOAD_MAXSIZE=1073741824
# 它定义为响应下载警告的大小，默认值：33554432 (32MB)
# DOWNLOAD_WARNSIZE = 33554432


# ---------------------------------------其它请求配置-----------------------------------

# 是否支持 cookie，cookiejar 进行操作 cookie，默认开启,禁用 cookies,有些站点会从 cookies 中判断是否为爬虫
# Disable cookies (enabled by default)
COOKIES_ENABLED = False
# COOKIES_DEBUG = True

# 禁止重定向
# 除非您对跟进重定向感兴趣，否则请考虑关闭重定向。 当进行通用爬取时，一般的做法是保存重定向的地址，并在之后的爬取进行解析。
# 这保证了每批爬取的 request 数目在一定的数量， 否则重定向循环可能会导致爬虫在某个站点耗费过多资源。
# REDIRECT_ENABLED = False

# 忽略状态
# HTTPERROR_ALLOWED_CODES = [404]

# FEED_EXPORT_ENCODING = "utf-8"

# Telnet 用于查看当前爬虫的信息，操作爬虫等...使用 telnet ip port ，然后通过命令操作
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_HOST = '127.0.0.1'
# TELNETCONSOLE_PORT = [6023,]

# Scrapy 发送 HTTP 请求默认使用的请求头
# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }


# ---------------------------------------中间件配置-----------------------------------

# 启用或禁用 downloader 中间件
# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'music163.middlewares.Music163DownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'music163.middlewares.Music163SpiderMiddleware': 543,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 配置项目管道
ITEM_PIPELINES = {
    "music163.pipelines.MyFilesPipeline": None,
    "music163.pipelines.MongoDBPipeline": 300,
}

# FILES_STORE = 'file'  # 文件存储路径

# ---------------------------------------限速算法（延迟）配置-----------------------------------

# 自动限速算法基于以下规则调整下载延迟
# spiders 开始时的下载延迟是基于 AUTOTHROTTLE_START_DELAY 的值
# 当收到一个 response，对目标站点的下载延迟=收到响应的延迟时间/ AUTOTHROTTLE_TARGET_CONCURRENCY
# 下一次请求的下载延迟就被设置成：对目标站点下载延迟时间和过去的下载延迟时间的平均值
# 没有达到200个 response 则不允许降低延迟
# 下载延迟不能变的比 DOWNLOAD_DELAY 更低或者比 AUTOTHROTTLE_MAX_DELAY 更高
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html

# Disable Telnet Console (enabled by default)
# 它定义是否启用 telnetconsole,默认值：True
# TELNETCONSOLE_ENABLED = False

# 启用并配置自动节流阀扩展(默认禁用)　防止请求过快，将服务器抓崩。
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 起始的延迟
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 最大延迟
# AUTOTHROTTLE_MAX_DELAY = 60

# The average number of requests Scrapy should be sending in parallel to
# each remote server
# 每秒并发请求数的平均值，不能高于 CONCURRENT_REQUESTS_PER_DOMAIN或CONCURRENT_REQUESTS_PER_IP，调高了则吞吐量增大强奸目标站点，调低了则对目标站点更加”礼貌“
# 每个特定的时间点，scrapy 并发请求的数目都可能高于或低于该值，这是爬虫视图达到的建议值而不是硬限制
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 调试
# AUTOTHROTTLE_DEBUG = False

# ---------------------------------------缓存配置-----------------------------------

# Enable and configure HTTP caching (disabled by default)
# 启用和配置 HTTP 缓存（默认禁用）
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 是否启用缓存策略
# HTTPCACHE_ENABLED = True

# 缓存策略：所有请求均缓存，下次在请求直接访问原来的缓存即可
# HTTPCACHE_POLICY = "scrapy.extensions.httpcache.DummyPolicy"

# 缓存策略：根据 Http 响应头：Cache-Control、Last-Modified 等进行缓存的策略
# HTTPCACHE_POLICY = "scrapy.extensions.httpcache.RFC2616Policy"

# 缓存超时时间
# HTTPCACHE_EXPIRATION_SECS = 0

# 缓存保存路径
# HTTPCACHE_DIR = 'httpcache'

# 缓存忽略的 Http 状态码
# HTTPCACHE_IGNORE_HTTP_CODES = []

# 缓存存储的插件
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# -----------------------------------------其它相关配置-------------------------------------------------------

# 它定义了将被允许抓取的网址的长度为URL的最大极限，默认值：2083
# URLLENGTH_LIMIT = 2083
# 爬取网站最大允许的深度(depth)值,默认值0。如果为 0，则没有限制
# DEPTH_LIMIT = 3
# 整数值。用于根据深度调整 request 优先级。如果为 0，则不根据深度进行优先级调整。
# DEPTH_PRIORITY = 3

# 最大空闲时间防止分布式爬虫因为等待而关闭
# 这只有当上面设置的队列类是 SpiderQueue 或 SpiderStack 时才有效
# 并且当您的蜘蛛首次启动时，也可能会阻止同一时间启动（由于队列为空）
# SCHEDULER_IDLE_BEFORE_CLOSE = 10
