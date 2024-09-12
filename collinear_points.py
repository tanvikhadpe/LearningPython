#  Given three points (x1, y1), (x2, y2) and (x3, y3), write a program to check if all the three points fall on one straight line.

x1 = int(input('Enter the co-ordinate of x1: '))
y1 = int(input('Enter the co-ordinate of y1: '))
x2 = int(input('Enter the co-ordinate of x2: '))
y2 = int(input('Enter the co-ordinate of y2: '))
x3 = int(input('Enter the co-ordinate of x3: '))
y3 = int(input('Enter the co-ordinate of y3: '))

if x1 == x2 and x2 == x3:
    print("Collinear")
elif x1 != x2 and x2 != x3 and x3 != x1:
    # Calculating slope using 2-point formula: (y2 - y1) / (x2 - x1)
    s1 = (float(abs(y2 - y1))) / float(abs(x2 - x1))
    s2 = (float(abs(y3 - y2))) / float(abs(x3 - x2))
    s3 = (float(abs(y3 - y1))) / float(abs(x3 - x1))

    if s1 == s2 and s2 == s3:
        print("Collinear. All the 3 points lies on the one straight line") 
    else: 
        print("Non-collinear")
