from click import option
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
## install pip3 install pyspark-stubs==2.3.0
from pyspark.streaming.kafka import KafkaUtils


sc = SparkContext(appName="RssConsumer")
ssc = StreamingContext(sc, 5)
ss = SparkSession.builder.appName("Something").getOrCreate()

ss.sparkContext.setLogLevel('WARN')

# ks = KafkaUtils.createDirectStream(ssc, ['newsfeeds'], {'metadata.broker.list': 'kafka:9092'})

df = ss.readStream\
    .format("kafka").option("kafka.bootstrap.servers", "kafka:9092")\
    .option("subscribe", "newsfeeds")\
    .option("startingOffsets", "earliest").load()

df.printSchema()
df.show()


