# dict() - Словарь -- упорядоченная коллекция элементов. (python3.7 -> ordered)
# каждый элемент в словаре хранится в виде пары: {ключ: значение}

# ассоциативный массив, hash tables, object, stucture == dictionary

# ключами могут выступать только неизменяемые типы данных и в словаре хранятся уникальные ключи. 
# Тогда как значениями могут выступать любые типы данных 

# {'name':'John Snow','age': 18,'number': 555667788}


# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967
# }

# print(thisdict)
# # print(type(thisdict))
# print(thisdict['model'])
# print(thisdict['year'])




# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# a = dict() / a = {} - создание пустого dictionary


# ls = [('key1', 'value1'), ('key2', 'value2') ]
# dict_ = dict(ls)
# print(dict_)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# print(dir(dict))

# items, keys, values

# user_info = {
#     'FirstName': 'John',
#     'LastName': 'Snow',
#     'Age': 24,
#     'email': 'Johnsnow123@mail.ru',
#     'role': 'Admin',
# }

# print(user_info.items())
# print()
# print(user_info.keys())
# print()
# print(user_info.values())

# for value in user_info.values():
#     print(value)

# print()
# print(user_info)
# print()
# for key, value in user_info.items():
#     print(f'key: {key}, value: {value}')


# ls = list(user_info.items())
# print(ls[0][1])

# # Изменения элементов в словаре
# dict_ = {'name': 'Jack', 'age': 24}

# # print(dict_['name'])
# # a = 5
# # print(a)
# # a = 7
# # print(a)
# # dict_['name'] = 'John'
# # dict_['adres'] = 'WinterFell'
# # print(dict_)


# dict_.update({'name': 'John', 'adres': 'WinterFell'})
# print(dict_)


# Создание - fromkeys
# dict_ = {}
# ls = list(range(1, 101))
# new_dict = dict_.fromkeys(ls, 'value')
# print(new_dict)






# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# get
# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.get(2))
# print(dict_[2])


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# setdefault - работает также как и get, но если нет такого ключа, то он создает новую пару значений из этого ключа.

# dict_ = {'name': 'Eddard', 'last-name': 'Stark', 'age': 28}
# print(dict_)
# print(dict_.setdefault('age', 38))
# print(dict_)


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Удаление элементов
# pop, popitem

# pop(<key>) - удаляет пару по ключу

# dict_ = {'name': 'John', 'LastName': 'Snow'}

# removed = dict_.pop('adres', 'Такого ключа нет!')
# print(dict_)
# print(removed)


# popitem() - удаляет последнюю пару
# dict_ = {'name': 'John', 'LastName': 'Snow'}
# removed = dict_.popitem()
# print(dict_)
# print(removed)




