__author__ = 'Daniel Gregory'


def insert_into(table_name, column_value_pairs):
    """
    Given a table name a list of column-value paris, generate
    insert statements in a list.

    column_value_pairs should take the form: [{"name" : "Donald", "age" : 54}, ...]
    """
    insert_strings = []
    for data in column_value_pairs:
        columns = data.keys()
        insert_stem = "INSERT INTO " + table_name + " (" + ", ".join(columns).upper() + ") "
        values = [transform(data[column]) for column in columns]
        insert_str = insert_stem + "VALUES (" + ", ".join(values) + ");"
        insert_strings.append(insert_str)
    return insert_strings


    ## TODO: more work required here
def transform(input_data):
    """
    Match the input data based on type and transform appropriately.
    Input types transform according to the following rules:
    str -> 'str'
    int -> str(int).
    """
    if type(input_data) == str:
        return "'" + input_data + "'"
    elif type(input_data) == int:
        return str(input_data)
    else:
        return str(input_data)