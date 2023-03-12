mul=int(input("Введите произведение чисел: "))
sum=int(input("Введите суммы чисел: "))
for i in range (mul):
    for y in range (sum):
        if i+y==sum and i*y==mul:
            print(f'Загаданные числа {i} и {y}')
            