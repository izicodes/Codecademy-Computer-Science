toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)

print("We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = [["pepperoni", 2], ["pineapple", 6], ["cheese", 1], ["sausage", 3], ["olives", 2], ["olives", 7], ["mushrooms", 2]]

pizza_and_prices = sorted(pizza_and_prices, key=lambda x: x[1])

cheapest_pizza = pizza_and_prices[0]

print(cheapest_pizza)

priciest_pizza = pizza_and_prices[-1]

print(priciest_pizza)

pizza_and_prices.pop()

pizza_and_prices.insert(6, ["peppers", 2.5])

print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]

print(three_cheapest)