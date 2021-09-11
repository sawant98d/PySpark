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

def foo(x):
  l1 = x.split(' ')
  l2 = []
  for l in l1:
    l2.append(int(l)+2)
  return l2

rdd4 = rdd.map(foo)
rdd4.collect()

print(rdd.collect(),rdd2.collect(),rdd3.collect(), rdd4.collect())

# COMMAND ----------


