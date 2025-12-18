# Лаба 8
Models.py

```python
from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __str__(self):
        return f'Obj Student. fio: {self.fio}, birthdate: {self.birthdate}, group: {self.group}, gpa: {self.gpa}'

    def __post_init__(self):
        if isinstance(self.gpa, str) or self.gpa < 0 or self.gpa > 5:
            raise ValueError('Invalid GPA-score')
        try:
            self._date_of_birth = datetime.strptime(self.birthdate, '%Y-%m-%d')
        except:
            raise ValueError('Invalid date format')

    @property
    def age(self) -> any:
        return date.today().year - self._date_of_birth.year

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }

    @classmethod
    def from_dict(cls, d: dict):
        return Student(d["fio"], d["birthdate"], d["group"], d["gpa"])
```


Seriallize.py

```python
import json
import os
from models import Student


def process_students():
    """Основная функция обработки студентов"""

    # Определяем пути к файлам
    base_dir = os.path.join("..", "..", "data", "lab08")
    input_path = os.path.join(base_dir, "students_input.json")
    output_path = os.path.join(base_dir, "students_output.json")

    # Создаем директорию, если ее нет
    os.makedirs(base_dir, exist_ok=True)

    # Проверяем, существует ли input файл
    if not os.path.exists(input_path):
        print(f"Файл {input_path} не найден!")
        print("Создаю пример файла...")

        # Создаем пример данных
        example_students = [
            Student(fio="Иванов Иван ", birthdate="2000-01-15", group="ГРП-101", gpa=4.5),
            Student(fio="Петрова Мария", birthdate="2001-03-22", group="ГРП-102", gpa=4.8),
        ]

        # Сохраняем пример в input файл
        example_data = [s.to_dict() for s in example_students]
        with open(input_path, "w", encoding="utf-8") as f:
            json.dump(example_data, f, ensure_ascii=False, indent=2)

        print(f"Пример файла создан в {input_path}")
        return

    # Читаем данные из input файла
    print(f"Обработка файла {input_path}")
    with open(input_path, "r", encoding="utf-8") as f:
        students_data = json.load(f)

    # Создаем объекты Student
    students = []
    for item in students_data:
        try:
            student = Student.from_dict(item)
            students.append(student)
        except ValueError as e:
            print(f"Ошибка в данных: {item.get('fio', 'Неизвестный')} - {e}")

    # Обрабатываем данные
    if students:
        print(f"\nУспешно загружено {len(students)} студентов:")
        for student in students:
            print(f"  - {student.fio}, {student.birthdate}, => {student.age} лет, GPA: {student.gpa}")

        # Сохраняем результат
        output_data = [s.to_dict() for s in students]
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"\nРезультат сохранен в {output_path}")
    else:
        print("Нет корректных данных для обработки")


if __name__ == "__main__":
    process_students()
```
![input.png](images/lab08/input.png)
![result.png](images/lab08/result.png)