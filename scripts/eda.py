import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load cleaned data
sales_data = pd.read_csv('../data/sales_data_cleaned.csv')

# Convert 'Date' to datatime format if not already done
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

# Confirm the data types
print("Updated Dataset Info:")
print(sales_data.info())

# Group data by Date to calculate daily total sales
daily_sales = sales_data.groupby('Date')['Total Amount'].sum().reset_index()

# Display the first few rows of daily sales
print("Daily Sales:")
print(daily_sales.head())

# Extract Month and Year from Date
sales_data["Month"] = sales_data["Date"].dt.month
sales_data["Year"] = sales_data["Date"].dt.year

# Group data by Year and Month
monthly_sales = sales_data.groupby(['Year', 'Month'])['Total Amount'].sum().reset_index()

# Display monthly sales
print("Monthly Sales Trends")
print(monthly_sales.head())

# Calculate total sales by Product Category
category_sales = sales_data.groupby('Product Category')['Total Amount'].sum().reset_index()

# Sort by Total Amount in descending order
category_sales = category_sales.sort_values(by='Total Amount', ascending=False)

# Display product category performance
print("Sales by Product Category")
print(category_sales)

# Age distribution
age_distribution = sales_data['Age'].value_counts().sort_index()

# Gender distribution
gender_distribution = sales_data['Gender'].value_counts()

# Display distributions
print("Age Distributions")
print(age_distribution)
print("Gender Distributions")
print(gender_distribution)

# Plot daily sales trend
plt.figure(figsize=(10, 6))
plt.plot(daily_sales['Date'], daily_sales['Total Amount'], color='blue', marker='o', linestyle='-', linewidth=2)
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()

# Bar plot for monthly sales
plt.figure(figsize=(10, 6))
plt.bar(monthly_sales['Month'], monthly_sales['Total Amount'], color='green')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(monthly_sales['Month'])  # Ensure all months are labeled
plt.show()

# Bar plot for product category sales
plt.figure(figsize=(10, 6))
sns.barplot(x='Total Amount', y='Product Category', data=category_sales, palette='viridis')
plt.title('Total Sales by Product Category')
plt.xlabel('Total Sales')
plt.ylabel('Product Category')
plt.show()

# Histogram for age distribution
plt.figure(figsize=(10, 6))
sns.histplot(sales_data['Age'], kde=True, bins=15, color='purple')
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Saving Key Outputs
daily_sales.to_csv('../data/daily_sales.csv', index=False)
monthly_sales.to_csv('../data/monthly_sales.csv', index=False)
category_sales.to_csv('../data/category_sales.csv', index=False)
print("Key Insights saved to CSV files.")
