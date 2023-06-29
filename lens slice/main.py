toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = [["pepperoni", 2], ["pineapple", 6], ["cheese", 1], ["sausage", 3], ["olives", 2], ["olives", 7], ["mushrooms", 2]]

sorted_pizza_and_prices = sorted(pizza_and_prices, key=lambda x: x[1])

print(sorted_pizza_and_prices)

cheapest_pizza = sorted_pizza_and_prices[0]

print(cheapest_pizza)