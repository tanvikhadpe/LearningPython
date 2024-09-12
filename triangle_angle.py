# Given three sides a, b, c of a triangle, write a program to obtain and print
# the values of three angles rounded to the next integer. 
# Formula:
# a^2 = b^2 + c^2 -2bc*cosA
# b^2 = a^2 + c^2 -2ac*cosB
# c^2 = a^2 + b^2 -2ab*cosC

import math
a, b, c = 3, 4, 5

angleA = (math.acos((b*b + c*c - a*a) / (2*b*c)) * 180) / 3.14
print("Angle A: ", angleA)

angleB = (math.acos((a*a + c*c - b*b) / (2*a*c)) * 180) / 3.14
print("Angle B: ", angleB)

angleC = (math.acos((a*a + b*b - c*c) / (2*a*b)) * 180) / 3.14
print("Angle C: ", angleC)
