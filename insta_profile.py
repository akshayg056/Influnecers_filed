from scrapy.spiders import CrawlSpider
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup
import os
import json


class Insta_profile(CrawlSpider):
    name = 'insta_profile'
    allowed_domains = ['instagram.com']
    web_url = 'https://www.instagram.com'
    start_urls = ['https://www.instagram.com/cristiano/']
    is_empty = False
    count = 0
    wait_time = 3
    timeout = '90'

    def __init__(self, *a, **kw):
        super(Insta_profile, self).__init__(*a, **kw)
        with open(os.path.join('scraped_file', self.name + '.json'), 'w') as file:
            file.write("# scraped insta profile below\n\n")

    def start_requests(self):

        yield SplashRequest(self.start_urls[0], callback=self.parse_items,
                            args={'wait': self.wait_time, 'timeout': self.timeout})

    def parse_items(self, response):
        with open(os.path.join('scraped_file', self.name + '.json'), 'a') as file:

            soup = BeautifulSoup(response.body,
                                 'html.parser')  # I have created a Beautiful soup object through which we can parse though html content

            name = soup.find('div', attrs={'class': 'nZSzR'}).find('h2').text

            post_count = soup.findAll('ul', attrs={'class': 'k9GMp'})[0].find('li').find('a').find('span').text

            followers = soup.findAll('ul', attrs={'class': 'k9GMp'})[1].find('li').find('a').find('span').text

            following = soup.findAll('ul', attrs={'class': 'k9GMp'})[2].find('li').find('a').find('span').text

            bio = soup.find('div', attrs={'class': '-vDIg'}).text

            try:
                if soup.find('div', attrs={'Title': 'Verified'}):
                    verified = True
                else:
                    verified = False
            except:
                pass

            profile_picture = soup.find('img', 'profile picture')['src']
            profile_ = {'name': name, 'post_count': post_count, 'followers': followers, 'following': following,
                        'bio': bio, 'verified': verified, 'profile_picture': profile_picture}
            data = json.dumps(profile_)
            return data




