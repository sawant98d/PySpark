# Databricks notebook source
#Example of working flatMap
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("Flat Map")
sc = SparkContext.getOrCreate(conf=conf)
rdd = sc.textFile('/FileStore/tables/sample.txt')
rdd.collect()

# COMMAND ----------

#Explaination of how traditional map works
new_rdd = rdd.map(lambda x:x.split())
new_rdd.collect()

# COMMAND ----------

#Explaination of how flatMap works
new_rdd = rdd.flatMap(lambda x:x.split())
new_rdd.collect()

# COMMAND ----------


