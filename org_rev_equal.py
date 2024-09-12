# A five-digit number is entered through the keyboard. Write a program to obtain the reversed number and to determine whether the original and reversed numbers are equal or not.
# Is it a palindrome or not

num = int(input('Enter a 5-digit number: '))
orinum = num
revnum = 0

while num>0:
    rem = num % 10
    revnum = (revnum*10) + rem
    num = num//10

print(f'Original number: {orinum}')
print(f'Reversed number: {revnum}')

if orinum == revnum:
    print('Original and reversed number are same.')
else:
    print('Original and reversed number are not same.')