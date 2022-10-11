# list() -> Список, массив - изменяемый, последовательный тип данных, который представляет из себя коллекцию каких-либо объектов(значений)

# my_list = [1, 'string', False, None, [1, 2, 3]]
# print(my_list)
# print(type(my_list))

# range() - возвращает последовательность элементов (чисел)

# ls = list(range(1, 101))
# print(ls)
# print(type(ls))

# ls1 = list(range(0, 101, 2))
# print(ls1)


# ls = list(range(1, 101))
# for num in ls:
#     # print(num ** 2 if num % 2 == 0 else num ** 3)
#     if num % 2 == 0:
#         print(f'Число {num} четное, квадрат: {num ** 2}')
#     else:
#         print(f'Число {num} нечетное, куб: {num ** 3}')

# print('Finished for!')

# ----------------------------------------------------------------------------------------------------------------------------------------
# Методы списков:

# print(dir(list))


# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


# append(element) - Добавляет элемент в конец списка

# ls = [1, 3, 5]
# print(ls)
# ls.append(7)
# ls.append([9, 11, 13])
# print(ls)


# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


# extend(iterable) -> расширяет список элементами из iterable object

# ls = [1, 2, 3]
# ls.append('Hello')
# print(ls)
# ls.extend('Hello')
# print(ls)

# ls = [1, 2, 3]
# ls.append([4, 5, 6])
# print(ls)
# ls.extend([4, 5, 6])
# print(ls)


# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


# insert(<index>, element) -> добавляет элемент по указанному индексу

# ls = ['string', 2, 3, False]

# ls.insert(1, 4)
# ls.insert(15, [7, 6, 5])
# print(ls)


# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


# index(element, <start>, <end>) - возвращает индекс элемента в списке

# ls = ['Hello' , 'World', 'my', 'name', 'is', 'John']
# res = ls.index('my')
# print(ls[res])

# print(ls[0:2])
# print(ls[-1][0])


# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


# count(element) - возвращает количество вхождений element в списке

# ls = [1, 2, 5, 3, 4, 5, 5, 5, 5, 5, 6, 7]
# result = ls.count(5)
# print(result)

# ls = ['Hello' , 'World', 'my', 'name', 'is', 'John', 'North', 'King', 'qween', 'USA']
# str1 = input('Введите слово: ')
# if str1 in ls:
#     print(f'{str1} есть в списке и его индекс: {ls.index(str1)}')
# else:
#     print('No!')



# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


# # sort() - сортирует список, если в аргументах передать reverse=True, то список будет сортирован в обратном порядке
# import random

# ls = []
# for x in range(0, 50):
#     ls.append(random.randint(0, 1000))

# ls.sort()
# print(ls)

# ls = ['John', 'Deyneris', 'Tirion', 'apple', 'Aikol', 'Nuraim', 'makers']
# ls.sort(reverse=True, key=len)
# print(ls)



# \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/


# remove(element) - удаляет элемент из списка, если такого нет, выводится ошибка
# pop([index]) - удаляет и возвращает элемент по index, но если index не указан, то удаляет последний элемент

# ls = [2, 4, 7, 0, 4, 2, 4, 7, 2]
# while 2 in ls:
#     ls.remove(2)
# print(ls)

# ls = [2, 3, 4, 2, 5, 2, 4, 2]
# delited = ls.pop(0)
# print(ls)
# print(delited)

# print(ls.pop())
# print(ls)


# update -------------------------------------------

# ls = [1, 'h', 3]
# print(ls)
# ls[1] = 2
# print(ls)



# x = int(input())
# y = int(input())
# res = x // y
# if x % y == 0:
#     print('x делится на y')
#     print('Частное: ', res)
# else:
#     print('x не делится на y')
#     print('Частное:', res)
#     print('Остаток:', x % y)






    