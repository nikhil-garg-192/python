import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker to generate fake data
fake = Faker()

# Define the dimensions of the dataset
num_rows = 100000
num_columns = 50

# Define column names and data types
columns = {
    'Name': 'text',
    'Age': 'number',
    'Birthdate': 'date',
    'Email': 'text',
    'Phone': 'text',
    'Address': 'text',
    'City': 'text',
    'Country': 'text',
    'Salary': 'number',
    'Join_Date': 'date',
    'Department': 'text',
    'Education': 'text',
    'Experience': 'number',
    'Skills': 'text',
    'Project_Name': 'text',
    'Project_Start_Date': 'date',
    'Project_End_Date': 'date',
    'Supervisor': 'text',
    'Client': 'text',
    'Revenue': 'number',
    'Review': 'text',
    'Rating': 'number',
    'Hobbies': 'text',
    'Subscription_Start': 'date',
    'Subscription_End': 'date',
    'Subscription_Type': 'text',
    'Last_Login': 'date',
    'Account_Status': 'text',
    'IP_Address': 'text',
    'Browser': 'text',
    'OS': 'text',
    'Device': 'text',
    'Payment_Method': 'text',
    'Transaction_Date': 'date',
    'Transaction_Amount': 'number',
    'Product_Name': 'text',
    'Product_Category': 'text',
    'Product_Price': 'number',
    'Quantity': 'number',
    'Order_Date': 'date',
    'Shipping_Address': 'text',
    'Shipping_City': 'text',
    'Shipping_Country': 'text',
    'Promotion_Code': 'text',
    'Promotion_Discount': 'number',
    'Promotion_Start_Date': 'date',
    'Promotion_End_Date': 'date',
    'Promotion_Description': 'text'
}

# Generate data for each column
data = {col_name: [] for col_name in columns}

for _ in range(num_rows):
    for col_name, col_type in columns.items():
        if col_type == 'text':
            data[col_name].append(fake.word())
        elif col_type == 'number':
            data[col_name].append(random.randint(1, 1000))
        elif col_type == 'date':
            start_date = datetime.now() - timedelta(days=365)
            random_date = fake.date_time_between(start_date=start_date, end_date='now')
            data[col_name].append(random_date)

# Create DataFrame
df = pd.DataFrame(data)

# Write to CSV file
filename = 'E:\github\python\large_dataset_with_consistent_types.csv'
df.to_csv(filename, index=False)

print(f"Generated {num_rows} rows and {num_columns} columns of data with consistent types and meaningful column names using pandas in {filename}")
