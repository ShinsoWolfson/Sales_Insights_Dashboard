import pandas as pd

# Load the dataset
sales_data = pd.read_csv('../data/sales_data.csv')

# Display the first few rows
print("Data Set Preview:")
print(sales_data.head())

# Display dataset structure and data types
print("Dataset Info:")
print(sales_data.info())

# Display summary statistics
print("Summary Statistics:")
print(sales_data.describe())

# Check for missing values
print("Missing Values")
print(sales_data.isnull().sum())

# Fill missing numeric values with 0
sales_data.fillna(0, inplace=True)

# Convert 'Date' column to datetime format
if 'Date' in sales_data.columns:
    sales_data['Date'] = pd.to_datetime(sales_data['Date'], errors='coerce')

# Drop duplicate rows
sales_data.drop_duplicates(inplace=True)

# Save cleaned data to a new CSV file
sales_data.to_csv('../data/sales_data_cleaned.csv', index=False)
print('Cleaned data saved to \'sales_data_cleaned.csv\'')