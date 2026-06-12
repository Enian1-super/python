snack_name = "Chips"
price = 1.50
quantity = 10
is_available = True


print("Snack: " + snack_name)
print("Price: " , price)
print("Quantity: " , quantity)
print("Is available: " , is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))




total = price * quantity
print("Total cost: " , total)
print("Sale price: " , price - 0.25)
print("Double stock: " , quantity * 2)

shop_name = "Quick " + "Bites"
print("Shop Name: " + shop_name)
print("Letters in snack name: " , len(snack_name))
print("First letter: " + snack_name[0])




price_a = 1.50
price_b = 3.00

print("Before: " , price_a , " and " , price_b)

temp = price_a
price_a = price_b
price_b = temp

print("After: " , price_a , " and " , price_b)

