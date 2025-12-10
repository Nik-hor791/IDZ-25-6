from src.lib.text import *

t = "Привет, мир! Привет!!!"

print("Всего слов:", len(tokenize(t)))
print("Уникальных слов:", len(count_freq(tokenize(t))))
print("Топ-5:")

for top_num in range(0, len(count_freq(tokenize(t)))):
    print(
        top_n(count_freq(tokenize(t)), 5)[top_num][0],
        ": ",
        top_n(count_freq(tokenize(t)), 5)[top_num][1],
        sep="",
    )
