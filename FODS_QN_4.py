import numpy as np

sales_data = np.array([10000, 12000, 15000, 18000])

total_sales_for_year = np.sum(sales_data)

percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print(f"The total sales for the year is: {total_sales_for_year}")
print(f"The percentage increase in sales from the first quarter to the fourth quarter is: {percentage_increase:.2f}%")
