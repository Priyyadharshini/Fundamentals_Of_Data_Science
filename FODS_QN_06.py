import pandas as pd

order_data = pd.DataFrame({
     'customer_ID': [1, 2, 1, 3, 2],
     'order_date': ['2023-10-10', '2023-10-12', '2023-10-15', '2023-10-17', '2023-10-18'],
     'product_name': ['A', 'B', 'A', 'C', 'B'],
     'order_quantity': [2, 3, 1, 2, 1]
 })

total_orders_by_customer = order_data['customer_ID'].value_counts()

average_order_quantity = order_data.groupby('product_name')['order_quantity'].mean()

earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()


print("Total number of orders made by each customer:")
print(total_orders_by_customer)
print("\nAverage order quantity for each product:")
print(average_order_quantity)
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
