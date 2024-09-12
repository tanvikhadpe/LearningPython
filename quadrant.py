# . Given a point (x, y), write a program to find out if it lies on the X- axis, Y-axis or on the origin. Also find the quadrant.

x = int(input('Enter X Co-ordinate of the point:'))
y = int(input('Enter Y Co-ordinate of the point:'))

if x == 0 and y == 0:
    print('Point lies on the origin.')

elif x == 0 and y != 0:
    print("Point lies on Y axis.")

elif x != 0 and y == 0:
    print("Point lies on the X axis.")

else:
    if x > 0 and y > 0:
        print("Point lies in the 1st Quadrant.")
    elif x < 0 and y > 0:
        print("Point lies in the 2nd Quadrant.")
    elif x < 0 and y < 0:
        print("Point lies in the 3rd Quadrant.")
    else:
        print("Point lies in the 4th Quadrant.")