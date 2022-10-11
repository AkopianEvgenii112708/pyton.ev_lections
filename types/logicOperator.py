# оператор сравнения
# <, >, ==(равно), <=, >=, !=(не равно)

# 1 < 5 -> True
# 7>9 -> False


# num1 = 15
# num2 = 15
# print(num1 != num2)



# num1 = 20
# num2 = 17
# print(num1 >= num2)


# stroka1 = 'Hello'
# stroka2 = 'World'
# print(stroka1 > stroka2)
#       #104 #87
# print ('hello world')     


# print (ord('H'))
# print (ord('a'))

# print(chr(1050), chr(973))
# print (ord('N'))


# stroka1 = 'hello!'
# stroka2 = 'world'

# print (len(stroka1) >len (stroka2))


# Условные операторы

# if 
# elif
# else

# if <condition>:
#     <body if> # сработает если в выражение if придет true
# elif <condition>:
#     <body elif>
# [else]:
#     <body else> # Сработает если во всех вышестоящих условиях пришло False



# string = input('Enter smth: ')
# if string.lower() == 'hello':
#     print('Hello stranger')
# elif string.lower() == 'John':
#     print('Hello John Snow')
# elif string.lower() == 'PyHub':
#     print('Best group')
# else:
#     print('go away')





# email = input('Enter your email: ')
# password1 = input('Enter your password: ')

# if len(password1) < 8:
#     raise ValueError('Password is too short!')

# password2 = input('Enter the password information: ')

# if password2 != password1:
#     raise ValueError('Password is wrong!')
# else:
#     print('Successfully sined up!')

    


# age = input('Enter your age: ')
# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Invalid values!!') 

# if age < 18:
#     print(f'Access denied! Come again after {18 - age} years!')
# else:
#     print('You are welcome!')




# Логические операторы
# and - логическое и
# or - логическое или
# not - логическое отрицание

# my_age = 20
# your_age = 18

# result = my_age == 20 and your_age == 19
# print(result)

# result = my_age == 20 or your_age == 19
# print(result)

# result = not my_age == 20
# print(result)

# ||||||||||||||||||||||||||||||||||||||||||\

# user 'John'
# is_google_user = True
# is_github_user = False
# is_age_greater_21 = False
# user_coins = 9000

# if ()is_google_user or is_github_user) and (is_age_greater_21 or user_coins > 8000):


















# str1 = 'Hello world'
# print(str1)
# choice = input('Enter the symbol: ')

# if choice in str1:
#     print(f'The symbol {choice} exist')
# else:
#     print(f'The symbol {choice} doesnt exist')