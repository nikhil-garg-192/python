import csv
import random

# Define the dimensions of the dataset
num_rows = 100000
num_columns = 50

# Generate random data
data = [[random.random() for _ in range(num_columns)] for _ in range(num_rows)]

# Write data to a CSV file
filename = 'E:\github\python\large_dataset.csv'
with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(data)

print(f"Generated {num_rows} rows and {num_columns} columns of random data in {filename}")
