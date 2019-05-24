import json
import os.path
import sqlite3


class InvalidNumToFind(Exception):
    error_message = 'Invalid number to find'


class InvalidInput(Exception):
    error_message = 'Invalid input args'


class DataBaseIsntExist(Exception):
    error_message = 'Specified database does not exist'


class TableIsntExist(Exception):
    error_message = 'Specified table does not exist'


class ColumnIsntExist(Exception):
    error_message = 'Specified column does not exist'


JSON_PATH = 'telephone_numbers.json'


class NumFinder:

    __slots__ = (
        'cursor', 'database_path', 'numb_to_find', 'table_name', 'column_name'
                 )

    def __init__(
            self, database_path, table_name, column_name):
        if not self.__input_validation(database_path, table_name, column_name):
            self.database_path = database_path
            self.table_name = table_name
            self.column_name = column_name
        self.numb_to_find = None
        self.cursor = None

    @staticmethod
    def __input_validation(database_path, table_name, column_name):
        for element in (database_path, table_name, column_name):
            if not isinstance(element, str) or element is '':
                raise InvalidInput('Invalid input args')

    def __number_validation(self, numb_to_find):
        if isinstance(numb_to_find, int) and not isinstance(
                numb_to_find, bool
                ) and numb_to_find > 0:
            self.numb_to_find = numb_to_find
        else:
            raise InvalidNumToFind('Invalid number to find')

    def __db_validation(self):
        if not os.path.isfile(self.database_path):
            raise DataBaseIsntExist('Specified database does not exist')
        conn = sqlite3.connect(self.database_path)
        self.cursor = conn.cursor()
        self.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' "
            f"AND name='{self.table_name}'"
        )
        if self.cursor.fetchone() is None:
            raise TableIsntExist('Specified table does not exist')
        self.cursor.execute(
            "SELECT COUNT(*) AS CNTREC "
            f"FROM pragma_table_info('{self.table_name}') "
            f"WHERE name='{self.column_name}'"
        )
        if self.cursor.fetchall()[0][0] == 0:
            raise ColumnIsntExist('Specified column does not exist')

    def get_numbers(self, numb_to_find):
        self.__number_validation(numb_to_find)
        self.__db_validation()
        self.cursor.execute(
            f"SELECT DISTINCT {self.column_name}, typeof({self.column_name})"
            f" FROM {self.table_name} "
            f" WHERE {self.column_name} LIKE '{self.numb_to_find}%' "
        )
        result_list = []
        while True:
            value = self.cursor.fetchone()
            if not value or len(result_list) == 10:
                break
            if value[1] == 'integer' and len(str(value[0])) == 11:
                result_list.append(value[0])
            else:
                continue
        with open(JSON_PATH, 'w') as file:
            json.dump({'tel_numbers': result_list}, file, indent=2)
        return result_list

    def __repr__(self):
        return (
            f'{self.__class__.__name__}({self.database_path}, '
            f'{self.table_name}, {self.column_name})'
        )


if __name__ == '__main__':
    from_db = NumFinder('test_db.db', 'TelNumbers', 'tel_numbers')
    from_db.get_numbers(8)
