from pathlib import Path
import json
import csv

def json_to_csv(json_path, csv_path):
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.exists():
        raise FileNotFoundError("Файл не найден")

    if json_file.suffix.lower() != ".json":
        raise ValueError("Неверный формат файла")
    if csv_file.suffix.lower() != ".csv":``
        raise ValueError("Неверный формат файла")


    with json_file.open('r', encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Некорректный JSON-файл")
    if not isinstance(data, list) or not all(isinstance(value, dict) for value in data):
        raise ValueError("Ожидается список словарей")
    if not data:
        raise ValueError("Пустой JSON")

    header = list(data[0].keys())
    with csv_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        for row in data:
            writer.writerow({k: row.get(k, "") for k in header})

def csv_to_json(csv_path, json_path):
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.exists():
        raise FileNotFoundError("Файл не найден")

    if json_file.suffix.lower() != ".json":
        raise ValueError("Неверный формат файла")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError("Неверный формат файла")


    with csv_file.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV не содержит заголовок")
        data = [row for row in reader]
    if not data:
        raise ValueError("Пустой CSV")

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print(json_to_csv('C:\\Users\\Hp\\Desktop\\IDZ-25-6\\data\\samples\\people.json','C:\\Users\\Hp\\Desktop\\IDZ-25-6\\data\\out\\people_from_json.csv'))
print(csv_to_json('C:\\Users\\Hp\\Desktop\\IDZ-25-6\\data\\samples\\people.csv','C:\\Users\\Hp\\Desktop\\IDZ-25-6\\data\\out\\people_from_csv.json'))