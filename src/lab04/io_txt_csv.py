import csv
from pathlib import Path

from src.lib.text import normalize
from src.lib.text import tokenize


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError("Файл не найден")
    try:
        with open(path, "r", newline="", encoding=encoding) as file:
            in_file = str(file.read())
        return normalize(in_file)
    except UnicodeDecodeError:
        print("неверная кодировка")


def write_csv(
    rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    p = Path(path)
    rows_list = list(rows)
    if rows_list:
        row_length = len(rows_list[0])
        for row in rows_list:
            if len(row) != row_length:
                raise ValueError(
                    f"Все строки должны иметь одинаковое количество элементов"
                )

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        for row in rows_list:
            writer.writerow(row)


if __name__ == "__main__":
    try:
        txt = read_text("text.test")
        print(f"Прочитано: {txt}")
    except FileNotFoundError:
        print("Файл text.test не найден")
    t = len(tokenize(txt))
    write_csv([("word", "count"), ("test", t)], "table.csv")
    print("файл csv создан!")
