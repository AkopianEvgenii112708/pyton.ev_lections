# методы строк
# print(dir(str))

# |||||||||||||||||||||||
# replace(old, new, [count]) - меняем в строке old на new значение, если вы укажите count, то он заменит его ровно count раз.

# text = 'ha ha ha ha'
# result = text.replace('a', 'i', 2)
# print(text)
# print(f'result after replace: {result}')

# str1 = 'Hello world! My name is John Snow'
# res = str1.replace('John Snow', 'Jamie Lanister')
# print(res)



# |||||||||||||||||||||||
# print(id('H'))
# print(id('h'))



# ||||||||||||||||||||||||
# strip() - убирает пробельные символы в начале и в конце строки
# rstrip, lstrip - right, left

# text = input('Enter the text: ')
# print(text)
# res = text.strip()
# print(res)



# ||||||||||||||||||||||||||

# isdigit ->              Проверяет
# isnumeric -> ->  состоит ли наша строка 
# isdecimal ->        полностью из чисел


# text = '572777'
# if text.isdigit():
#     num = int(text)
#     print(num)
# else:
#     print('Oops!Invalid symbuls')





# ||||||||||||||||||||||||||

# isalnum() - проверяет, состоит-ли наша строка из чисел и символов латинского алфавита и киррилицы

# str1 = '56a'
# print(str1.isalnum())
# str2 = '56_a'
# print(str2.isalnum())


# ||||||||||||||||||||||||||||
# isalpha() - состоит ли наша строка только из символов латинского и киррильского алфавита

# rec1 = 'fubллп'
# print(rec1.isalpha())


# |||||||||||||||||||||||||||||

# islower() - проверяет на нижний регистр
# isupper() - проверяет на верхний регистр
# istitle() - проверяет первый символ каждого слова на заглавный регистр








# index(value, [start], [end]) - выводит индекс значения value которое мы передаем в нашей строке.

# test = 'Hello guyH'
# print(test.index('guy'))
# print(test[6:])
# print(test.index('g', 5))

# ss = test.index('H')
# print(ss)
# ss = test.index('H', ss+1)
# print(ss)






# |||||||||||||||||||||||||||||||||||||||

# count(value, [start], [end]) - считает сколько символов value содержится в строке 

# text = 'helloooooooo'
# print(text.count('o'))
# print(text.count('l'))
# print(text.count(' '))

# text = 'Hello world! We are looking for number ooo'
# text = input('Enter the text: ')
# i = 0
# res = -1
# while i < text.count('o'):
#     res = text.index('o', res+1)
#     print(res)
#     i += 1 # инкремент





# ||||||||||||||||||||||||||||||||
# find(value, [start], [end]) - делает то же самое что и метод index, но есть 1 отличие, если value нету в строке, то возвращается -1.

# text = 'Hello'
# print(text.find('l'))
# print(text.find('hi'))



# |||||||||||||||||||||||||||||||||||

# swapcase() - переводит все символы в противоположный регистр 
# upper() - переводит все символы в верхний регистр 
# lower() - переводит все символы в нижний регистр

# text = 'HelLo WorlD'
# print(text)
# print(text.swapcase())
# print(text.upper())
# print(text.lower())





# |||||||||||||||||||||||||||||||||||
# capitalize() - переводит первый символ в верхний регистр

# name = input('Enter your name: ').capitalize()
# print(f'Nice to meet you {name}')




# ||||||||||||||||||||||||||||||||||||
# title() - переводит первые символы всех слов в верхний регистр 

# name = input("enter your name: ").title()
# print(f'Hello {name}')


# ||||||||||||||||||||||||||||||||||||
# split(разделитель) - он дробит строку по разделителю на несколько частей, который находится в строке, все части строки сохраняются в тип данных list

# text = 'Let me speak all that i want to! Because we are free!'
# ls = text.split(" ")
# print(ls)
# # print(len(ls))



# # 'разделитель'.join(iterable(list)) - соединяет строки которые находятся в list по разделтелю.
# res = ' '.join(ls)
# print(res)
