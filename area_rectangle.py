# Determine whether area of rectangle is greater than its perimeter

length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))
area = round((length * width), 2)
perimeter = 2 * (length + width)
print(f'Area = {area}, Perimeter = {perimeter}')

print('Area is greater than periemeter') if area > perimeter else print('Perimeter is greater than area.')
