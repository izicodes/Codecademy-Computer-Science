weight = 8.40
cost = 0

# Ground Shipping
ground_shipping_flat_charge = 20.00
ground_shipping_premium_flat_charge = 125.00

if weight <= 2:
  price_per_pound = 1.50
  cost = (weight * price_per_pound) + ground_shipping_flat_charge
  print("$" + str(cost))
elif weight > 2 and weight <= 6:
  price_per_pound = 3.00
  cost = (weight * price_per_pound) + ground_shipping_flat_charge
  print("$" + str(cost))
elif weight > 6 and weight <= 10:
  price_per_pound = 4.00
  cost = (weight * price_per_pound) + ground_shipping_flat_charge
  print("$" + str(cost))
else:
  price_per_pound = 4.75
  cost = (weight * price_per_pound) + ground_shipping_flat_charge
  print("$" + str(cost))


