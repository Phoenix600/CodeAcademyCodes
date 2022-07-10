# Your code below:
# creating the list of toppings using thr concept of list
"""Check point-01 """
toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]

# creating the new list 
"""Check point-02 """
prices = [2,6,1,3,2,7,2]

"""Check point-03 """
# number of 2$ slices in your price seciton 
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

"""Check point-04 """
# finding the total number of toppings in toppings list 
num_pizzas = len(toppings)

"""Check point-05 """
# printing the message at user end for more sales 
print(f"We sell {num_pizzas} different kinds of pizza!")

"""Check point-06 """
pizza_and_prices = [[2,"pepperoni"],[6,"pineapple"],[1,"cheese"],[3,"sausage"],[2,"olives"],[7,"anchovies"],[2,"mushrooms"]]
print(pizza_and_prices)
"""Check point-07 """
pizza_and_prices.sort()
"""Check point-08 """
cheapest_pizza = pizza_and_prices[2]
"""Check point-09 """
pricest_pizza = pizza_and_prices[-1]
"""Check point-10 """
pizza_and_prices.pop()
"""Check point-11 """
pizza_and_prices.append([2.5,"peppers"])
pizza_and_prices.sort()
three_cheapest = pizza_and_prices[-3:]
print(three_cheapest)
