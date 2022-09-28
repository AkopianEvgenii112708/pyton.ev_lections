#  String - Строки
# "Hello"
# 'Hello'

# """ 
# Hello world!
# Nice to meet!
# """

# Строки - это набор последовательных символов, которые мы используем для хранения и предстваления текстовой информации.
# Набор методов и операций которые мы можем использовать с данными в виде текста.

# индексация в строке
# name = 'John'
# print(name[0])
# print(name[-1])




# str1 = 'birthday'
# print(str1[0:5])
# print(str1[5], str1[6], str1[7])


# Срезы по индексам
# [start: end: <step>]
# str1 = 'birthday'
# str2 = str1[0:5]
# print(str2)
# print(str1[0:5], str1[5:8])
# print(len(str1))

# len() - выдает колличество символов в строке

# print(str1[0:]) - выводит все что находится в строке

# print(str1[:5]) - Выводит все значения до 5 индекса

# text = 'Hello world! My name is John! i\'m North king!'
# print(text)
# print(len(text))
# print(text[:12])


# Конкатиннация строк (слияние, соединение)
# word1 = 'Hello'
# word2 = 'World'
# result = word1 + ' ' + word2 + '!'
# print(result)


# Форматирование строк
# 1. С помощью знака %
# 2. С помощью .format()
# 3. Интерполяция строк (f-строки)

# % 
# name = input('enter your name: ')
# last_name = input('enter your last name: ')
# print('Hello, my name is', name, last_name)
# print('Hello, my name is' + ' ' + name + ' ' + last_name)
# print('Hello, my name is %s %s' %(name, last_name))

# .format
# name = input('enter your name: ')
# last_name = input('enter your last name: ')
# print('Hello, my name is {} {}' .format(name, last_name))

# (f-строки)
# name = input('enter your name: ')
# last_name = input('enter your last name: ')
# print(f'Hello, my name is {name} {last_name} !!!')

# Экранирование строк - механизм при помощи которого можно вставлять символы, которые сложно ввести с клавиатуры в строку
# \n - перенос строки
# \t - горизонтальная табуляция
# \v - вертикальная табуляция 


# name = 'John\nSnow'
# lastName = '\vSnow'
# last_name = '\tSnow'
# print(name)
# print(lastName)
# print(last_name)




