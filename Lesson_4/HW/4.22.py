n=int(input("Введите количество элементов первого множества: "))
m=int(input("Введите количество элементов второго множества: "))
set1=set()
set2=set()

for i in range (n):
    set1.add(int(input(f"Введите {i} число множества n: ")))
for i in range (m):
    set2.add(int(input(f"Введите {i} число множества n: ")))
per=set1.intersection(set2)
result=list(per)
result.sort
for i in result:
    print(i, end=" ")