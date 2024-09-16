from pyspark.sql import SparkSession

def main():
    # Create a SparkSession
    spark = SparkSession.builder \
        .appName("PySpark Test") \
        .config("spark.socket.timeout", "300s") \
        .master("local[*]") \
        .getOrCreate()

    # Create a DataFrame with some sample data
    data = [("Alice", 34), ("Bob", 45), ("Catherine", 29)]
    columns = ["Name", "Age"]

    df = spark.createDataFrame(data, columns)

    # Show the DataFrame
    df.show()

    # Perform a simple operation: calculate average age
    avg_age = df.groupBy().avg("Age").collect()[0][0]
    print(f"Average Age: {avg_age}")


    web_url = spark.sparkContext.uiWebUrl
    print(f"Spark Web UI is running at: {web_url}")
    # Stop the SparkSession
    #spark.stop()

if __name__ == "__main__":
    main()
