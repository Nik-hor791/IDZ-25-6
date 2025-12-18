import csv
from pathlib import Path


import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lab08.models import Student

HEADER = ["fio", "birthdate", "group", "gpa"]

class Group:
    """
    CSV-based student storage with CRUD operations.
    """

    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self._ensure_storage_exists()

    def _ensure_storage_exists(self) -> None:
        """Create CSV file with header if it does not exist."""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(HEADER)

    def _read_all(self):
        """Load all rows from CSV → list[Student]."""
        students = []
        with self.path.open("r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)

            if reader.fieldnames != HEADER:
                raise ValueError(
                    f"Invalid CSV header. Expected {HEADER}, got {reader.fieldnames}"
                )

            for row in reader:
                try:
                    students.append(
                        Student(
                            fio=row["fio"],
                            birthdate=row["birthdate"],
                            group=row["group"],
                            gpa=float(row["gpa"]),
                        )
                    )
                except Exception as e:
                    raise ValueError(f"Invalid row in CSV: {row}") from e

        return students

    def _write_all(self, students: list[Student]) -> None:
        """Rewrite CSV file with the given student list."""
        with self.path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADER)
            writer.writeheader()
            for st in students:
                writer.writerow(
                    {
                        "fio": st.fio,
                        "birthdate": st.birthdate,
                        "group": st.group,
                        "gpa": st.gpa,
                    }
                )

    # CRUD OPERATIONS
    def list(self) -> list[Student]:
        """Return all students."""
        return self._read_all()

    def add(self, student: Student) -> None:
        """Add a new student (no duplicates by FIO)."""
        students = self._read_all()

        if any(st.fio == student.fio for st in students):
            raise ValueError(f"Student already exists: {student.fio}")

        students.append(student)
        self._write_all(students)

    def find(self, substr: str):
        """Find students whose FIO contains the given substring."""
        substr = substr.lower()
        return [st for st in self._read_all() if substr in st.fio.lower()]

    def remove(self, fio: str) -> None:
        """Delete the student with the exact FIO."""
        students = self._read_all()
        new = [st for st in students if st.fio != fio]

        if len(new) == len(students):
            raise ValueError(f"No student with fio: {fio}")

        self._write_all(new)

    def update(self, fio: str, **fields) -> None:
        """
        Update fields of an existing student.
        Example:
            group.update("Ivanov Ivan", gpa=4.9, group="SE-01")
        """
        students = self._read_all()
        updated = False

        for st in students:
            if st.fio == fio:
                for key, value in fields.items():
                    if not hasattr(st, key):
                        raise ValueError(f"Unknown field: {key}")
                    setattr(st, key, value)
                updated = True
                break

        if not updated:
            raise ValueError(f"No student with fio: {fio}")

        self._write_all(students)
