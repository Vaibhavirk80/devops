print("Welcome to Python Calculator!")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2 if num2 != 0 else "Cannot divide by zero"

print("\n----- Results -----")
print("Addition:", sum)
print("Subtraction:", difference)
print("Multiplication:", product)
print("Division:", division)

print("\nThank you for using the calculator!")
