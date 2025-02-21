# Shopping cart program
''' Takes both menu items and their price both by user'''

foods = []
prices = []
total_price = 0
while True:
    food = input("enter your food to buy(press q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = int(input("enter the price of food you want to buy: "))
        foods.append(food)
        prices.append(price)

print("--------------Your Cart is done-------------------")
for food in foods:
    print(food,end=" a"
                   "")
print()
for price in prices:
    total_price += price
print(f"total price of all the food items is {total_price}")


