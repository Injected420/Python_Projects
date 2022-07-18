import feedparser
from PIL import Image
import sys
from urllib.request import urlretrieve

def main():
    feed = feedparser.parse('http://nasa.gov/rss/dyn/lg_image_of_the_day.rss')
    latest = feed['entries'][0]
    title = latest['title']
    description = latest['summary']
    print('%s\n\n%s' % (title, description))
    links = latest['links']
    image_url = None
    for link in links:
        if link.get('type').startswith('image'):
            image_url = link.get('href')
    if image_url:
        urlretrieve(image_url, 'ImageOfTheDay.jpg')
        img = Image.open('ImageOfTheDay.jpg')
        img.show()
        

if __name__ == '__main__':
    main()