import pandas as pd

# Assuming you have a CSV file named 'data.csv' in the current directory
# Load data from CSV into a DataFrame
df = pd.read_csv('E:\github\python\sampleFile.csv')

# Display the first few rows of the DataFrame
print("First 5 rows of the DataFrame:")
print(df.head())

# Get basic information about the DataFrame
print("\nDataFrame information:")
print(df.info())

# Summary statistics of numerical columns
print("\nSummary statistics:")
print(df.describe())

# Accessing specific columns
print("\nAccessing specific columns:")
print(df['Salary'])  # Replace 'column_name' with the actual column name

# Filtering rows based on conditions
print("\nFiltering rows based on conditions:")
filtered_data = df[df['Salary'] > 60000]  # Example condition
print(filtered_data.head())

# Adding a new column
df['New_column'] = df['Name'] + df['Education']  # Example calculation
print("\nDataFrame with new column:")
print(df.head())

# Saving the modified DataFrame back to CSV
df.to_csv('E:\github\python\sampleFile_changed.csv', index=False)

# Deleting a column
del df['Education']

# Handling missing data
print("\nHandling missing data:")
print(df.isnull().sum())  # Check for missing values
df.dropna(inplace=True)  # Drop rows with missing values
