from pyspark.sql import SparkSession

spark=SparkSession.builder \
      .appName("Read File") \
      .getOrCreate()

df = spark.read.csv("E:\github\python\large_dataset_with_consistent_types.csv",header=True,inferSchema=True)
#df.show(4)
#df.printSchema()
#df.describe().show()
#print(type(df.columns))
df_cols=df.select('Name','Age','Transaction_Amount','Quantity')
#df_cols.show(5)
df_filter=df_cols.filter(df_cols['Name']=='heardear')
df_filter.show()

