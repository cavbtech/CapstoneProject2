## This program is to read the data and clense the date
from pyspark.sql import SparkSession
from pyspark.sql import Window
from pyspark.sql.functions import  col, row_number,regexp_replace,substring,locate

quotes_match_expression = """/["'][\w\s]+["']|\w+["']\w+/"""
image_tag_starting      ="<img"

spark           = SparkSession.builder().master("local[1]")\
                                .appName("SparkByExamples.com")\
                                .getOrCreate()
## This would have the fields {id, title,published_time,summary,source,category}
df              = spark.read.csv("/datavol/raw/newsfeeds/*.csv",header=True)

firstRowWindow  = Window.partitionBy(col("id")).orderBy(col("published_time").desc)
deduped_df      = df.withColumn("rn", row_number.over(firstRowWindow))\
                    .where(col("rn") == 1).drop(col("rn"))
## Clean the data
refined_df      = deduped_df.withColumn("title1",regexp_replace(col("title",quotes_match_expression,"")))\
                            .withColumn("summary1",regexp_replace(col("summary",quotes_match_expression,"")))\
                            .withColumn("bare_summary",substring("summary1",1,locate("summary1",image_tag_starting)))\
                            .drop(col("title"),col("summary"),col("summary1"))\
                            .select(col("id"),
                                    col("published_time"),
                                    col("title1").alias("title"),
                                    col("bare_summary").alias("summary"),
                                    col("source"),
                                    col("category"))

deduped_df.write
##So just a single part- file will be created
deduped_df.coalesce(1) \
.write.mode("overwrite") \
.option("mapreduce.fileoutputcommitter.marksuccessfuljobs","false") \
.option("header","true") \
.csv("file:///datavol/cleansed/")