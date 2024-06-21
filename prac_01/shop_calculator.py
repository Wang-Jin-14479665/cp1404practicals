DISCOUNT_RATE = 0.9

num_of_items = int(input("Number of items:"))

total_price = 0  # Initialize the total price

for i in range(num_of_items):
    price = float(input("Price of item: "))
    while price < 0:
        print("Invalid number of items!")
        price = float(input("Price of item: "))
    total_price += price

if total_price > 100:
    total_price = total_price * DISCOUNT_RATE

print(f"Total price of {num_of_items} is ${total_price:.2f}")
