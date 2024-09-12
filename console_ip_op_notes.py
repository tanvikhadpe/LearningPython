# How will you make the following code more compact?
# print('Enter ages of 3 persons')
# age1 = input( )
# age2 = input( )
# age3 = input( )

# age1, age2, age3 = input("Enter 3 values: ").split(',')

# Print "Rendezvous" in a line and retain the cursor in the same line in which the output has been printed?
print('Rendezvous', end = '')

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

# What will be the output of the following code snippet?
l, b = 1.5678, 10.5
print('length = {l} breadth = {b}')

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

n = 3
# n > 5 indicates that value of n be printed right-justified in 5 columns.
# Similarly, n ** 2:>7 indicates that value of n ** 2 be printed right-
# justified within 7 columns.
#    3      9      27
print(f'{n:>5}{n ** 2:>7}{n ** 3:>8}')

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

name = 'Tanvi'
phone = 333666999000
# Tanvi           : 333666999000
# The name variable is left-aligned in a field that is 15 characters wide. 
# Since 'Tanvi' has 5 characters, there will be 10 spaces padding it on the right.
# The phone variable is right-aligned in a field that is 10 characters wide. 
# Since the phone number 333666999000 has 12 digits, it will take the full space without additional padding.
print(f'{name:15} : {phone:10}')

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------


# Print the output of the following code segment using fstring?
x, y, z = 10, 20, 40
print('{0:<5} {1:<7} {2:<8}'.format(x,y,z))
print(f'{x:<5} {y:<7} {z:<8}')

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

# How will you receive arbitrary number of floats from keyboard
numbers = [float(x) for x in input('Enter values: ').split()]
for n in numbers:
    print(n + 10)

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

print(f'{'\nx = ':4}{x:>10}{'\ny = ':4}{y:>10}')
# Correct the above 

# This f-string includes actual newline characters \n for formatting.
# "x = ":4 formats the string "x = " to be at least 4 characters wide. 
# Since "x = " is already 4 characters, it remains unchanged.

# x =         10
# :>10 formats x to be right-aligned within a width of 10 characters. 
# If x has fewer than 10 characters, it is padded with spaces on the left.

# y =         20
# :>10 formats y to be right-aligned within a width of 10 characters, padding with spaces if necessary.

print(f'{x = :>10}\n{y = :>10}')

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

# Receiving boolean values as input:
# b = bool(input("Enter a boolean value: "))

# Receiving complex number as input:
# b = complex(input("Enter a complex value: "))

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

# How will you display price in 10 columns with 4 places beyond decimal points? 
# Assume value of price to be 1.5567894

price = 1.5567894
# price =      1.557
print(f'{price = :10.4}')

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

# Program to receive an arbitrary number of floats using one input( ) statement. 
# Calculate the average of floats received.

num = int(input('How many numbers do you want to input: '))
total_sum = 0
number = [float(x) for x in input("Enter all numbers: ").split()]
for n in range(len(numbers)):
    total_sum = total_sum + number[n]

avg = total_sum / num
print('Average of', num, 'numbers is:', avg)

# --------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------

# Program to receive the following using one input( ) statement.
# Name of the person, Years of service, Diwali bonus received.
# Calculate and print the agreement deduction.
# Formula: deduction = 2 * years of service + bonus * 5.5 / 100

data = input("Name, years of service, bonus: ").split(',')
name = data[0]
service = int(data[1])
bonus = float(data[2])

deduction = float((2 * service) + (bonus * 5.5)/100)
print('Deduction = Rs.', deduction)

