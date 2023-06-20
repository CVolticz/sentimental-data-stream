"""
    Instantiate a SparkSession to process incoming data from the opened port
"""
# system level import
from datetime import datetime

# library level import
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

# class level import

def preprocessing(lines):
    words = lines.select(
        explode(
            split(lines.value, "t_end")
        ).alias("word")
    )
    
    words = words.na.replace('', None)
    words = words.na.drop()
    words = words.withColumn('word', F.regexp_replace('word', r'http\S+', ''))
    words = words.withColumn('word', F.regexp_replace('word', '@\w+', ''))
    words = words.withColumn('word', F.regexp_replace('word', '#', ''))
    words = words.withColumn('word', F.regexp_replace('word', 'RT', ''))
    words = words.withColumn('word', F.regexp_replace('word', ':', ''))
    return words


if __name__ == "__main__":
    # create Spark session
    # read the tweet data from socket -> store it as lines object
    spark = SparkSession.builder.appName("TwitterSentimentAnalysis").getOrCreate()
    lines = spark.readStream.format("socket").option("host", "127.0.0.1").option("port", 5555).load()
    words = preprocessing(lines)

    # start_time = datetime.now()

    query = words.writeStream.queryName("all_tweets")\
        .outputMode("append").format("parquet")\
        .option("path", "./data/parc")\
        .option("checkpointLocation", "./data/checkpoint")\
        .trigger(processingTime='60 seconds').start()

    # stream data in 1 minute interval for 10 minutes
    # if (datetime.now() - start_time).total_seconds() >= 600:
    #     query.stop()
    query.awaitTermination()
