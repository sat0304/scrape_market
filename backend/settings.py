from shutil import which
from backend.utils import cookies, get_random_agent

# SELENIUM_DRIVER_NAME = 'chrome'
# SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
# # SELENIUM_DRIVER_ARGUMENTS=['-headless']  # '--headless' if using chrome instead of firefox
# SELENIUM_DRIVER_ARGUMENTS = []
# SELENIUM_BROWSER_EXECUTABLE_PATH = which('chrome')
# SELENIUM_COMMAND_EXECUTOR = 'http://localhost:4444/wd/hub'


PAGES_COUNT = 1
PRODUCT_COUNT = 1


DOWNLOAD_DELAY = 45
RANDOMIZE_DOWNLOAD_DELAY = True


BOT_NAME = "backend"

SPIDER_MODULES = ["backend.spiders"]
NEWSPIDER_MODULE = "backend.spiders"

# ROTATING_PROXY_LIST = [
#     '128.199.252.41:8000',
#     '50.174.145.12:80',
#     '128.140.26.12:80',
#     'http://brd-customer-hl_f3b35232-zone-scraping_browser1:mdsaue7gwur5@brd.superproxy.io:9222',
#     'http://brd-customer-hl_f3b35232-zone-scraping_browser1:mdsaue7gwur5@brd.superproxy.io:9515',
# ]

# Enable The Proxy Middleware In Your Downloader Middlewares
DOWNLOADER_MIDDLEWARES = {
    # 'antiblock_scrapy_selenium.SeleniumMiddleware': 800,
    'scrapy_selenium.SeleniumMiddleware': 850,
    # 'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    # 'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 400,
    # 'backend.middlewares.BackendSpiderMiddleware': 350,
}

# PROXY_USER = 'brd-customer-hl_f3b35232-zone-scraping_browser1'
# PROXY_PASSWORD = 'mdsaue7gwur5'
# PROXY_ENDPOINT = 'brd.superproxy.io'
# PROXY_PORT = '9222'


DOWNLOADER_MIDDLEWARES.update({
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': None,
    'scrapy.downloadermiddlewares.robotstxt': None,
    'scrapy_rotated_proxy.downloadmiddlewares.proxy.RotatedProxyMiddleware': 750,
})
ROTATED_PROXY_ENABLED = True
PROXY_STORAGE = 'scrapy_rotated_proxy.extensions.file_storage.FileProxyStorage'
# When set PROXY_FILE_PATH='', scrapy-rotated-proxy
# will use proxy in Spider Settings default.
PROXY_FILE_PATH = ''
HTTP_PROXIES = [
]
HTTPS_PROXIES = [
    '50.174.145.12:80',
    '119.39.68.18:2323',
    # 'https://brd-customer-hl_f3b35232-zone-scraping_browser1:mdsaue7gwur5@brd.superproxy.io:9515',
    # 'https://brd-customer-hl_f3b35232-zone-scraping_browser1:mdsaue7gwur5@brd.superproxy.io:9222',
]

CONCURRENT_REQUESTS_PER_DOMAIN = 2

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

USER_AGENT = get_random_agent()

# SELENIUM_DRIVER_CHANGE_IP_AFTER = 42
# SELENIUM_DRIVER_ALLOW_REUSE_IP_AFTER = 5
# Obey robots.txt rules
ROBOTSTXT_OBEY = True


# Cookies
# SELENIUM_DRIVER_PERSIST_COOKIES_WHEN_CLOSE = False
# SELENIUM_DRIVER_RELOAD_COOKIES_WHEN_START = False
# SELENIUM_DRIVER_COOKIE_DOMAIN = 'http://localhost:8000/'

# SELENIUM_DRIVER_LOCATION_OF_COOKIES = 'cookies-1.pkl'
# SELENIUM_DRIVER_LOAD_COOKIES = [cookie for cookie in cookies]
# SELENIUM_DRIVER_COOKIE_DOMAIN = 'http://www.ozon.ru:8000/'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "backend.middlewares.BackendSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "backend.middlewares.BackendDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "backend.pipelines.BackendPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 12
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
