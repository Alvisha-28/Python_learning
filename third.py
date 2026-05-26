item = str(input("Enter the name of the item: "))
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))       
total_cost = price * quantity
print("Total cost of the item is: ", total_cost)
membership = str(input("Enter your membership status (Gold/Silver): "))
if membership == "Gold":
    discount = 0.1 * total_cost
    print("Discount is: ", discount)
    final_cost = total_cost - discount
    print("Final cost after discount is: ", final_cost)
else:    print("No discount applied. Final cost is: ", total_cost)
