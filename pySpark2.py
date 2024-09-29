from pyspark.sql import SparkSession
import pandas as pd
df=[("Nikhil",43),("Aditya",34),("JD",23)]


spark = SparkSession.builder \
       .appName("MyApp") \
       .getOrCreate()



print(spark)

