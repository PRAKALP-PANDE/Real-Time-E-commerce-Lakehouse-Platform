# spark/test_spark.py

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("test")
    .master("local[*]")
    .getOrCreate()
)

print("Spark Version:", spark.version)

spark.stop()