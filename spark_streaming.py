
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, to_date, sum
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder.appName("KafkaPurchaseAggregator").getOrCreate()

schema = StructType() \
    .add("user", StringType()) \
    .add("amount", IntegerType()) \
    .add("timestamp", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "purchases") \
    .option("startingOffsets", "latest") \
    .load()

value_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

value_df = value_df.withColumn("date", to_date(col("timestamp")))

agg_df = value_df.groupBy("date").agg(sum("amount").alias("running_total"))

query = agg_df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()
