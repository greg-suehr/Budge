import os
import yaml
import sqlite3

def create_schema_dict_from_yaml(schema_file):
    """Reads a YAML file in /schema into a dict"""
    f = open(schema_file, "r")
    return yaml.load(f, Loader=yaml.FullLoader)

def create_table_from_yaml(schema_dict, db_cursor, validate=False):
    """Create a sqlite3 table in the connected database from a schema dict"""

    create_table = "CREATE TABLE " + schema_dict['name'] + " ("    
    column_list = list(schema_dict['columns'].keys())

    for column in column_list:
        column_dict = schema_dict['columns'][column]

        # throw nice errors for misformatted YAML, but only in debug mod
        if validate:
            try:
                assert 'datatype' in column_dict.keys()
                assert column_dict['datatype']
            except AssertionError:
                print(error) # TODO: print the "nice" error :)

        create_table += column + " " + column_dict['datatype']

        if 'key' in column_dict.keys():
            create_table += " " + column_dict['key'] + " key,"
        else:
            create_table += ","
    create_table = create_table.rstrip(",")
    create_table += ")"

    if validate: print(create_table)

    try:
        db_cursor.execute(create_table) # TODO: commit this corretly
    except Exception as error:
        return error


if __name__ == "__main__":
    db_name = input("Specify the path and filename for the sqlite database: ")
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    yaml_dir = input("Specify the path to a directory containing YAML schema files: ")
    for schema_file in os.listdir(yaml_dir): # TODO: fix this path when it breaks
        if schema_file.endswith('.yml'):
            schema = create_schema_dict_from_yaml(yaml_dir + "/" +  schema_file)

            print("on %s" % schema_file)
            response = create_table_from_yaml(schema, c)
            if response is not None: print(response)



