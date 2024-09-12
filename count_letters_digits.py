# Write a program to count the number of alphabets and number of digits in the string 'Nagpur-440010'

my_string = 'Mumbai-$$$-400055'
alphabets = digits = special = 0

for i in range(len(my_string)):
    if (my_string[i].isalpha()):
        alphabets = alphabets + 1
    
    elif (my_string[i].isdigit()):
        digits = digits + 1
    
    else:
        special = special + 1

print(f'Number of Alphabets: {alphabets}')
print(f'Number of Digits: {digits}')
print(f'Number of Special Characters: {special}')
