n=list(map(int,input("Введите числа через пробел: ").split()))
print(n)
x=int(input("Введите число, которое будем искать: "))
counter=0
for i in range (len(n)):
    print(n[i])
    if n[i]==x:
        counter+=1
print(f"Количество совпадений равно {counter}")
    