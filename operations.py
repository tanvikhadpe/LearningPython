# Print imaginary part
import math


a = 2+3j
print(a.imag)

# Obtain conjugate of 4+2j
b = 4+2j
print(b.conjugate())

# Decimal equivalent
c = '1100001110'
print(int(c,2))

# Convert float into numeric string
d = 4.33
print(str(d))

# Obtain quotient, remainder while dividing 29 by 5
print(divmod(29,5))

# Obtain hexadecimal equivalent of decimal
print(hex(34567))

# Round-off a number to second deciaml place
print(round(45.6782, 2))

# Obtain 4 from 3.556
print(round(3.556))

# Obtain 17 from 16.7844
print(round(16.7844))

# Obtain remainder 
print(3.455 % 1.22)

# Find minimum
print(min(2, 5, 7, 6))

# Find binary
print(bin(46))

# Find hypotenuse
print(math.hypot(6,8))

# modf: returns the fractional and integer parts of the number in a two-item tuple
# (remainder(fractional part), quotient(integer part))
print(math.modf(3.145))