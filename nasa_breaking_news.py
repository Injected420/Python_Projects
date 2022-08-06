from time import time
import feedparser
from PIL import Image
import sys
from urllib.request import urlretrieve
import time


def breaking_news():
    feed = feedparser.parse('https://www.nasa.gov/rss/dyn/breaking_news.rss')
    latest = feed['entries'][1]
    news_title = latest['title']
    news_description = latest['summary']
    print("")
    print("**NASA's Daily News**")
    time.sleep(1)
    print("--------------------------\n")
    print('News Title: \n' ' %s\n\n%s\n' % (news_title, news_description))


if __name__ == '__main__':
    breaking_news()
