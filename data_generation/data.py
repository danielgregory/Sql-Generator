__author__ = 'Daniel Gregory'
from distributions.gaussian import gaussian_generator


# returns data of the form # [{"NAME": "Donald", "AGE": 54}, ...]
# columns looks like: {"name": str, "age": int}
# n corresponds to the number of rows of data to return
def generate_column_value_pairs(columns, n):
    # generators the distributions
    gs = generate_names()
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
    return data_list


def generate_names():
    while True:
        yield "Donald"




