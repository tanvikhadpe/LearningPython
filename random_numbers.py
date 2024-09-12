import random
import time

random.seed(3)
for i in range(5):
    print(random.randint(10,50))
print()
t = int(time.time())
random.seed(t)
for i in range(5):
    print(random.randint(10, 50))


# The seed() method is used to initialize the random number generator.

# The random number generator needs a number to start with (a seed value), to be able to generate a random number.

# By default the random number generator uses the current system time.

# Use the seed() method to customize the start number of the random number generator.

# Setting a seed starts you at a particular known starting point in a long list of pseudorandom numbers.
