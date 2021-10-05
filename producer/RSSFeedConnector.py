
import feedparser
## This method returns all the news feeds in a particula News Feed URL
def readRSSFeedURL(urlEntry):
    print(f'Number of RSS posts : Made an entry')
    newsFeed = feedparser.parse(urlEntry)
    print (f'Number of RSS posts : {len(newsFeed.entries)}')
    for entry in newsFeed.entries:
        print(f'entry={entry}')
    return newsFeed.entries