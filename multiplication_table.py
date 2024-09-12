# Print the multiplication table of the number entered by the user. The table should get displayed in the following form:
num = int(input('Enter any number: '))
low = 1
high = 10

for i in range(low, high+1):
    print(num, 'x', i, '=', num*i)