from click import group

from group import Group

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.lab08.models import Student

group = Group('C:\\Users\\Hp\\Desktop\\IDZ-25-6\\data\\lab09\\students.csv')

print(group.list())

#print(group.remove('Михаил Александрович Бакунин'))
#print(group.add(Student(fio='Михаил Александрович Бакунин', birthdate='1814-01-07', group='SE-01', gpa=4.5)))
print(group.update('Сидоров Алексей Петрович', **{'birthdate': '2007-06-26', 'group': 'БИВТ-25-4', 'gpa': 4.2}))
print(group.find('Иванов Иван Иванович'))