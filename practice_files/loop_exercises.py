groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Carrots", 0.56],
["Oranges", 3.08]
]

spinach_bought = input("How many bags of spinach did you buy? ")
chocolate_bought = input("and hot chocolate? ")
crackers_bought = input("How many boxes of crakers? ")
carrots_bought = input("How many carrots? ")
oranges_bought = input("How many oranges? ")

spinach_price = int(spinach_bought) * groceries[0][1]
chocolate_price = int(chocolate_bought) * groceries[1][1]
crackers_price = int(crackers_bought) * groceries[2][1]
carrots_price = int(carrots_bought) * groceries[3][1]
oranges_price = int(oranges_bought) * groceries[4][1]
total_price = spinach_price + chocolate_price + crackers_price + carrots_price + oranges_price

print("====Sara's Food Emporium====")
print("Baby Spinach	 $" + str(spinach_price))
print("Hot Chocolate     $" + str(chocolate_price))
print("Crackers   	 $" + str(crackers_price))
print("Carrots		 $" + str(carrots_price))
print("Oranges		 $" + str(oranges_price))
print("============================")
print("Total:	$" + str(total_price))
