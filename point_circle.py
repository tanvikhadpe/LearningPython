#  Given the coordinates (x, y) of center of a circle and its radius, write a program that will determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ) function)
import math
centerX = int(input("Enter X co-cordinate of center of circle: "))
centerY = int(input("Enter Y co-cordinate of center of circle: "))

radius = int(input('Enter radius of circle: '))

print('Enter Co-ordinates of point')
pointX = int(input("Enter X co-cordinate of point: "))
pointY = int(input("Enter Y co-cordinate of point: "))

xDiff = centerX - pointX
yDiff = centerY - pointY

distance = math.sqrt( (xDiff * xDiff) + (yDiff * yDiff) )
if distance == radius:
    print('Point is on the circle.')
elif distance < radius:
    print('Point lies inside the circle.')
else:
    print('Point lies outside the circle.')