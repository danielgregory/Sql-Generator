__author__ = 'Daniel Gregory'
""" A Python script that generates some simple results. """


from data import data
from helpers import writer
from sql import insert_into as sql

dt = data.dt

# define the data type of each column in the table. Note that the
# ages are distributed according to a Gaussian distribution
columns = {"name": dt.str, "age": dt.gaussian_int, "PersonID": dt.uuid}

# return a generator which, when evaluated, gives us the next
# piece of data.
column_value_pairs = data.generate_column_value_pairs(columns, 5)

# generate insert statements from the column-value pairs
insert_statements = sql.insert_into("People", column_value_pairs)

# write the insert statements to a file
writer.write_to_file("MY_DB", insert_statements)
