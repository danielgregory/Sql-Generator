__author__ = 'Daniel Gregory'


# column_value_pairs is of the form:
# [{"name" : "Donald", "age" : 54}, ...]
def insert_into(table_name, column_value_pairs):
    columns = column_value_pairs[0].keys()
    insert_str = "INSERT INTO " + table_name + " (" + str.join(", ", columns) + ") "
    for data in column_value_pairs:
        value_str = "VALUES ("
        for column in columns:
            insert_data = transform(data[column])
            value_str = value_str + insert_data + ", "
        value_str = value_str[:-2] + ")"
    return insert_str + value_str


## TODO: more work required here
def transform(input_data):
    if type(input_data) == str:
        return "'" + input_data + "'"
    elif type(input_data) == int:
        return str(input_data)
    else:
        return str(input_data)
