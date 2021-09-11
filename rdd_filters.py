# Databricks notebook source
# DEMO Of RDD Filters
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("RDD Filters")
sc = SparkContext.getOrCreate(conf=conf)
rdd = sc.textFile("/FileStore/tables/sample.txt")
rdd.collect()

# COMMAND ----------

#Normal Map or FlatMap
new_rdd = rdd.map(lambda x:x.split())
new_rdd.collect()

# COMMAND ----------

# Demostration of RDD filter
new_rdd = rdd.filter(lambda x: x!='0 9 87 8')
new_rdd.collect()

# COMMAND ----------

def foo(x):
   if x!='0 9 87 8':
      return True
   else:
    return False
    
new_rdd = rdd.filter(foo)
new_rdd.collect()

# COMMAND ----------


