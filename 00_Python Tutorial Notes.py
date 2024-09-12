# print is a function
print("Hello World")

name = "Tanvi"
age = 23
price = 25.99

# Will return the data types of the variables (str, int, float) as : <class 'str'>
print(type(name))
print(type(age))
print(type(price))

# Assignment operators: =, +=, -=, *=, /=, %=, **=

num = 10
num += 10
print("num : ", num) # outputs: 20

# TYPE CONVERSION
#  - Type Conversion: Python interpreter does this automatically 

a = 2 #int
b = 1.9 #float
sum = a + b # float
print(type(sum)) # Assigns the superior data type to 'sum'
print(sum) # 2.0 + 1.9 = 3.9

#  - Type Casting: Manually
a, b = 1, "2" # Error bcoz you can only add string to string. Not string to float
c = int(b) # Type Casting happens here
# sum = a + b # Gives error

# Print alphabets from A to Z

# range( ) function cannot be used to generate a sequence of floats.

for alpha in range(65,91):
    print(chr(alpha), end=' ')

