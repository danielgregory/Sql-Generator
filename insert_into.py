# column_value_pairs is of the form:
# [{"name" : "Donald", "age" : 54}, ...]
def insert_into(table_name, column_value_pairs):
    columns = column_value_pairs[0].keys()
    insert_str = "INSERT INTO " + table_name + " (" + str.join(",", columns) + ") "
    for data in column_value_pairs:
        value_str = "VALUES ("
        for column in columns:
            value_str = value_str + data[column] + ", "
        value_str = value_str[:-2] + ")"
    return insert_str + value_str

# normal distribution using the Box-Muller transform.
from random import uniform
from math import pi, sin, cos, sqrt, log

## generate 'n' random numbers in a Gaussian distribution
def gaussian_generator(mean, sigma):
    while True:
        U_1 = uniform(0,1)
        U_2 = uniform(0,1)
        Z_1 = sqrt(-2 * log(U_1)) * sin(2 * pi * U_2)
        yield Z_1 * sigma + mean

from matplotlib import pyplot as plt

# where f is the generator of the distrubtion
# N is the number of points to generate
def plot_distribution(distribution_generator, N):
    points = [distribution_generator.next() for i in range(N)]
    plt.hist(points, bins = N / 10)
    plt.show()
    
    
    
