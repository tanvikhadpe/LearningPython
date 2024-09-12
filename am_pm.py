# Program to print 24 hours of day with suitable suffixes like AM, PM, Noon and Midnight.
for hour in range(24):
    if hour == 0:
        print('12 Midnight')
    if hour < 12:
        print(f'{hour} AM')
    if hour > 12:
        print(hour % 12, 'PM')