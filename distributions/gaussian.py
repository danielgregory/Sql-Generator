__author__ = 'Daniel Gregory'

# normal distribution using the Box-Muller transform.
from random import uniform
from math import pi, sin, sqrt, log


## generate 'n' random numbers in a Gaussian distribution
## see: https://en.wikipedia.org/wiki/Box-Muller_transform
def gaussian_generator(mean, sigma):
    while True:
        u_1 = uniform(0, 1)
        u_2 = uniform(0, 1)
        z_1 = sqrt(-2 * log(u_1)) * sin(2 * pi * u_2)
        yield z_1 * sigma + mean