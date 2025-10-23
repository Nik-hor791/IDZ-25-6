from src.lib.text import normalize
from src.lib.text import tokenize

import csv
from pathlib import Path
from typing import Iterable, Sequence
from collections import Counter

path = "src\data\lab04\input.txt"

def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    file = open(path).read()

    return file

print(read_text(path))