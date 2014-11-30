import feedparser
import urllib, urllib2
from urlparse import urlparse
import json
from bs4 import BeautifulSoup
import google

# uClassify API Key: 5W6oMs7Jwb4oS5rTyA3LaNk7MWY
# http://uclassify.com/browse/uClassify/Topics/ClassifyUrl?readkey=5W6oMs7Jwb4oS5rTyA3LaNk7MWY&url=apple.com&version=1.01


### RSS Finding Tools
def findFeeds(query):
    query = 'filetype:xml RSS' + query #This is super ratchet but we'll talk.
    result = [x for x in google.search(query, start=0, stop=10)] #That sexy list comprehension
    return result


### RSS Parsing Tools
def parseFeed(feed):
    return feedparser.parse(feed)

def getTitle(parsedFeed):
    return parsedFeed['feed']['title']

def getCategory(feed):
    URL = urlparse(feed)
    hostname = URL.hostname[4:]

    uClassify = "http://uclassify.com/browse/uClassify/Topics/ClassifyUrl?readkey=5W6oMs7Jwb4oS5rTyA3LaNk7MWY&output=json&url="+hostname+"&version=1.01"
    request = urllib2.urlopen(uClassify)
    result = request.read()
    data = json.loads(result)
    rlist = data['cls1']
    #print rlist #Categories and their percentage matches
    inverse = [(value, key) for key, value in rlist.items()]
    category = max(inverse)[1]
    print "CATEGORY: " + category
    return category


#print getTitle(parseFeed('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'))
#print findFeeds("Apple")
#print getCategory("https://www.apple.com/main/rss/hotnews/hotnews.rss") #should return computers


for item in findFeeds("Forbes"):
    print getTitle(parseFeed(item))
