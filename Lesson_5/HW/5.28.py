def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)

a=int(input("Введите число A: "))
b=int(input("Введите число B: "))
print(summa(a,b))