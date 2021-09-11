# Databricks notebook source
# For the quiz you'll be using '/FileStore/tables/filter_quiz.txt' file
# Read this file in the RDD
# Write a filter that will remove all the words that are either starting from 'a' or 'c'
# from the RDD
from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("Filter Quiz")
sc = SparkContext.getOrCreate(conf=conf)
rdd = sc.textFile('/FileStore/tables/filter_quiz.txt')
rdd.collect()

# COMMAND ----------

## Filtering the data using remove_text user function
def remove_text(text):
  if text.startswith('a') or text.startswith('c'):
    return False
  else:
    return True

flatRDD = rdd.flatMap(lambda x:x.split()) #Transformation
filterRDD = flatRDD.filter(remove_text) #Transofrmation
lst = filterRDD.collect() #Action
print(' '.join(lst))


# COMMAND ----------

# Filtering the data using lambda function
flatRDD = rdd.flatMap(lambda x:x.split()) # Transofmation
#filterRDD = flatRDD.filter(lambda text: False if (text.startswith('a') or text.startswith('c')) else True )
filterRDD = flatRDD.filter(lambda text: not (text.startswith('a') or text.startswith('c'))) # Alternative for above
filterRDD.collect()

# COMMAND ----------


