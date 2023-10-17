import numpy as np

house_data= np.genfromtxt('Housing_data.csv', delimiter =',')
bedroom = house_data[:,1]
sale_price= house_data[:,3]

more_than_four_bedrooms = house_data[bedrooms >4]
average_price_more_than_four_bedrooms = np.mean(more_than_four_bedrooms [:,3])
  
print(f"The average sale price of  houses with more than four bedrooms is:", average_price_more_than_four_bedrooms )
                    
