#one person climbs a stair case with n steps and can climb either 1 or 2 steps at a time find the number of ways to climb the stairs
def count_ways(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_ways(n - 1) + count_ways(n - 2)
number_of_steps = int(input("Enter the number of steps in the staircase: "))
print(f"The number of ways to climb {number_of_steps} steps is: {count_ways(number_of_steps)}")
