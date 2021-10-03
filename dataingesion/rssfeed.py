## This module reads  RSS (Rich site summary) from variuos NEWS articles and tries to 
## prepare a train data for Model

import feedparser

URL_INPUT_FILE_LIST = "rss_feed_urls.txt"


## This method returns all the news feeds in a particula News Feed URL
def readRSSFeedURL(urlEntry):
    newsFeed = feedparser.parse("https://timesofindia.indiatimes.com/rssfeedstopstories.cms")
    print (f'Number of RSS posts : {len(newsFeed.entries)}')
    for entry in newsFeed.entries:
        print(f'entry={entry}')
    return newsFeed.entries

## This method reads a file with the list of URLs from which RSS feeds are to be read
def readRSSSitesList(rssFeedUrlsFile):
    
    listOfURLS = []
    try:
        file1 = open(rssFeedUrlsFile, 'r')
        Lines = file1.readlines()
        count = 0
        
        # Strips the newline character
        for line in Lines:
            count += 1
            newsURLEntry = line.strip()
            listOfURLS.append(newsURLEntry)
            print("Line{}: {}".format(count, line.strip()))
    except:
        print(f" file {rssFeedUrlsFile} doesnt exist")
    finally:
        file1.close()
    return listOfURLS
    
    
rssFeedSitesList = readRSSSitesList(URL_INPUT_FILE_LIST)