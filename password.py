# Password Strength Analyzer
password = input("Enter password: ")
min_length = int(input("Enter minimum length: "))

score = 0

# Check length
if len(password) >= min_length:
    score += 1

# Check uppercase
if any(c.isupper() for c in password):
    score += 1

# Check lowercase
if any(c.islower() for c in password):
    score += 1

# Check digit
if any(c.isdigit() for c in password):
    score += 1

# Check special character
if any(c in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for c in password):
    score += 1

# Display strength
print(f"Score: {score}/5")
if score >= 4:
    print("Strong password")
elif score >= 2:
    print("Medium password")
else:
    print("Weak password")
