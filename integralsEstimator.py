import random
import numpy as np
from matplotlib import pyplot as plt

# a is a start argument for definite integral
a = 0
# b is an end argument for definite integral
b = 1


# solves function f for given argument x

# point a1
# def f(x):
#     return x ** (1/3)


# point a2
# def f(x):
#     return np.sin(x)


# point a3
def f(x):
    return 4 * x * pow((1 - x), 3)


# finds min(m) where m >= sup{f(x): x belongs to [a, b]}
def find_m(a, b):
    val = []
    for x in np.arange(a, b, 0.01):
        val.append(f(x))
    return max(val)


# returns aproximation of integral for given parameters
def aprox(n, a, b, m):
    c = 0
    for i in range(1, n + 1):
        x = random.uniform(a, b)
        y = random.uniform(0, m)
        if y <= f(x):
            c += 1
    # return aproximation of integral given by formula (c/n) * (b - a) * m
    apr = (c / n) * (b - a) * m
    return apr


# rename file for other functions
file1 = open("data_a3.txt", "w")

# running simulation and saving data to a file
for helper in range(1, 101):
    n = 50 * helper
    avr_sum = 0
    avr = 0
    file1.write(str(n))
    file1.write(", ")
    for k in range(1, 51):
        # saving data
        data = aprox(n, a, b, find_m(a, b))
        file1.write(str(data))
        file1.write(", ")
        avr_sum += data
    avr = avr_sum / 50
    file1.write(", ")
    file1.write(str(avr))
    file1.write("\n")






