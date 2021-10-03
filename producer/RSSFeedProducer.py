import json
import sys
from time import sleep

## install pymongo for this .  Do not install bson directly
from bson import json_util
from kafka import KafkaProducer

from RSSFeedConnector import readRSSFeedURL
from common.CommonUtils import getCurrentTime

rss_feed_url_txt_file = "rssfeedurls.txt"
sleep_time = 3600*4
BROKER = 'kafka:9092'
TOPIC = 'newsfeeds'

## read rss feed url file and generates the url list
def collectRSSFeedURLs():
    rss_feed_uls_list = []
    with open(rss_feed_url_txt_file, "r+") as file1:
        # Reading form a file
        line = file1.read()
        print("line={line}")
        rss_feed_uls_list(line)
    return rss_feed_uls_list

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
    rss_feed_uls_list = collectRSSFeedURLs()
    kafkaProducer          = getKafkaProducer()

    while True:
        print(f"producer started after {getCurrentTime()}")
        rssentries = []
        ## get the URLs to pull the data
        for rss_feed_url in rss_feed_uls_list:
            rssentries = readRSSFeedURL(rss_feed_url)
        ## get the entry from rss feeds
        for rssentry in rssentries:
            kafkaProducer.send(TOPIC, json.dumps(rssentry, default=json_util.default).encode('utf-8'))
        ## sleep for at least 4 hours
        sleep(sleep_time)




