import matplotlib.pyplot as plt

# Sample data for monthly sales
months = ['January', 'February', 'March', 'April', 'May']
sales_values = [10000, 12000, 8000, 11000, 15000]

# Creating a line plot for monthly sales data
plt.figure(figsize=(8, 6))
plt.plot(months, sales_values, marker='o', linestyle='--', color='b', label='Monthly Sales')
plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales Values')
plt.legend()
plt.grid(True)
plt.show()
