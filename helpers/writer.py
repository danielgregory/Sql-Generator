__author__ = 'Daniel Gregory'
""" Responsible for writing to file."""

import os


def write_to_file(db, lines):
    """ Take an input list of insert statements and write to a file."""
    filename = os.path.dirname(os.path.realpath("writer.py")) + "\\output\\insert_statements.txt"
    with open(filename, 'a') as file:
        file.write("USE " + db + "\nGO\n\n")
        for line in lines:
            file.write(line + "\n")