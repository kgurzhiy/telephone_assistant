--telephin_assistant.py:
���� NumFineder ��������� ���� � ���� ������, �������� �������, � �������� ������� � �������� ���������.
����� get_numbers() ��������� ���������� ����� � ��������� ������ � �������� ������� �������� �� ���� ������, ������������ � ���������� ���������.
������ � �������� ��� �� ����������� � 'telephone_numbers.json'.
������:

from_db = NumFinder('test_db.db', 'TelNumbers', 'tel_numbers')
from_db.get_numbers(8096)
result = [80963335566, 80967789090, 80965555555]


--generate_db_py:
����� create_test_db() ������� ���� ������ ��� ������ �� ���������� ���������� ������� ��������� (�������� � �� ��������)�
��������� ���������: ���� � ��� ��� �������� ���� ������, �������� �������, �������� ������� � �������� ��������� (������������� ���������� ID ��� ������� ��������)

�����  get_test_values_from_db() ���������� ��� �������� � ������� ������� ��������� � ������� 'test_db_data.json' ��� ������������ ����.
��������� ���������� ����� � ��������� ���� ������, �������� �������, �������� ������� � �������� ���������, ����� � �������� .json �����
������:
create_test_db('test_db.db', 'TelNumbers', 'tel_numbers')

���������:  test_db.db

get_test_values_from_db(
        'test_db.db', 'TelNumbers', 'tel_numbers', 'test_db_data'
    ) 

���������:   test_db_data.json


--test_telephone_assistant.py:
�����


--test_db.db - ���� ������, �������� ������� 'TelNumbers', ������� �������� ������� 'ID' � 'tel_numbers'
--test_db_data.json - �������� ��� �������� ������� 'tel_numbers' �� 'test_db.db' 

--telephone_numbers.json - �������� ��������� ������ ������ get_numbers()