__author__ = 'Daniel Gregory'
from distributions.gaussian import gaussian_generator
import os
from uuid import uuid4


class DataTypes(object):
    def __init__(self, names):
        for number, name in enumerate(names.split()):
            setattr(self, name, number)

dt = DataTypes("uniform_int gaussian_int str datetime uuid")


# TODO: where should this go?
def generate_uuid():
    """
    Returns a random UUID string.
    """
    while True:
        yield uuid4().get_hex()


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
    # generates the distributions
    gs = get_names()
    gg = gaussian_generator(5, 5)
    uuid = generate_uuid()
    # return result
    for _ in range(n):
        data_dict = {}
        for k, v in columns.items():
            if v == dt.str:
                data_dict[k] = next(gs)
            elif v == dt.gaussian_int:
                data_dict[k] = round(next(gg))
            elif v == dt.uuid:
                data_dict[k] = next(uuid)
            else:
                raise Exception("Type not found")
        yield data_dict


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





