def find_min_max(numbers):
    min_value = data[0]
    max_value = data[0]

    for num in data[1:]:
        if num > max_value:
            max_value = num
        if num < min_value:
            num = min_value
    return max_value, min_value

data = input("Enter the numbers separated by spaces: ").split()
data = [int(x) for x in data]

max_value, min_value = find_min_max(data)

print(f"The maximum value is: {max_value}")
print(f"The minumum value is: {min_value}")

# # Can also be done with inbuilt functions as:
# min_value = min(data)
# max_value = max(data)

# print(f"The minimum value is {min_value}")
# print(f"The maximum value is {max_value}")