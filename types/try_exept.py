# Обработка исключений
# Операторы try...except

# print('Hello world!')

# Ошибки Errors -> связанные с кодом:
#     SyntaxError
#     IndentationError
#     TabError


# Исключения Exceptions -> связаны с неправильными данными которые передаются в код

# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# KeyError
# ValueError
# ImportError
# BaseException # создает свою ошибку

# try:
#     num = int(input('Enter the number: '))
#     print(num)
#     num2 = int(input('Enter the number 2: '))
#     print(num2)
#     print(num/num2)
# except:
#     print('No work') 
# print('very viel')

# try ... except

# try:
#     <body try>
# except:
#     <body except> сработает только если в <body try> ошибка
# else:
#     <body else> сработает если в операторе try нет ошибки
# finally:
#     <body finally>  сработает в любом случае
# try:
#     num1 = int(input('Enter the number: '))
# except:
#     print('Invalid values!')
# else:
#     print(num1)
#     print(num1 + 5)
# finally:
#     print('Code end!')

# --------------------------------------------------------------------------
# Отображение ошибки

# 1. import sys

# list_ = [1, 2, 3, 4, 5]

# index = int(input('Enter index: '))
# try:
#     res = list_[index]
#     print(res)
# except:
#     print(f'oops, we catched {sys.exc_info()[0]} error')


# 2. Exception as e / (error)

# ls = [1, 2, 3, 4, 5]

# while True:
#     try:
#         index = int(input('vvedite index: '))
#         print(ls[index])
#     except Exception as error:
#         print(f'oops, we catched {error.__class__} error!!!')


# try:
#     num1 = int(input('Enter number 1: '))
#     print(num1 / 0)
# except (ValueError, ZeroDivisionError):
#     print('You enterred incorrect values!!!')


# try:
#     num1 = int(input('Enter number 1: '))
#     print(num1 / 0)
# except ValueError:
#     print('Invalid values!!!')
# except ZeroDivisionError:
#     print('Devide by 0!') 


# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     res = num1 / num2
# except ZeroDivisionError:
#     print('You cant devide by 0!')
# except ValueError:
#     print('Invalid symbols!')
# else:
#     print(res)
# finally:
#     print('The end!!!')


# --------------------------------------------------------------------------------------/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

# from string import digits

# flag = True
# symbols = digits + '-' + '.'

# while flag:
#     num1 = input('Введите первое число: ')
#     num2 = input('Введите второе число: ')

#     try:
#         num1 = float(num1) if '.' in num1 else int(num1)
#         num2 = float(num2) if '.' in num2 else int(num2)
#     except ValueError:
#         print('Вы ввели неправильное число!')
#         continue
#     print(num1)
#     print(num2)
#     operator = input('Введите оператор(+, -, *, /): ')

#     if operator == '+':
#         print(f'Result: {num1 + num2}')
#     elif operator == '-':
#         print(f'Result: {round(num1 - num2, 2)}')
#     elif operator == '*':
#         print(f'Result: {num1 * num2}')
#     elif operator == '/':
#         if num2 == 0:
#             print('На 0 делить нельзя!')
#         else:
#             print(f'Result: {num1 / num2}')
#     else:
#         print('Вы ввели неправильный оператор!')

#     choice = input('Хотите остановить?(yes/no): ')
#     if choice.lower() == 'yes':
#         flag = False
#         print('Пока!')
    








