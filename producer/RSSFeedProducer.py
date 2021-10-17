import json
import sys
from rssfeedurls import rss_feed_urls
from time import sleep

## install pymongo for this .  Do not install bson directly
from bson import json_util
from kafka import KafkaProducer

from RSSFeedConnector import readRSSFeedURL
from CommonUtils import getCurrentTime

rss_feed_url_txt_file = "rssfeedurls.py"
sleep_time = 3600*4
BROKER = 'kafka:9092'
TOPIC = 'newsfeeds'

## getKafkaProducer to return the Kakfa producer object
def getKafkaProducer():
    try:
        producer = KafkaProducer(bootstrap_servers=BROKER)
    except Exception as e:
        print(f"ERROR --> {e}")
        sys.exit(1)
    return producer

    ## produce message to kafka for every 4 hours
def produceRssFeeds():
    rss_feed_uls_list      = rss_feed_urls##collectRSSFeedURLs()
    kafkaProducer          = getKafkaProducer()

    while True:
        print(f"producer started after {getCurrentTime()}")
        messageCount = 1
        ## get the URLs to pull the datavol
        for category,rss_feed_url in rss_feed_uls_list.items():
            rssentries = readRSSFeedURL(category,rss_feed_url)

        ## get the entry from rss feeds
            for rssentry in rssentries:
                print(f"message sent count {messageCount}")
                bjsonData = json.dumps(rssentry.__dict__, default=json_util.default).encode('utf-8')
                print(f"bjsonData={bjsonData}")
                kafkaProducer.send(TOPIC, bjsonData)
                messageCount = messageCount + 1
        ## sleep for at least 4 hours
        sleep(sleep_time)

# Main function to start the app when main.py is called
if __name__ == "__main__":
    produceRssFeeds()




