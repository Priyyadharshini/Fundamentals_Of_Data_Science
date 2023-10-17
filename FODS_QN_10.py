import matplotlib.pyplot as plt

# Sample data for monthly temperature and rainfall
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
temperature = [10, 12, 15, 20, 25, 28, 30, 29, 26, 20, 15, 12]
rainfall = [50, 40, 60, 30, 20, 10, 5, 5, 15, 40, 55, 60]

# 1. Line Plot of Monthly Temperature Data
plt.figure(figsize=(8, 6))
plt.plot(months, temperature, marker='o', linestyle='--', color='b', label='Temperature (in °C)')
plt.title('Monthly Temperature Data for the City')
plt.xlabel('Months')
plt.ylabel('Temperature (°C)')
plt.legend()

# 2. Scatter Plot of Monthly Rainfall Data
plt.figure(figsize=(8, 6))
plt.scatter(months, rainfall, color='r', marker='o')
plt.title('Monthly Rainfall Data for the City')
plt.xlabel('Months')
plt.ylabel('Rainfall (mm)')

plt.show()
