lovely_lowerseat_description = '''Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'''
lovely_loveseat_price = float(254.00)
stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

stylish_sette_price = float(180.50)

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

luxurious_lamp_price = float(52.15)

sales_tax = float(0.088)

# our first customer 
customer_one_total = float(0)

# customer_itermization
customer_one_itemization = ""
# updating_total_customer_price
customer_one_total +=  lovely_loveseat_price
# updating the customers description of items 
customer_one_itemization += customer_one_itemization

# updating the price 
customer_one_total += luxurious_lamp_price

# updating the itemization description 
customer_one_itemization += luxurious_lamp_description

# customer has to pay the tax
customer_one_tax = customer_one_total * sales_tax
customer_one_tax += sales_tax
print("Customer One Items : ",customer_one_itemization)
#printing the total cost
print("Customer One Total: ",customer_one_total)

