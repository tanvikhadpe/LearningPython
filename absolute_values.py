# Write a program to find the absolute value of a number entered through the keyboard.
x = float(input("Enter any number: "))

# Calculating the absolute value using abs() function
absolute_value = abs(num)
print(f"The absolute value of {num} using abs() function is {absolute_value}")
if x < 0:
    y = x*(-1)
else:
    y = x
print(f"Absolute value of {x} is {y}")

