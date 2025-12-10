
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е')

    if '\t' in text or '\r' in text or '\n' in text:
        text = text.replace('\t', ' ')
        text = text.replace('\r', ' ')
        text = text.replace('\n', ' ')

    s = text.split()
    itog = ''
    for i in s:
        itog = itog + ' ' + str(i)

    itog = itog.strip()

    return itog

def tokenize(text: str):
    text = normalize(text)

    pct_to_rplc = [',', '.', '!', '?', ';', ':', '(', ')', '[', ']', '{', '}', '"', "'"]

    for rep in pct_to_rplc:
        text = text.replace(rep, ' ')

    text_split = text.split()

    itog = list()

    for el in text_split:
        ok = 1
        for smbl in el:
            if smbl.isalnum():
                ok = 1
            else:
                ok = 0

        if ok == 1:
            itog = itog + [el]


    return itog

def count_freq(tokens: list[str]):
    uniq = list(set(tokens))

    l = list()

    for el in uniq:
        kort = (el, tokens.count(el))
        l = l + [kort]

    d = dict(l)

    return d

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if type(freq) is not dict:
        raise TypeError("Нужны словари")
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]







#print(normalize("ПрИвЕт\nМИр\t"))
#print(normalize("ёжик, Ёлка"))
#print(normalize("Hello\r\nWorld"))
#print(normalize("  двойные   пробелы  "))
#print('_______________')
#print(tokenize("привет мир"))
#print(tokenize("hello,world!!!"))
#print(tokenize("по-настоящему круто"))
#print(tokenize("2025 год"))
#print(tokenize("emoji 😀 не слово"))
#print('_______________')
#print(count_freq(["a","b","a","c","b","a"]))
#print(count_freq(["bb","aa","bb","aa","cc"]))
#print('_______________')
#print(top_n(count_freq(["a","b","a","c","b","a"]), 2))
#print(top_n(count_freq(["bb","aa","bb","aa","cc"]), 2))
print(top_n(count_freq(["яблоко","апельсин","банан"])))
