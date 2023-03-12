n=int(input("Введите число монеток: "))
count_reshka=0
count_gerb=0
for i in range(n):
    x = int(input("Введите сторону монеты, 0 = решке, 1 = гербу: "))
    if x == 0:
        count_reshka+= 1
    else:
        count_gerb += 1
if count_reshka > count_gerb:
    print(f'Необходимо перевернуть {count_gerb} монет')
else:
    print(f'Необходимо перевернуть {count_reshka} монет')