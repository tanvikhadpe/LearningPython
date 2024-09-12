import math


# The floor function returns the nearest integer value below the specified number. 
# Please note that the results are not symmetrical for positive and negative numbers. 
# For example: floor(2.15) returns 2, while floor(-2.15) returns -3.
print("Floor of -2.8: ", math.floor(-2.8))
print("Floor of -0.5: ", math.floor(-0.5))
print("Floor of 0.2: ", math.floor(0.2))
print("Floor of 1.5: ", math.floor(1.5))
print("Floor of 2.9: ", math.floor(2.9))
print()

# The trunc function truncates the number to the specified number of decimal places, without rounding of any kind: 
# trunc(2.15,1) will return 2.1, trunc(-2.15,1) returns -2.1, and trunc(2.15) returns 2. 
# If the number is an integer type, it will be returned unchanged (as an integer), 
# even if the number of decimals was specified and not 0.
print("Trunc of -2.8: ", math.trunc(-2.8))
print("Trunc of -0.5: ", math.trunc(-0.5))
print("Trunc of 0.2: ", math.trunc(0.2))
print("Trunc of 1.5: ", math.trunc(1.5))
print("Trunc of 2.9: ", math.trunc(2.9))
print()

# The ceil function ("ceiling") returns the nearest integer value above the specified number. 
# Here there is also no symmetry for positive and negative number ranges. 
# Example: ceil(2.15) returns 3, and ceil(-2.15) returns -2.
print("Ceil of -2.8: ", math.ceil(-2.8))
print("Ceil of -0.5: ", math.ceil(-0.5))
print("Ceil of 0.2: ", math.ceil(0.2))
print("Ceil of 1.5: ", math.ceil(1.5))
print("Ceil of 2.9: ", math.ceil(2.9))






# floor , ceil , trunc , and round always return a float .