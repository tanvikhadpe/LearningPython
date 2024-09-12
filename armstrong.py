# Print out all Armstrong numbers between 1 and 500.
# If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number. 
# For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 ).

print("Armstrong numbers between 1 and 500 are :")
for num in range(1, 501):
    n = num

    d3 = n % 10
    n = int(n/10)

    d2 = n % 10
    n = int(n/10)

    d1 = n % 10

    if d1**3 + d2**3 + d3**3 == num:
        print(num, end=' ')
