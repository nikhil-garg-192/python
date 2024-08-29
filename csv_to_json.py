import pandas as pd

def csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Convert the DataFrame to a JSON file
    df.to_json(json_file_path, orient='records', lines=True, indent=4)

# Example usage
csv_file_path = 'E:/github/python/large_dataset_with_consistent_types.csv'
json_file_path = 'E:/github/python/large_dataset_with_consistent_types.json'
csv_to_json(csv_file_path, json_file_path)
