# Check if number is odd or even
number = int(input("Enter Number: "))
if number%2 == 1:
    print("Number is Odd!")
else: 
    print("Number is Even!")

# ///////////////////////////////////////////////////

# Generating 1st 25 odd numbers
for num in range(1, 50, 2):
    print(num, end=', ')

# ///////////////////////////////////////////////////

# Another way of 25 odd numbers
count = 0
num = 1

while count < 25:
    if num % 2 != 0:
        print(num, end=', ')
        count += 1
    num += 1