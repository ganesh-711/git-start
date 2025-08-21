# Simple addition program
def add_numbers(a, b):
    return a + b

# Get input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate and display result
result = add_numbers(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")
