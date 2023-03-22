def mathpow(a,b):
    if b==1:
        return a
    if b!=1:
        return (a * mathpow(a ,b-1))
a=int(input("Введите число A: "))
b=int(input("Введите число B: "))
print(mathpow(a,b))