--telephin_assistant.py:
Клас NumFineder принимает путь к базе данных, название таблицы, и название колонки с номерами телефонов.
Метод get_numbers() принимает аргументом число и возващает список с максимум десятью номерами из базы данных, начинающихся с введенного аргумента.
Список с номерами так же сохраняется в 'telephone_numbers.json'.
Пример:

from_db = NumFinder('test_db.db', 'TelNumbers', 'tel_numbers')
from_db.get_numbers(8096)
result = [80963335566, 80967789090, 80965555555]


--generate_db_py:
Метод create_test_db() создает базу данных для тестов со случанйыми значениями номеров телефонов (валидных и не валидных)ю
Принимает аргументы: путь и имя для создания базы данных, название таблицы, название колонки с номерами телефонов (автоматически генерирует ID для каждого елемента)

Метод  get_test_values_from_db() возвращает ВСЕ значения с колонки номеров телефонов и создает 'test_db_data.json' для визуализации инфы.
Принимает аргументыЖ пусть к созданной базе данных, название таблицы, название колонки с номерами телефонов, пусть к созданию .json файла
Пример:
create_test_db('test_db.db', 'TelNumbers', 'tel_numbers')

Результат:  test_db.db

get_test_values_from_db(
        'test_db.db', 'TelNumbers', 'tel_numbers', 'test_db_data'
    ) 

Результат:   test_db_data.json


--test_telephone_assistant.py:
Тесты


--test_db.db - база данных, содержит таблицу 'TelNumbers', таблица срдержит колонки 'ID' и 'tel_numbers'
--test_db_data.json - содержит все значения колонки 'tel_numbers' из 'test_db.db' 

--telephone_numbers.json - содержит результат работы метода get_numbers()