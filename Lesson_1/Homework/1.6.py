#Задача 6: Вы пользуетесь общественным транспортом? 
#Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, 
#где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
#Вам требуется написать программу, которая проверяет счастливость билета.

ticket=int(input("Введите номер билета(шестизначный): "))
Lside= ticket//1000
LRes = Lside//100 + Lside%10 + int(Lside/10)%10
Rside= ticket%1000
RRes = Rside//100 + Rside%10 + int(Rside/10)%10
if RRes==LRes:
    print("Билет счастливый!")
else:
    print("Не повезло :(")