import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load cleaned data
sales_data = pd.read_csv('../data/sales_data_cleaned.csv')

# Extract metrics
total_revenue = sales_data['Total Amount'].sum()
average_daily_sales = sales_data.groupby('Date')['Total Amount'].sum().mean()
top_category = sales_data.groupby('Product Category')['Total Amount'].sum().idxmax()


# Print summary metrics
print(f"Total Revenue: ${total_revenue}")
print(f"Average Daily Sales: ${average_daily_sales: .2f}")
print(f"Top Category: {top_category}")

# Create a figure with subplots
plt.figure(figsize=(15, 10))

# Subplot 1: Daily Sales Trend
plt.subplot(2, 2, 1)
daily_sales = sales_data.groupby('Date')['Total Amount'].sum().reset_index()
plt.plot(daily_sales['Date'], daily_sales['Total Amount'], marker='o', linestyle='-')
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True)

# Subplot 2: Monthly Sales Trend
plt.subplot(2, 2, 2)
sales_data['Month'] = pd.to_datetime(sales_data['Date']).dt.month
sales_data['Year'] = pd.to_datetime(sales_data['Date']).dt.year
monthly_sales = sales_data.groupby(['Year', 'Month'])['Total Amount'].sum().reset_index()
sns.barplot(x='Month', y='Total Amount', data=monthly_sales, errorbar=None)
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')

# Subplot 3: Product Category Performance
plt.subplot(2, 2, 3)
category_sales = sales_data.groupby('Product Category')['Total Amount'].sum().reset_index()
sns.barplot(x='Total Amount', y='Product Category', data=category_sales, palette='viridis', hue=None, legend=False)
plt.title('Sales by Product Category')
plt.xlabel('Total Sales')
plt.ylabel('Product Category')

# Subplot 4: Customer Age Distribution
plt.subplot(2, 2, 4)
sns.histplot(sales_data["Age"], kde=True, bins=15, color='purple')
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
