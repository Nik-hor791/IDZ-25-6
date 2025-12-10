def format_record(rec):
    if len(rec) != 3:  # Проверка: колличество элементов
        return "ValueError"
    if (
        type(rec[0]) != str or type(rec[1]) != str or type(rec[2]) != float
    ):  # Проверка: тип элементов
        return "TypeError"

    Name_split = rec[0].split()
    vivod = Name_split[0].title() + " " + Name_split[1][0].upper() + "."

    if len(Name_split) == 3:
        vivod += Name_split[2][0] + "., "
    else:
        vivod += ", "

    vivod += "гр. " + rec[1] + ", GPA " + f"{round(rec[2],2):.2f}"
    return vivod


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record((" сидорова анна сергеевна ", "ABB-01", 3.999)))
