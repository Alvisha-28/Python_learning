company = "TATA"
kilometers = int(input("Enter the kilometers you have driven: "))
fuel_consumed = float(input("Enter the fuel consumed in liters: "))
mileage = kilometers / fuel_consumed
print("The mileage of the car is: ", mileage, "km/liter")   
toll_charges = 500
fuel_cost = fuel_consumed * kilometers/mileage
total_cost = fuel_cost + toll_charges
print("Total cost of the trip is: ", total_cost)
daily_wage = 1000
days = int(input("Enter the number of days you have driven: "))
driver_allowance = daily_wage * days
print("Driver allowance is: ", driver_allowance)
total_trip_cost = total_cost + driver_allowance
print("Total trip cost including driver allowance is: ", total_trip_cost)