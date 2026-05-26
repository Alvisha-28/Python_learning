coordinates = input("Enter the coordinates: ")
x, y = map(float, coordinates.split(","))       
print("The x-coordinate is: ", x)
print("The y-coordinate is: ", y)
coordinates1 = input("Enter the second set of coordinates: ")
x1, y1 = map(float, coordinates1.split(","))        
print("The x-coordinate of the second point is: ", x1)
print("The y-coordinate of the second point is: ", y1)

distance = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
print("The distance between the two points is: ", distance)
