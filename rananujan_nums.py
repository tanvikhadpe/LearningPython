# # Ramanujan number is the smallest number that can be expressed as sum
# # of two cubes in two different ways. Write a program to print all such
# # numbers up to a reasonable limit.

# def find_ramanujan_numbers(limit):
#     # Dictionary to store sums of cubes and their corresponding pairs
#     cubes = {}
    
#     # Iterate through possible values for a and b
#     for a in range(1, int(limit**(1/3)) + 1):
#         for b in range(a, int(limit**(1/3)) + 1):
#             sum_of_cubes = a**3 + b**3
#             if sum_of_cubes > limit:
#                 break
#             if sum_of_cubes in cubes:
#                 cubes[sum_of_cubes].append((a, b))
#             else:
#                 cubes[sum_of_cubes] = [(a, b)]
    
#     # Print all numbers that can be expressed as the sum of two cubes in two different ways
#     for sum_of_cubes, pairs in cubes.items():
#         if len(pairs) > 1:
#             print(f"{sum_of_cubes} can be expressed as the sum of cubes in two different ways:")
#             for pair in pairs:
#                 print(f"{pair[0]}^3 + {pair[1]}^3")
#             print()

# # Set a reasonable limit
# limit = 40000

# # Find and print all Ramanujan numbers up to the limit
# find_ramanujan_numbers(limit)


# Another way:
for i in range(1, 31):
    for j in range(1, 31):
        for k in range(1, 31):
          for l in range(1, 31):
            if (i != j and i != k and i != l) and (j != k and j != l) and (k != l ) :
                if i * i * i + j * j * j == k * k * k + l * l * l :
                    print(i, j, k, l)
