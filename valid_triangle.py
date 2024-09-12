# Write a program to check whether a triangle is valid or not, when the
# three angles of the triangle are entered through the keyboard. A triangle
# is valid if the sum of all the three angles is equal to 180 degrees

x = int(input("Enter 1st angle: "))
y = int(input("Enter 2nd angle: "))
z = int(input("Enter 3rd angle: "))

if x+y+z == 180:
    print('Triangle is valid')
else:
    print('Triangle is not valid')