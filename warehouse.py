n = int(input("enter the no of deliveries: "))
total_dev= 0
for i in range(n):
    amount = float(input("enter the amount of delivery: "))
    total_dev += amount
print("total delivery amount is: ", total_dev)      
avg = total_dev/n
print("average delivery amount is: ", avg)
