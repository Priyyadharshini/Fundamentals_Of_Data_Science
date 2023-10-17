import pandas as pd

property_data = pd.DataFrame({
    'property_ID': [1, 2, 3, 4, 5],
    'location': ['Location A', 'Location B', 'Location A', 'Location C', 'Location B'],
     'number_of_bedrooms': [3, 4, 2, 5, 4],
     'area_square_feet': [1500, 2000, 1200, 3000, 1800],
     'listing_price': [200000, 300000, 180000, 400000, 280000]
 })

average_listing_price_by_location = property_data.groupby('location')['listing_price'].mean()

num_properties_more_than_four_bedrooms = property_data[property_data['number_of_bedrooms'] > 4].shape[0]

property_with_largest_area = property_data[property_data['area_square_feet'] == property_data['area_square_feet'].max()]


print("Average listing price of properties in each location:")
print(average_listing_price_by_location)
print("\nNumber of properties with more than four bedrooms:", num_properties_more_than_four_bedrooms)
print("Property with the largest area:")
print(property_with_largest_area)
