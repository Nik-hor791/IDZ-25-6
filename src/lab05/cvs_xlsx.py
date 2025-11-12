from pathlib import Path
import csv
from openpyxl import Workbook

def csv_to_xlsx(csv_path, xlsx_path):
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)

    if csv_file.suffix.lower() != ".csv":
        raise ValueError("Неверный формат файла")
    if xlsx_file.suffix.lower() != ".xlsx":
        raise ValueError("Неверный формат файла")

    if not csv_file.exists():
        raise FileNotFoundError("Файл CSV не найден")
    if not xlsx_file.exists():
        raise FileNotFoundError("Файл XLSX не найден")

    with csv_file.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows or all(not any(row) for row in rows):
        raise ValueError("Пустой CSV или неподдерживаемая структура")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    for col in ws.columns:

        max_len = max(len(str(cell.value or "")) for cell in col)
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = max(max_len + 2, 8)

    wb.save(xlsx_file)

print(csv_to_xlsx('C:\\Users\\Hp\\Desktop\\IDZ-25-6\\data\\samples\\people.csv','C:\\Users\\Hp\\Desktop\\IDZ-25-6\\data\\out\\people.xlsx'))