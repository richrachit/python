a = 5
b = 6
c = 7
# Uncomment below to take inputs from the user
# a = float(input('Enter first side'))
# b = float(input('enter second side'))
# c = float(input('enter third side'))

# calculate the semi-perimeter
s = (a+b+c)/2
# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) **0.5
print("the area of the triangle is %0.2f",area)