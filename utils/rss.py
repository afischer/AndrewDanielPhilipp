import feedparser
import urllib, urllib2
import json
from bs4 import BeautifulSoup
import google

# uClassify API Key: 5W6oMs7Jwb4oS5rTyA3LaNk7MWY
# http://uclassify.com/browse/uClassify/Topics/ClassifyUrl?readkey=5W6oMs7Jwb4oS5rTyA3LaNk7MWY&url=apple.com&version=1.01

#http://www.rssmicro.com/?q=the+verge&f=3&v=0&sd=-1&sit=t&p=1&pi=15&s=d&rst=1&lang=0

### RSS Finding Tools
def findFeeds(query):
    #URL = "http://www.rssmicro.com/?q="+query+"&f=3&v=0&sd=-1&sit=t&p=1&pi=15&s=d&rst=1&lang=0"
    #So I'm doing a bad thing here. rssmicro has an API but it's not free. So I'm web scraping.
    #Sorry! If this becomes a real thing we will pay you <3

    # URL = "https://www.google.com/?gws_rd=ssl#q=filetype:xml+RSS+" + query
    # URL = URL.replace (" ", "+")
    # print URL
    # request = urllib2.urlopen(URL)
    # result = request.read()

    #SCREW THIS STUFF PODFUPOSFUOPSDFIUPOSDFIUPSODIF

    query = 'filetype:xml RSS' + query #This is super ratchet but we'll talk.

    result = [x for x in google.search(query, start=0, stop=10)] #That sexy list comprehension

    # for link in result:
    #     print link

    return result


### RSS Parsing Tools
testFeedURL = 'http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
testFeed    = feedparser.parse(testFeedURL)


def getTitle(parsedFeed):
    return parsedFeed['feed']['title']


print getTitle(testFeed)
print findFeeds("the verge")
