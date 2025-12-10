price = int(input("Введите цену:"))
discount = int(input("Введите скидку:")) / 100
vat = int(input("Введите НДС:")) / 100

base = price * (1 - discount)
vat_amount = base * vat
total = base + vat_amount

print("База после скидки:", base)
print("НДС:", vat_amount)
print("Итого к оплате:", total)
