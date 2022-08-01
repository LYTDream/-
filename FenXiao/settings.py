# Scrapy settings for FenXiao project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'FenXiao'

# DEBUG = False

SPIDER_MODULES = ['FenXiao.spiders']
NEWSPIDER_MODULE = 'FenXiao.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0",Win64",x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = \
#     {
#         "XIAOEID": "327a7554d27265229839312d9ee142bd",
#         "cookie_channel": "11-396651361292",
#         "sajssdk_2015_cross_new_user": "1",
#         "Hm_lvt_32573db0e6d7780af79f38632658ed95": "1659369902",
#         "Hm_lpvt_32573db0e6d7780af79f38632658ed95": "1659369902",
#         "view_url": '''https://sem.xiaoe-tech.com/?bd_vid=8413973579398792995&jzl_act=31888086&jzl_adp=6039716041&jzl_ch=11&jzl_cpg=144614223&jzl_ctv=51546062473&jzl_dv=1&jzl_kwd=308433199718&jzl_sty=19; cookie_referer=https://www.baidu.com/baidu.php?url=0s0000aPch_Smgbn9I3ntnZ4II4NZBGJrfFBh2jb9h-5F8DNfW2cXyfNYEstWkJ-tExaa6DMGX1zDglw5XnE8glm6RMTf5OisbTVrFCEHCubZNdJATf1duXiLqkZQtS0w8OBg7xxxbql5sC3xCaDuW9-kQOJxwwDaAkcycKcj846kyHqJjYnAq4LZA6IjL-air9uQWIVW5H8eOjPOanQAR4-SWbg.7R_NR2Ar5Od66WHGt89eQb4lampbfItEjw4XL68m3vUr1WkoLeOAEudztPZ-9Cxfk8oLIMHuY4r1k3qTEjw4mph2lS8g9CtonPKWWg_vUQPMHdztPZ-9klh2S1_lpS1Fb3qTEjw4yU_UZHukLSPxHuvNqTEjw4mlA9BExdztPZ-8S9BVmhr1xu8LTpOZ-3dtVHQ8gZJyAp7WIk3dq26.U1Yz0ZDqY2AvenvCkPocLUxy1Oo2YQr90ZKGm1Ys0ZK1pyI85Hmkm1bduW6smvmvPjwhnywWuWfLuyPhnWPhn1RYmvD10ZfqY2AvenvCFHcsVqU5S_of_lD0pyYqnWcd0ATqUvNsT1D0Iybqmh7GuZN_UfKspyfqnfKWpyfqn0KVIjYknjD4g1DsnHIxnW0dnNtknjmkg1csPWFxn1msnfKopHYs0ZFY5HRzn0KBpHYkPH9xnW0Yg1RsnsKVm1YknjD4g1DsnHIxnW0dnNtknjFxnW6vP1nvP1m1rjPxn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Yz0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdWUfKGuAnqiDFK0ZKCIZbq0Zw9ThI-IjYvndtsg1DdnsKYIgnqnHRsP1nsPHR3PHcsPjDLP1nsPjb0ThNkIjYkPWR4n1m4rHDdPHns0ZPGujY3n1-hmWRsmH0snH7WmWf40AP1UHYvPWRdPbnsnW9KfbfYrRm10A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg1Kxn7tsg100uA78IyF-gLK_my4GuZnqn7tsg1KxPHRkP1Dkr7tsg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KGTvP_5H00mywhUA7M5HD0UAuW5H00uAPWujY0IZF9uARqn0KBuA-b5R7jnDwAfW9DrDFDrH6Lf1N7PWRvnH-DP1RLwH7jPWFD0AqW5HD0mMfqn0KEmgwL5H00ULfqn0KETMKY5H0WnanWnansc10Wna3snj0snj0WnaPDw-fWnanVc108nj0snj0sc1D8nj0snH0s0Z91IZRqn1D3rj6srjm0TNqv5H08rjKxna3sn7tsQW0sg108rjKxna3Yn7tsg108PjKxn0KBTdqsThqbpyfqn0KzUv-hUA7M5H00mLmq0A-1gvPsmHYs0APs5H00ugPY5H00mLFW5HRsP1R&us=newvui&xst=mWdKf1KDwbc3wj9awjb3PYndwHmdPWD4wjTdPYRkf1mzw0715HbYrjfYrH61rHf3nWDsnW0Yrj-xnWcdg1DKI1LfCUU_1p66VqU5S_of_lDKTHLfCUU_1pWDv_WIVqU5S_of_lDKIHY1nH63rj03P67Y5HDvPHb1PWb4nHRKUgDqn0cs0BYKmv6quhPxTAnKUZRqn07WUWYYrH0dPHnkPdt1nNqCmyqxTATKnWb3PW0kPWn1r0&word=&ck=640.9.110.449.245.388.148.400&shh=www.baidu.com&sht=49055317_31_hao_pg&wd=&bc=110101; channel=11-308433199718; cookie_session_id=jzSFkneDmudyGgNjTJcn6X4WyetHlgaB''',
#         "bd_vid": "8413973579398792995",
#         "Qs_lvt_416447": "1659369902,1659369908,1659369926",
#         "Qs_pv_416447": "3507460361763028500,3789241017607377400,3776846203705877500",
#         "Hm_lvt_081e3681cee6a2749a63db50a17625e2": "1659369933",
#         "Hm_lpvt_081e3681cee6a2749a63db50a17625e2": "1659369933",
#         "dataUpJssdkCookie": '''{"wxver":"","net":"","sid":""}''',
#         "laravel_session": "2ooxVb5UdZDWHHXGxK4rKyus2klzR1edqDc7k8Vr",
#         "sensorsdata2015jssdkcross": '''{"distinct_id":"1825a274d42cd4-0e7e23112bf7e9-26021a51-1327104-1825a274d43c42","first_id":"","props":{"$latest_traffic_source_type":"自然搜索流量","$latest_search_keyword":"未取到值","$latest_referrer":"https://www.baidu.com/"},"$device_id":"1825a274d42cd4-0e7e23112bf7e9-26021a51-1327104-1825a274d43c42"}'''
#     }

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml",q=0.9,*/*",q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'FenXiao.middlewares.FenxiaoSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'FenXiao.middlewares.FenxiaoDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'FenXiao.pipelines.FenxiaoPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
