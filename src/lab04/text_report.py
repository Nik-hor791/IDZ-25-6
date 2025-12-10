import sys, os, csv
from collections import Counter

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

try:
    from src.lib.text import normalize, tokenize
except ImportError as e:
    sys.exit(f"Ошибка импорта: {e}")


def main():
    input_file = "C:\\Users\\Hp\\Desktop\\IDZ-25-6\\src\\lab04\\text.test"
    output_file = "src\\lab04\\table.csv"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
        if not text.strip():
            sys.exit("Файл пустой")
    except Exception as e:
        sys.exit(f"Ошибка чтения {input_file}: {e}")

    try:
        normalized = normalize(text)
        words = tokenize(normalized)
        if not words:
            sys.exit("После обработки слов не найдено")
        word_freq = Counter(words)
    except Exception as e:
        sys.exit(f"Ошибка обработки текста: {e}")

    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["word", "count"])
            for word, count in sorted(word_freq.items(), key=lambda x: (-x[1], x[0])):
                writer.writerow([word, count])
    except Exception as e:
        sys.exit(f"Ошибка сохранения {output_file}: {e}")

    top5 = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))[:5]
    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(word_freq)}")
    print("Топ 5:")
    k = 0
    print(f'{"слово:":^15} |{"частота":^15}')
    print(f"{'----------' * 3:^30}")
    for word, counts in top5:
        if k == 5:
            break
        k += 1
        print(f"{word:^15} |{counts:^15}")


if __name__ == "__main__":
    main()
