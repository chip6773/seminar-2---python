# for (int i = 0; i <= 5; i++) i = i + 1 <-> i += 1
# ++i <-> i++
# for element in True, False, 2, 1.345, "Hello, World!":
#     print(element)

# for i in range(5):
#     print(i)

# print(*range(5))

# # range(begin=0, end=обязательно, step=+1)

# print(*range(2, 7, 2))
# print(*range(12, -1, -3))

# # foreach <-> for(python)

# n = 10
# while n > 0:
#     print(n, end=' ') # end - вывод в строчку
#     n -= 1  # n = n - 1

# print()

## \n - переход на новую строчку
## \t - переход на новую строчку

# task 9 - факториал
# n = int(input("Введите число: ")) 
# result = 1
# while n > 1:
#     print(result, '*', n)
#     result *= n
#     n -= 1
# print(result)


# task 11 - числа фибоначчи

# n = int(input("Введите число: "))
# n0 = 0
# n1 = 0
# n2 = 1
# i = 2 # Так как 2 первых числа уже известны это 0 и 1
# while n0 < n:
#     n0 = n1 + n2
#     n1 = n2
#     n2 = n0
#     i += 1
#     if n0 > n:
#         i = 0
# if i != 0:
#     print(i)
# else:
#     print(-1)


# Task 15 - лёгкий и тяжёлый арбуз
# n = int(input("Введите кол-во арбузов: "))
# x = int(input("Введите массу арбуза: "))
# min_massa = x
# max_massa = x
# for i in range(n - 1):
#     x = int(input("Введите массу арбуза: "))
#     if min_massa > x:
#         min_massa = x
#     elif max_massa < x:
#         max_massa = x
# print(min_massa, max_massa)


# Task 13 - ищем числа больше 0
n = int(input("Введите кол-во дней: "))
days_plus = 0
max_days_plus = 0
for i in range(n):
    temp = int(input("Введите температуру: "))
    if temp > 0:
        days_plus += 1
        if max_days_plus < days_plus:
            max_days_plus = days_plus
    else:
        days_plus = 0
print(max_days_plus)