foods = [] # List to store food items
prices = [] # List to store prices of food items
total = 0 # Variable to store total price

while True:
    food = input("Enter a food item ('exit' or 'done' to finish): ")
    if food.lower() == 'done' or food.lower() == 'exit':
        break
    try:
        price = float(input(f"Enter the price for {food}: "))
        if price < 0:
            print("Price cannot be negative. Please enter a valid price.")
            continue
        foods.append(food)
        prices.append(price)
        total += price
    except ValueError:
        print("Invalid input. Please enter a numeric value for the price.")
        
print(foods)
print(prices)
for food, price in zip(foods, prices):
# for food in foods:
    print(f"Food item: {food} for ${price:.2f}")
# for price in prices:
#     total += price

print(f"Total price: ${total:.2f}")
