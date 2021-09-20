# Influencers_filed

This repo contains the sourec code for assignment given by Filed Related to Scraping 

1. Insta.py contains spider based on Scrapy in python for generating list of top 1000 influencers.

2. Insta.json contains scraped list of instagram ids with public urls from insta.py

Now, the next step is to scrape instagram for each of these ids and store data. Instagram is having very strong algorithm with detects bots trying to scrape it. 
there are still some ways through which we can scrape it. 

1. We can use third party APIs for scraping Instagram like ScrapeStack API which can scrape Insta using its Residential IPs and Vast geolocation rotations.
   I have Implemented this API as well to show, how we can use it in our case. This code is included in scrapestack.py. Note: We need to subscribe to thier premium
   plan for using above mentioned features.
   
2. The second way of scraping Instagram through python code. I have implemented this using Scrapy in python with Splash docker(JavaScript rendering service) through
   which I am able to scrape Instagram. The issue with this method is that Instagram can detect our IP easily and then can block it permanently. Instagram also blocked me 
   during this development. The solution we can have is, we should use multiple proxy IPs with rotation. This code is included in insta_profile.py
   
The other task was to scrape data of user from other handles as well. Since, we have implemented this method for instagram, we can do that in similar way.    
