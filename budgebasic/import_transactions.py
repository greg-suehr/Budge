import csv
import sqlite3

from collections import defaultdict


def validate_payload_mapping(payload_mapping):
    """transactions requires: description, date, inflow, outflow
       allows: category_id, a list of tag_ids, memo
    """
    required_fields = {'description': 0, 'date': 0,
                       'inflow': 0, 'outflow': 0 }

    allowed_fields = ['category_id', 'tag_ids', 'memo']

    for field in payload_mapping.keys():
        if field in required_fields.keys():
            required_fields[field] = 1
        else:
            if field not in allowed_fields: return False

    if 0 in required_fields.values(): 
        return False
    else:
        return True


def load_transactions_from_file(connection, file, delimiter=",", payload_mapping=None, paystore_format=None):
    """Inserts records to `transactions` from a csv file.

       If a payload_mapping is not provided, prompt the user. Reprompt and show an
       error if an invalid mapping is provided.
    """
    if payload_mapping is None:
        print("load_transactions_from_csv requries a field mapping atm.")
        return

    if not validate_payload_mapping(payload_mapping):
        print("invalid payload mapping") # TODO: tell me whyyy it's invalid

    c = conn.cursor()

    f = open(file, "r")
    payload_iterable = list(csv.reader(f, delimiter=delimiter))

    for payload in payload_iterable:
        
        paystore = defaultdict()
        for field in payload_mapping.keys():
            paystore[field] = payload[payload_mapping[field]]    
        
        insert_sql = "INSERT INTO transactions ("

        field_list = list(paystore.keys()) # keep in order
        for field in field_list:
            insert_sql += field + ","
        insert_sql = insert_sql.rstrip(",")
        insert_sql += ") VALUES ("
        for field in field_list:
            # TODO: this is a more general problem
            if field in ['description', 'date', 'memo']:
                insert_sql += '"' + paystore[field] + '",' # wrap string fields in ""
            else:
                if paystore[field] == "": paystore[field] = "0.00" # clean up empty money fields
                insert_sql += paystore[field].lstrip("$").replace(",","") + "," # clean up money fields

        insert_sql = insert_sql[:-1] # remove one of two trailing commas, no rstrip
        insert_sql += ")"

        print(insert_sql)
        try:
            c.execute(insert_sql)
            conn.commit()
        except sqlite3.OperationalError as error:
            print(error)
            print(payload)


# script

conn = sqlite3.connect("budge.db")

payload_mapping = {'description': 1, 'date': 0, 'inflow': 4, 'outflow': 5}
load_transactions_from_file(conn, "june_transactions.tsv", delimiter="\t", payload_mapping=payload_mapping)
