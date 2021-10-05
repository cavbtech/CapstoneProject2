from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.streaming import StreamingContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StringType
from pyspark.sql.functions import col,from_json
## install pip3 install pyspark-stubs==2.3.0
# from pyspark.streaming.kafka import KafkaUtils


sc = SparkContext(appName="RssConsumer")
ssc = StreamingContext(sc, 5)
ss = SparkSession.builder.master("local[1]").appName("Something").getOrCreate()

ss.sparkContext.setLogLevel('WARN')

# ks = KafkaUtils.createDirectStream(ssc, ['newsfeeds'], {'metadata.broker.list': 'kafka:9092'})

df = ss.readStream\
    .format("kafka").option("kafka.bootstrap.servers", "kafka:9092")\
    .option("subscribe", "newsfeeds")\
    .option("startingOffsets", "earliest").load()

df.printSchema()

schema = StructType().add("b", StringType())
# df.select( \
#   col("key").cast("string"),
#   from_json(col("value").cast("string"), schema))
datadf = df.select(from_json(col("value").cast("string"), schema))

query = datadf.writeStream \
  .outputMode("append") \
  .format("console") \
  .start()

query.awaitTermination()





# ks = KafkaUtils.createDirectStream(ssc, ['newsfeeds'], {'metadata.broker.list': 'localhost:9092'})
# lines = ks.map(lambda x: x[1])

