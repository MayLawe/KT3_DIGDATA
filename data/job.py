from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("kt3-first-app").getOrCreate()

# 1. Read curated Parquet
df = spark.read.parquet("/data/curated/sales")

# 2. Transformations
clean = (
    df
    .filter(F.col("amount") > 0)
    .withColumn("hour", F.hour("event_time"))
)

# 3. Aggregation
city_revenue = (
    clean
    .groupBy("city")
    .agg(
        F.sum("amount").alias("revenue"),
        F.count("*").alias("orders")
    )
    .orderBy(F.desc("revenue"))
)

# Action: show result
city_revenue.show()

# 4. Save result
(
    city_revenue
    .coalesce(1)
    .write
    .mode("overwrite")
    .parquet("/data/curated/city_revenue")
)

print("DONE: city_revenue written")

spark.stop()
