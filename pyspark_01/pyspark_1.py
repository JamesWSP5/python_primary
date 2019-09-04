from pyspark.sql import SparkSession
from pyspark.sql import Row

spark = SparkSession.builder.appName('yelp').getOrCreate()
s1 = SparkSession.builder.config("k1", "v1").getOrCreate()
print(s1.conf.get("k1") == s1.sparkContext.getConf().get("k1") == "v1")

s2 = SparkSession.builder.config("k2", "v2").getOrCreate()

L = [('Alice', 1)]
print(spark.createDataFrame(L).collect)
print(spark.createDataFrame(L, ['name', 'age']).collect)


