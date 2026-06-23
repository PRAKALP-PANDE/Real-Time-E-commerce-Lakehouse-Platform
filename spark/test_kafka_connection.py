from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("KafkaTest")
    .master("local[2]")
    .config(
        "spark.jars.packages",
        "org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.1"
    )
    .getOrCreate()
)

print("Spark Started Successfully")

spark.stop()