__author__ = 'Daniel Gregory'

from random import uniform
from math import pi, sin, sqrt, log


def gaussian_generator(mean, sigma):
    """
    Returns a (lazily-evaluated) generator of floats distributed according
    to a Gaussian, with standard deviation sigma. The numbers are generated
    using the Box-Muller transform.

    see: https://en.wikipedia.org/wiki/Box-Muller_transform """
    while True:
        u_1 = uniform(0, 1)
        u_2 = uniform(0, 1)
        z_1 = sqrt(-2 * log(u_1)) * sin(2 * pi * u_2)
        yield z_1 * sigma + mean