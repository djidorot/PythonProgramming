# Comparison Operators - Comparing two values always evaluates to a Boolean answer.
print(10 > 9)   # Returns True
print(5 == 2)   # Returns False (Equality check)
print(7 != 3)   # Returns True  (Inequality check)


# Logical Operators - You can combine or manipulate Boolean values using three main logical keywords:
x = True
y = False

print(x and y)  # Returns False
print(x or y)   # Returns True
print(not x)    # Returns False


# The bool() Function and Truthiness - You can check or convert any value into a Boolean using the built-in Python bool() function. Python categorizes every object as either Truthy (evaluates to True) or Falsy (evaluates to False):
print(bool("Hello"))  # Returns True
print(bool(0))        # Returns False
print(bool([]))       # Returns False


# Conditional Control Flow - Booleans automatically dictate the path your program takes when using if statements or while loops.
is_logged_in = True

if is_logged_in:
    print("Welcome to your dashboard!")
else:
    print("Please log in.")
