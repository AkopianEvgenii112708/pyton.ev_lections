# Циклы - это конструкции, при помощи которых можно организовать многократное исполнение определенного кода
# 
# 
# while <expression>:
#   <body>
# else:
#   <body>  
#  


# i = 0
# while i <=10:
#     print(f'Цикл выполнился {i} раз!')
#     i += 1
# else:
#     print('Конец цикла!')

# print('Начало кода!')


# name1 = ''
# name2 = ''
# i = 0


# while name1.lower() != 'john' and name2.lower() != 'jamie':
#     name1 = input('Введите имя 1: ')
#     name2 = input('Введите имя 2: ')
#     i += 1
#     if i > 4:
#         print('Цикл остановлен')
#         break
# else:
#     print('Вы ввели правильное имя!')
# 




# admin = ['johnsnow23', 'ilovepython23']
# i = 3

# password = None
# username = None

# while username != admin[0] or password != admin[1]:
#     username = input('Введите username: ')
#     password = input('Введите password: ')
#     i -= 1
#     print('Неверный логин или пароль! Попробуйте снова!')
#     if i == 0:
#         print('Blocked for 5 min!!!')
#         break
# else: 
#     print(f'{admin[0]} Вы успешно зашли в систему!')



# --------------------------------------------------------------------------------
# for <variable> in <iterable object>:
#     <body>


# list_ = [0, 1, 2, 3, 4, 5]
# i = iter(list_)
# print(i)

# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# # print(next(i))

# # for x in list_:
# #     print(x) 



# # ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# # # for x in ls:
# # #     print(f'Element: {x}')


# # i = 0
# # while i < len(ls):
# #     print(f'Element: {ls[i]}')
# #     i += 1
 

# # --------------------------------------------------------

# # secret_list = ['DeltaViski', 'LORD123', 'JohnSnow']

# # word = input('Введите секретное слово: ')
# # while word not in secret_list:
# #     print('incorrect word! Try again!')
# #     word = input('Введите секретное слово: ')

# # print(f'You are welcome, {word}!')



# # ---------------------------------------------------------

# steps = 8
# path = 'UDDDUDUU'

# sea_level = 0
# valley = 0
# u = 'U'
# d = 'D'
# for x in path:
#     if x == u:
#         sea_level += 1
#     elif x == d:
#         sea_level -= 1
#     if x == u and sea_level == 0:
#         valley += 1
# print(valley)
# # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# steps = 8
# path = 'UDDDUDUU'

# sea_level = 0
# valley = 0
# u = 'U'
# d = 'D'
# for x in path:
#     if x == u:
#         sea_level += 1
#         if sea_level == 0:
#             valley += 1
#     elif x == d:
#         sea_level -= 1
# print(valley)

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
