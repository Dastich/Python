number=int(input("Введите трехзначное число: "))
res= number//100 + number%10 + int(number/10)%10
print(res)