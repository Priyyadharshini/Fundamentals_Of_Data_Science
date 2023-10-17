import pandas as pd

# Sample sales data stored in a Pandas DataFrame
data = {'Customer_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Customer_Age': [25, 30, 35, 35, 45, 30, 35, 40, 45, 50],
        'Purchase_Amount': [100, 150, 200, 250, 300, 200, 250, 300, 350, 400]}

sales_data = pd.DataFrame(data)

# Finding the frequency distribution of customer ages
age_frequency_distribution = sales_data['Customer_Age'].value_counts()

print("Frequency distribution of the ages of the customers who made a purchase in the past month:")
print(age_frequency_distribution)
