#  Write a program to convert the following string: 


# [Q.1.] CAPITALIZE EACH WORD
# 'Visit ykanetkar.com for online courses in programming' into
# 'Visit Ykanetkar.com For Online Courses In Programming'

import re


s = 'Visit ykanetkar.com for online courses in programming'
t = ''
for w in s.split():
    t = t + w.capitalize() + ' '
print(t)
print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# [Q.2.] SEARCH AND REPLACE IN STRING
# 'Light travels faster than sound. This is why some people appear bright until you hear them speak.' into
# 'LIGHT travels faster than SOUND. This is why some people appear bright until you hear them speak.'

msg = 'Light travels faster than sound. This is why some people appear bright until you hear them speak.'
new_msg = msg.replace('Light', 'LIGHT').replace('sound', 'SOUND')
print(new_msg)
print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# [Q.3.] STRING FUNCTIONS

a = 'HumptyDumpty'
b = '0123456789'

print("a = ", a)
print("b = ", b)

print('a.isalpha()', a.isalpha())
print('b.isalpha()', b.isalpha())

print('a.isdigit()', a.isdigit())
print('b.isdigit()', b.isdigit())

print('a.isalnum()', a.isalnum())
print('b.isalnum()', b.isalnum())

print('a.islower()', a.islower())
print('a.isupper()', a.isupper())

print('a.startswith(\'Hum\')', a.startswith('Hum'))
print('a.endswith(\'Dump\')', a.endswith('Dump'))

print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# [Q.4.] SEPARATING INDIVIDUAL WORDS IN A STRING
msg = 'The difference between stupidity and genius is that genius has its limits'
for word in msg.split():
    print(word)
print()
# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# [Q.5.] WAYS TO STORE STRING: He said, "Let Us Python".

# Python raw string is created by prefixing a string literal with 'r' or 'R'.
# Python raw string treats backslash (\) as a literal character. This is useful
# when we want to have a string that contains backslash and don't want it
# to be treated as an escape character.


s1 = 'He said, \"Let Us Python\"'
s2 = r'He said, "Let Us Python"'
print()
# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# Returns the identity of an object. This identity is a unique integer that serves as the object's memory address during its lifetime.
# Python outputs the memory address of the string object 'Imaginary'.
print(id('Imaginary')) 

# type('Imaginary') returns <class 'str'>, indicating that the object 'Imaginary' is of type str, which stands for "string".
# This tells you that 'Imaginary' is a string object in Python.
print(type('Imaginary'))
print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

s3 = 'C:\\Users\\Kanetkar\\Documents'
print(s3.split('\\'))
print(s3.partition('\\')) # Partition : useful when you need to split a string at the first occurrence of a separator and need all parts of the split.
print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# Eliminate spaces on either side of the string

c = ' Flanked by spaces on either side '
print(c.strip())
print()

# s.strip('*') removes the asterisks (*) at the beginning and end of the string (spaces by default).
d = '***Hello, World!***'
print(d.strip('*'))
print(d.lstrip())  # 'Hello, World!***' ==> lstrip(): Removes leading characters
print(d.rstrip())  # '***Hello, World!' ==> rstrip(): Removes trailing characters (spaces by default)
print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# Because the string "Hello" is the same for all three assignments, Python points all three variables to the same string object in memory.
# The id() function returns the unique identifier for the object, which is the same for all three variables since they refer to the same object.
sA = sB = sC = 'Hello'
print(id(sA), id(sB), id(sC)) # 36330016 36330016 36330016
print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

msg = 'Aeroplane'
ch = msg[-0]
# Using msg[-0] is not meaningful in python bcoz -0 is same as 0, which returns the first character of the string.
# String indexing allows you to access individual characters of the string. index can be +ve or -ve.
# Positive indices start from the beginning (0 for the first character), and negative indices start from the end (-1 for the last character).
print(ch)
print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# MISCELLANEOUS 
myword = 'Keep yourself warm'
print(myword.swapcase()) # kEEP YOURSELF WARM
print(myword.count('e')) # 3
print(len(myword)) # 18 
print(myword[-1]) # d
print(myword[1:1:1]) # empty string ==> start at index 1 and go up to, but not including, index 1, taking every character with a step of 1
print(myword[-1:3]) # empty string ==> the slice will be empty because it cannot proceed from a higher to a lower index with the default positive step.
print(myword[:-3]) # Keep yourself w
print(myword[-3:]) # arm
print(myword[0:-2]) # Keep yourself wa

print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////

# Example strings that will match each of the given regular expressions:

# 1. **`\w+`**: This matches one or more word characters (letters, digits, or underscores).
#    - Example: `"Hello123"` (matches `Hello123`)

# 2. **`\d{2}`**: This matches exactly two digits.
#    - Example: `"year2022"` (matches `20`)

# 3. **`\w{1,}`**: This matches one or more word characters (same as `\w+`).
#    - Example: `"Test123"` (matches `Test123`)

# 4. **`\w{2,4}`**: This matches between two and four word characters.
#    - Example: `"abcde"` (matches `abcd`)

# 5. **`A*B`**: This matches zero or more 'A' characters followed by a 'B'.
#    - Example: `"AAAB"` (matches `AAAB`)

# 6. **`\d+?`**: This matches one or more digits, but in a non-greedy way (matches as few as possible).
#    - Example: `"12345"` (matches `1` if the expression is part of a larger pattern)

# To illustrate all matches in one example string:

example_string = "AB Hello123 year2022 Test123 abcde AAAB 12345"

# Demonstrating matches
print(re.findall(r'\w+', example_string))  # ['AB', 'Hello123', 'year2022', 'Test123', 'abcde', 'AAAB', '12345']
print(re.findall(r'\d{2}', example_string))  # ['20', '22', '12', '23', '45']
print(re.findall(r'\w{1,}', example_string))  # ['AB', 'Hello123', 'year2022', 'Test123', 'abcde', 'AAAB', '12345']
print(re.findall(r'\w{2,4}', example_string))  # ['AB', 'Hell', 'o123', 'year', '2022', 'Test', '123', 'abcd', 'e', 'AAAB', '1234', '5']
print(re.findall(r'A*B', example_string))  # ['AB', 'AAAB']
print(re.findall(r'\d+?', example_string))  # ['1', '2', '3', '4', '5', '2', '0', '2', '2', '1', '2', '3', '4', '5']


# Each regular expression matches a specific part of the `example_string`.