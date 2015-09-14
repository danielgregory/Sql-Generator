__author__ = 'Daniel Gregory'
from distributions.gaussian import gaussian_generator
import os


def generate_column_value_pairs(columns, n):
    """
     function: dictionary, int -> generator
     Takes a dictionary describing the table columns and generates test data
     to be inserted into the table.

    @return Return data in the form (but as a generator): [{"NAME": "Donald", "AGE": 54}, ...]

    columns looks like: {"name": str, "age": int}

    n corresponds to the number of rows of generated data to return
    as a generator.
    """
    # generators the distributions
    gs = get_names()
    gg = gaussian_generator(5, 5)

    # return result
    data_list = []
    for _ in range(n):
        for k, v in columns.items():
            data_dict = {}
            if v == str:
                data_dict[k] = next(gs)
            elif v == int:
                data_dict[k] = round(next(gg))
            else:
                raise Exception("Type not found")
            data_list.append(data_dict)
    return (data for data in data_list)


def generate_test_data(filename):
    """ Reads file of names and returns each line one at a time
    in a generator."""
    with open(filename) as f:
        lines = f.read().splitlines()
        return (line for line in lines)


def get_names():
    """ Gets test names from file."""
    filename = os.path.dirname(os.path.realpath("data.py")) + "\\data\\resources\\names.txt"
    return generate_test_data(filename)


def get_addresses():
    """ Gets test addresses from file."""
    filename = os.path.dirname(os.path.realpath("data.py")) + "\\data\\resources\\addresses.txt"
    return generate_test_data(filename)





