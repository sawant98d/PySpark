## PySpark & AWS: Master Big Data With PySpark and AWS
### Hands on Big Data course including in demand industry skills

### BIG DATA

### Prerequisites

### Website: www.aisciences.io

### Applications of Spark

### Applications of Spark 
- Streaming Data
- Machine Learning
- Batch Data
- ETL Pipelines
- Full load and Replication on going

### What's inside

### Methodology

### Projects
- Student Data Analysis
- Employee Data Analysis
- Collaborative Filtering
- Spark Streaming
- ETL Pipeline
- Full Load and Replication on Going

## SPARK
### Why Spark?
- Speed
- Distributed
- Advanced Analytics
- Real Time
- Powerful Caching
- Fault Tolerant
- Deployment

## HADOOP

![Hadoop Ecosystem](https://github.com/sawant98d/PySpark/blob/master/screenshot/1.png)
![Map & Reduce](https://github.com/sawant98d/PySpark/blob/master/screenshot/2.png)

## Spark Architecture
![Spark Architecture](https://github.com/sawant98d/PySpark/blob/master/screenshot/3.png)

## Spark Ecosystem
![Spark Ecosystem](https://github.com/sawant98d/PySpark/blob/master/screenshot/4.png)

## Data Bricks

## Spark Local Setup

## Spark RDD's
- RDD is the spark’s core abstraction which stands for Resilient Distributed Dataset
- RDD is the immutable distributed collection of objects
- Internally spark distributes the data in RDD, to different nodes across the cluster to achieve parallelization.

## Transformations and Actions
- Transformation creates new RDD from an existing one.
- Actions return a value to the driver program after running a computation on the RDD
- All transformation in Spark are lazy
- Spark only triggers the data flow when there is a action.

## Creating Spark RDD

## Running code locally

## map()
- Map is used as a mapper of data from one state to another
- It will create a new RDD
- rdd.map(lambda x:x.split())

- Quiz

![image](https://user-images.githubusercontent.com/53881680/132971263-78306af0-6977-4640-a7c5-0bbba8d74ae4.png)

- Quiz solution : https://github.com/sawant98d/PySpark/blob/master/RDD%20Map.py

## flatMap()
- Flat Map is used as a mapper of data and explodes data before final output 
- It will create new RDD
- rdd.flatMap(lambda x:x.split()) 
- https://github.com/sawant98d/PySpark/blob/master/flat_map.py
- https://github.com/sawant98d/PySpark/blob/master/flat_map.ipynb

## filter()
- Filter is used to remove the elements from the RDD
- It will create new RDD
- rdd.filter(lambda x:x!=12)

- Quiz

![image](https://user-images.githubusercontent.com/53881680/132971368-f468a306-4bcf-4c6b-9f73-40b29fe1cd96.png)

- Quiz solution - https://github.com/sawant98d/PySpark/blob/master/filter_quiz.py

## distinct()
- Distinct is used to get the distinct elements in RDD
- It will create new RDD
- rdd.distinct()
- https://github.com/sawant98d/PySpark/blob/master/rdd_distinct.ipynb

## groupByKey()
- groupByKey() is used to create group based on Keys in RDD
- For groupByKey to work properly the data must be in the format of (k,v), (k,v), (k2,v), (k2,v)
-  - Example ("Apple",1), ("Ball",1), ("Apple",1)
-  It will create a new RDD
-  rdd.groupByKey()
-  mapValues(list) are usually used to get the group data
