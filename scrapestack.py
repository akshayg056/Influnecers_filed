import requests
from bs4 import BeautifulSoup
import json

def profile_data(profile_url):
    params = {
        'access_key': '0262710ed5575a8ed4306fa9acc51c30',
        'url': profile_url
    }

    api_result = requests.get('http://api.scrapestack.com/scrape', params)
    website_content = api_result.content

    soup = BeautifulSoup(website_content, 'html.parser')  # I have created a Beautiful soup object through which we can parse though html content

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

    profile_ = {'name': name, 'post_count': post_count, 'followers': followers, 'following': following, 'bio': bio, 'verified': verified, 'profile_picture': profile_picture}
    data = json.dumps(profile_)
    return data








