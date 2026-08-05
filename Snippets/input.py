# 1. Collecting Text Input - You can capture a user's text and save it directly into a variable for later use.
# Displaying a prompt and storing the result
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")


# 2. Collecting Numeric Input (Type Casting) - Because input() always returns a string, you cannot perform mathematical operations on it directly. You must explicitly convert (typecast) the value using functions like int() or float().
# Convert input string to an integer
age = int(input("Enter your age: "))
years_left = 100 - age
print(f"You will turn 100 in {years_left} years.")

# Convert input string to a floating-point number
price = float(input("Enter item price: "))
print(f"Total with tax: {price * 1.12}")


# 3. Reading Multiple Inputs at Once - You can combine input() with the .split() method to capture multiple space-separated values in a single line.
# Expecting two numbers separated by a space
x, y = input("Enter two numbers: ").split()
total = int(x) + int(y)
print(f"The sum is: {total}")

