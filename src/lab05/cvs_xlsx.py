from pathlib import Path
import csv
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использует openpyxl. Автоматическая ширина колонок.
    """
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)
    if csv_file.suffix.lower() != ".csv":
        raise ValueError("Неверный формат входного файла: ожидается .csv")
    if xlsx_file.suffix.lower() != ".xlsx":
        raise ValueError("Неверный формат выходного файла: ожидается .xlsx")
    if not csv_file.exists():
        raise FileNotFoundError("Файл не найден")

    with csv_file.open(encoding="utf-8") as f:
        reader = list(csv.reader(f, delimiter="\t"))
        if not reader:
            raise ValueError("Пустой файл")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in reader:
        ws.append(row)

    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            value = str(cell.value) if cell.value is not None else ""
            if len(value) > max_length:
                max_length = len(value)
        adjusted_width = max(max_length + 2, 8)
        ws.column_dimensions[column].width = adjusted_width

    wb.save(xlsx_file)


print(
    csv_to_xlsx(
        "C:\\Users\\Hp\\Desktop\\IDZ-25-6\\data\\samples\\people.csv",
        "C:\\Users\\Hp\\Desktop\\IDZ-25-6\\data\\out\\people.xlsx",
    )
)
