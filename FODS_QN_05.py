item_prices = [10, 20, 30]  
quantities = [2, 3, 1]  
discount_rate = 10
tax_rate = 8  

total_cost_before_discount = sum([price * quantity for price, quantity in zip(item_prices, quantities)])

discount_amount = (discount_rate / 100) * total_cost_before_discount

cost_after_discount = total_cost_before_discount - discount_amount

tax_amount = (tax_rate / 100) * cost_after_discount

total_cost = cost_after_discount + tax_amount

print(f"The total cost for the customer's purchase is: {total_cost}")
