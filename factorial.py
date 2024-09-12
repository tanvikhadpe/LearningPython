# Find the factorial value of any number entered through the keyboard.
number = int(input("Enter a number: "))
fact = 1
for i in range(1, number+1):
    fact = fact * i
print(f'Factorial Value is {fact}')