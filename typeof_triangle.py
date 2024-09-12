# Is the triangle isosceles, equilateral, scalene or right-angled triangle.
s1 = int(input('Enter the 1st side of triangle: '))
s2 = int(input('Enter the 2nd side of triangle: '))
s3 = int(input('Enter the 3rd side of triangle: '))

# Checking if it is a valid triangle
# The triangle is valid if the sum of two sides is greater than the largest of the three sides
if s1+s2 <= s3 or s2+s3 <= s1 or s1+s3 <= s2:
    print('The sides do not form a triangle.')
else:
    if s1 == s2 and s2 == s3:
        print('Equilateral Triangle')

    if s1 != s2 and s2 != s3 and s3 != s1:
        print('Scalene Triangle.')

    if s1 == s2 and s2 != s3:
        print('Isosceles Triangle.')
    if s2 == s3 and s1 != s3:
        print('Isosceles Triangle.')
    if s1 == s3 and s1 != s3:
        print('Isosceles Triangle.')

    a = (s1**2) == (s2**2) + (s3**2)
    b = (s2**2) == (s1**2) + (s3**2)
    c = (s3**2) == (s1**2) + (s2**2)

    if a or b or c:
        print('Right-angled Triangle.')
        
