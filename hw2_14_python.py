# Задача 14:
# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

your_number = int(input("\nВаше число: "))
a = 0

for i in range(1, your_number+1):
    if 2**i <= your_number:
        a = 2**i
        print(a, end=' ')