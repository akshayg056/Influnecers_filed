from scrapy.spiders import CrawlSpider
from scrapy_splash import SplashRequest
import yaml
import os
import pdb


class Insta(CrawlSpider):
    name = 'insta'
    allowed_domains = ['starngage.com']
    web_url = 'https://starngage.com'
    start_urls = ['https://starngage.com/app/global/influencer/ranking/all?page=']
    is_empty = False
    count = 0
    wait_time = 3
    timeout = '90'

    def __init__(self, *a, **kw):
        super(Insta, self).__init__(*a, **kw)
        with open(os.path.join('scraped_file', self.name + '.json'), 'w') as file:
            file.write("# scraped insta ids below\n\n")

    def start_requests(self):
        while self.is_empty is False:
            self.count = self.count + 1
            yield SplashRequest(self.start_urls[0] + str(self.count), callback=self.parse_items,
                                args={'wait': self.wait_time, 'timeout': self.timeout})

    def parse_items(self, response):
        with open(os.path.join('scraped_file', self.name + '.json'), 'a') as file:
            item = {}

            if self.count == 10:
                self.is_empty = True
            ids = response.xpath("//table[@class = 'table table-hover table-responsive-sm']/tbody/tr/td[@class = "
                                 "'align-middle text-break']/a/text()").extract()
            for i in ids:
                yaml.dump({i: 'https://instagram.com/' + i[1:]}, file)
            item['ids'] = ids
            return item




