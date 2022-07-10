weight = float(45)
cost = float(0)

# Ground Shipping 
if weight <= 2.0 and weight > 0:
  price = float(weight*1.50) + 20.0 
  print(price)
elif weight > 2.0 and weight <= 6.0:
  price = float(weight*3.0) + 20.0
  print(price)
elif weight > 6.0 and weight <= 10.0:
  price = float(weight*4.0) + 20.0
  print(price)
elif weight > 10.0 :
  price = float(weight*4.75) + 20.0
  print(price)
else :
  print("Invalid weight")

# Ground Shoipping Premium
cost_premium_shipping = 120.0 
print(cost_premium_shipping)

# Drone Shipping 
if weight <= 2.0 and weight > 0.0:
  price = float(4.50)
  print(price)
elif weight > 2.0 and  weight < 6.0 :
  price = float(9.0)
  print(price)
elif weight > 6.0 and weight <= 10.0 :
  price = float(12.0)
  print(price)
elif weight > 10 :
  price = float(14.25)
  print(price)
else :
  print("Invalid weight")
