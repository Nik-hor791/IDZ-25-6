N = input ("ФИО:")
I = N.split()
initial=""
ll=2
for i in range(0,3):
    initial = initial + I[i][0]
    ll = len(I[i]) + ll
print("Инициалы:",initial.upper())
print("Длина (символов):",ll)