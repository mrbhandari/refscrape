from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.item import Item
import string
from tutorial.items import DmozItem

text_file = open("starturls", "r")


class DmozSpider(CrawlSpider):
    name = "dmoz"
    #allowed_domains = ["bing.com"]
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        #Rule(SgmlLinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(SgmlLinkExtractor(deny=('subsection\.php', ))),
        Rule(SgmlLinkExtractor(allow=('\.com', )), deny=('neimanmarcus\.com', ),callback='parse_item'),
    )
    
    start_urls = text_file.read().split('\n')
    #start_urls = [
        #"http://www.facebook.com"
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    #]

    def parse_item(self, response):
        sel = Selector(response)
        #sites = sel.xpath('//ul/li')
        #items = []
        #for site in sites:
        #   item = DmozItem()
        #   item['title'] = site.xpath('a/text()').extract()
        #   item['link'] = site.xpath('a/@href').extract()
        #   item['desc'] = site.xpath('text()').extract()
        #   items.append(item)
        
        print "xxxxxxxxxxxxxxxxxxxxxxxxxx"
        #filename = url_to_filename(response.url)
        #open(filename, 'wb').write(response.body)
        item = DmozItem()

        try:
            item['url'] = response.url
        except:
            pass
        try:
            item['referrer'] = response.meta
        except:
            pass
        try:
            item['title'] = sel.xpath('//title/text()').extract()[0]
            print item['title']
        except:
            pass
        try:
            item['keyword'] = sel.xpath('//meta[@name="keyword"]/@content').extract()[0]
        except:
            pass
        try:
            item['keywords'] = sel.xpath('//meta[@name="keywords"]/@content').extract()[0]
        except:
            pass
        try:
            item['description'] = sel.xpath('//meta[@name="description"]/@content').extract()[0]
        except:
            pass
        return item


def url_to_filename(urlstring):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    return ''.join(c for c in urlstring if c in valid_chars)

