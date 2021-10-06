
import feedparser
from dateutil import parser

class RssFeedFields:
    def __init__(self, title, published_time, summary,source,category):
        self.title = title
        self.published_time = published_time
        self.summary = summary
        self.source=source
        self.category=category

## method to get the date in expected format
def timeToYYYYMMDDHHmmss(publisedTimeObj):
    return str(publisedTimeObj.year) + str(publisedTimeObj.month) + \
    str(publisedTimeObj.day) + str(publisedTimeObj.hour) + \
    str(publisedTimeObj.minute) + str(publisedTimeObj.second)


def readRSSFeedURL(urlEntry):
    readRSSFeedURL("other", urlEntry)

## This method returns all the news feeds in a particula News Feed URL
def readRSSFeedURL(category,urlEntry):
    print(f'Number of RSS posts : Made an entry')
    newsFeed = feedparser.parse(urlEntry)
    print (f'Number of RSS posts for URL {urlEntry} : {len(newsFeed.entries)}')
    rssfeedDataEntries = []
    for entry in newsFeed.entries:
        title = entry['title']
        publishedTime =""
        try:
            if entry['published']:
                publishedTime   = entry['published']
        except:
            publishedTime = ""

        publishedTimeParsed = ""
        if publishedTime:
            publishedTimeObj = parser.parse(publishedTime)
            publishedTimeParsed  = timeToYYYYMMDDHHmmss(publishedTimeObj)
        summary =  entry['summary']
        sourcelink = entry['title_detail']['base']
        rssdataObj = RssFeedFields(title,publishedTimeParsed,summary,sourcelink,category)
        rssfeedDataEntries.append(rssdataObj)
    return rssfeedDataEntries
