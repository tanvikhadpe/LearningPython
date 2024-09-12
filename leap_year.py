year = int(input("Enter a year: "))

# With if-else statements
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,'is a leap year')
        else:
            print(year,'is not a leap year')
    else:
        print(year,'is a leap year')
else:
    print(year,'is not a leap year')

# Using logical operators 'and' & 'or'

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year, 'is a leap year.')
else:
    print(year, 'is not a leap year.') 

