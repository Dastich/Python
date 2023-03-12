n=list(map(int,input("Введите числа через пробел: ").split()))
x=int(input("Введите число, к которому будем искать ближайшее: "))
raz=x
for i in range (len(n)):
    if x-n[i] < raz:
        raz=x-n[i]
        result=n[i]
print(f"Ближайшее число к искомому = {result}")
