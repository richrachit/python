# Find square root of real or complex number
# Importing the complex math module
import cmath
num = 1+2j
# to take input from the user
# num = eval(input('enter a number:'))
num_sqrt = cmath.sqrt(num)
print(' the sqrt root of {0} is {1:0.3f}+{2:0.3f}j'.format(num , num_sqrt.real,num_sqrt.imag))