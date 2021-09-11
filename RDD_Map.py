# Databricks notebook source
print("hello world")

# COMMAND ----------

from pyspark import SparkConf, SparkContext

# COMMAND ----------

conf = SparkConf().setAppName("Read File")

# COMMAND ----------

sc = SparkContext.getOrCreate(conf=conf)

# COMMAND ----------

rdd = sc.textFile("/FileStore/tables/sample.txt")

# COMMAND ----------

rdd.collect()

# COMMAND ----------

rdd2 = rdd.map(lambda x: x.split())

  

# COMMAND ----------

rdd2.collect()

# COMMAND ----------

rdd3 = rdd.map(lambda x: x+" Dadasaheb")

# COMMAND ----------

print(rdd3.collect())

# COMMAND ----------

print(rdd.collect(),rdd2.collect(),rdd3.collect())

# COMMAND ----------


