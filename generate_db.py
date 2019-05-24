import json
import random
import sqlite3
import string


DB_DATA_JSON_PATH = 'test_db_data'


def create_test_db(database_name, table_name, column_name):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY, {column_name} INTEGER
        )"""
    )
    with conn:
        operator_tuple = (8096, 8066, 8059, 8067, 8050, 8068, 8091, 8073, 8099)
        test_chars = string.ascii_letters + string.digits
        for i in range(10):
            rand_op = f'{random.choice(operator_tuple)}'
            rand_num = f"{''.join(random.sample(test_chars, 7))}"
            invalid_value = rand_op + rand_num
            cursor.execute(f"INSERT INTO {table_name} ({column_name}) "
                           f"VALUES ('{invalid_value}')"
                           )
        for i in range(10):

            z = random.choice([5, 8])
            rand_op = random.choice(operator_tuple) * (10 ** z)
            rand_num = random.randint(10000, 99999)
            invalid_len_value = rand_op + rand_num
            cursor.execute(f"INSERT INTO {table_name} ({column_name}) "
                           f"VALUES ('{invalid_len_value}')"
                           )
        for i in range(10):
            rand_op = random.choice(operator_tuple) * (10 ** 7)
            rand_num = random.randint(1000000, 9999999)
            invalid_sign_value = -(rand_op + rand_num)
            cursor.execute(f"INSERT INTO {table_name} ({column_name}) "
                           f"VALUES ('{invalid_sign_value}')"
                           )
        for i in range(30):
            rand_op = random.choice(operator_tuple) * (10 ** 7)
            rand_num = random.randint(1000000, 9999999)
            valid_value = rand_op + rand_num
            cursor.execute(f"INSERT INTO {table_name} ({column_name}) "
                           f"VALUES ('{valid_value}')"
                           )
        for i in range(10):
            cursor.execute(f"INSERT INTO {table_name} ({column_name}) "
                           f"VALUES ('80997106990')"
                           )
        cursor.execute(f"INSERT INTO {table_name} ({column_name}) "
                       f"VALUES ('800000')"
                       )
        cursor.execute(f"INSERT INTO {table_name} ({column_name}) "
                       f"VALUES ('8000000000')"
                       )


def get_test_values_from_db(database_name, table_name, column_name, json_path):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    with conn:
        cursor.execute(f"SELECT {column_name} FROM {table_name}")
        db_data = [i[0] for i in cursor.fetchall()]
    with open(json_path, 'w') as file:
        json.dump(db_data, file, indent=2)
    return db_data


if __name__ == '__main__':
    create_test_db('test_db.db', 'TelNumbers', 'tel_numbers')
    get_test_values_from_db(
        'test_db.db', 'TelNumbers', 'tel_numbers', DB_DATA_JSON_PATH
    )
