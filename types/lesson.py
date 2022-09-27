# Инкремент - увеличение значеия какой-либо переменной. Пример а = 1 (а += 1 -> a = a+1)
# a = 0
# a +=1
# print(a)


# Дикремент - уменьшение значения какой-либо переменной. (a -= 1)
# a = 0
# a -= 1
# print(a)


# a = 1
# a *= 9
# print(a)

# a = 8
# a /= 2
# print(int(a))

# id()
# a = 1
# b = 3
# print(id(a))
# print(id(b))


# var = int(input("Введите число: "))



# a = int(input('Введите 1 число: '))
# b = int(input('Введите 2 число: '))
# print(a ** b)


# Модуль random - предоставляет функции для генерации случайных чисел, букв, символов и тд.

# import random
# # print(dir(random))
# num = random.randint(0, 100)
# print(num)

# from random import choice
# import string
# # print(string.ascii_letters)
# a = choice(string.ascii_letters)
# print(a)



# from math import pi
# r = int(input('Введите радиус: '))
# p = 2 * pi * r
# s = pi * (r ** 2)
# print("Периметр окружности: ", round(p), "\nПлощадь окружности: ",  round(s))