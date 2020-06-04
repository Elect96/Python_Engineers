#! /usr/bin/python
# src: https://www.pythonforengineers.com/an-introduction-to-numpy-and-matplotlib/
import numpy as np

x = [5, 10, 15, 20, 25]
y = []

# old fashioned C/C++ way
for counter in x:
    y.append(counter / 5)
print("Old fashioned way: x = {} y = {} \n".format(x, y))

# list comprehensions
z = [n / 5 for n in x]
print("List comprehensions: x = {} z = {} \n".format(x, z))

# numpy
try:
    a = x / 5
except:
    print("No, you can't do that with regular Python lists\n")

a = np.array(x)
b = a / 5

print("With Numpy: a = {} b = {} \n".format(a, b))