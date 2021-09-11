# Databricks notebook source
# path /FileStore/tables/map_quiz.txt
# QUIZ -
#for the quiz you'll be using this input file '/FileStore/tables/map_quiz.txt'
#Read this file in RDD
#Write a mapper that will provide the length of each word in the following format
#[[2,3,3,4],[4,3,3,4],[4]]

# COMMAND ----------

from pyspark import SparkConf, SparkContext
conf = SparkConf().setAppName("Map Quiz")
sc = SparkContext.getOrCreate(conf=conf)
rdd = sc.textFile("/FileStore/tables/map_quiz.txt")
new_rdd = rdd.collect()
new_rdd

# COMMAND ----------

def count_length(st):
  
  
  row = st.split()
  #print('hel')
  row_len = []
  for l in row:
    row_len.append(len(l))
  return row_lena
  

new_rdd = rdd.map(count_length)
new_rdd.collect()

# COMMAND ----------

new_rdd = rdd.map(lambda x:[len(i) for i in x.split()])
new_rdd.collect()

# COMMAND ----------



# COMMAND ----------


