# Print all prime numbers from 1 to 300
for num in range(1, 301):
    for n in range(2,num):
        if num % n == 0:
            break
    else:
        print(num, end=', ')
