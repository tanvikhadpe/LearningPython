# Demonstration of while loop

my_list = ['desert', 'dessert', 'to', 'too', 'lose', 'loose']
my_string = 'Mumbai'
i = 0

while i < len(my_list):
    if i > 3:
        break
    else:
        print(i, my_list[i], my_string[i])
        i += 1

# //////////////////////////////////////////////////////////////////
print()
# Rewriting above code using for loop

for i, ele in enumerate(my_list):
    if i > 3:
        break
    else:
        print(i, ele, my_string[i])