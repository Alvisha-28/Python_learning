pin= 1234
max_attempts = 3

for i in range(max_attempts):
    pin = int(input("Enter the pin: "))
    if pin == 1234:
        print("Pin is correct go ahead")
        break
    else:
        remaining_attempts = max_attempts - (i + 1)
        if remaining_attempts > 0:
            print("Incorrect pin. Try again. Remaining attempts: ", remaining_attempts)
        else:
            print("Incorrect pin. No more attempts left. Access denied.")