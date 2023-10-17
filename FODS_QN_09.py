import matplotlib.pyplot as plt

# Sample data for sales over time
months = ['January', 'February', 'March', 'April', 'May']
sales = [100, 130, 80, 110, 150]

# 1. Simple Line Plot
plt.figure(figsize=(8, 6))
plt.plot(months, sales, marker='o', linestyle='--', color='b', label='Sales over Time')
plt.title('Product Sales over Time')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.show()

# 2. Scatter Plot
plt.figure(figsize=(8, 6))
plt.scatter(months, sales, color='r', marker='o')
plt.title('Product Sales over Time')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()

# 3. Bar Plot
plt.figure(figsize=(8, 6))
plt.bar(months, sales, color='g', alpha=0.7)
plt.title('Product Sales over Time')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.show()
