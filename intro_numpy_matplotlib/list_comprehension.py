#! /usr/bin/python
# src: https://www.pythonforengineers.com/an-introduction-to-numpy-and-matplotlib/
import numpy as np

x = [5, 10, 15, 20, 25]
y = []

# old fashioned C/C++ way
for counter in x:
    y.append(counter / 5)
print("Old fashioned way: x = {} y = {} \n".format(x, y))