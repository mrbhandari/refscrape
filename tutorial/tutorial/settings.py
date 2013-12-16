# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'
EXTENSIONS = {'scrapy.contrib.logstats.LogStats': 1}
LOGSTATS_INTERVAL = 60.0
RETRY_TIMES = 4
CONCURRENT_REQUESTS = 320
CONCURRENT_REQUESTS_PER_DOMAIN = 120
CONCURRENT_ITEMS = 2000
DOWNLOAD_DELAY = 0.75
#DOWNLOADER_MIDDLEWARES = {
#        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware' : None,
#        'Tutorial.rotate_useragent.RotateUserAgentMiddleware' :400
#    }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
