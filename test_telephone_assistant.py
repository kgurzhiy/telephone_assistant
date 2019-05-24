import random
from telephone_assistant import *


TEST_TYPE_DATA = [
        random.sample(range(1, 7), 6),
        tuple(random.sample(range(-7, 7), 6)),
        set(random.sample(range(10, 17), 3)),
        random.uniform(-1000000000.0, 100000000000.0),
        {1: 11, 2: 22, 3: 33},
        lambda x: x + 2,
        '', [], {}, (), set(), True, False, None,
        random.randint(-10000, 0)
]


def test_num_finder():
    test_result = NumFinder('test_db.db', 'TelNumbers', 'tel_numbers')
    assert len(test_result.get_numbers(8)) == 10, (
        'Max value of finded elements is 10'
    )
    for i in test_result.get_numbers(8):
        assert isinstance(i, int), 'Elements type'
        assert len(str(i)) == 11, 'Element len'
        assert str(i)[:1] == '8', "Starts from correct value"
    #   80997106990 repeats 10 times
    assert len(test_result.get_numbers(80997106990)) == 1, (
        'Numbers do not repeat'
    )
    for el in TEST_TYPE_DATA:
        try:
            test_result.get_numbers(el)
        except Exception as e:
            assert isinstance(e, InvalidNumToFind), (
                'Test for invalid data type: number'
            )
    for el in TEST_TYPE_DATA:
        try:
            test_result = NumFinder(el, 'TelNumbers', 'tel_numbers')
            test_result.get_numbers(8)
        except Exception as e:
            assert isinstance(e, InvalidInput), (
                'Test for invalid data type: db name'
            )
    for el in TEST_TYPE_DATA:
        try:
            test_result = NumFinder('test_db.db', el, 'tel_numbers')
            test_result.get_numbers(8)
        except Exception as e:
            assert isinstance(e, InvalidInput), (
                'Test for invalid data type: table name'
            )
    for el in TEST_TYPE_DATA:
        try:
            test_result = NumFinder('test_db.db', 'TelNumbers', el)
            test_result.get_numbers(8)
        except Exception as e:
            assert isinstance(e, InvalidInput), (
                'Test for invalid data type: column name'
            )
    incorrect_name = 'incorrect_name'
    try:
        test_result = NumFinder('test_db.db', 'TelNumbers', incorrect_name)
        test_result.get_numbers(8)
    except Exception as e:
        assert isinstance(e, ColumnIsntExist), 'Column Isnt Exist test filed'
    try:
        test_result = NumFinder('test_db.db',  incorrect_name, 'tel_numbers')
        test_result.get_numbers(8)
    except Exception as e:
        assert isinstance(e, TableIsntExist), 'TableIsntExist test filed'
    try:
        test_result = NumFinder(incorrect_name, 'TelNumbers', 'tel_numbers')
        test_result.get_numbers(8)
    except Exception as e:
        assert isinstance(e, DataBaseIsntExist), 'DataBaseIsntExist test filed'
