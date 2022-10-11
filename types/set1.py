# # set - Множества в python - контейнер который содержит в себе уникальные элементы в не упорядоченном виде 

# # {} !!!

# # a = {1: 'a'} -> словарь
# # a = {1, 2, 3} -> множество


# # set1 = {8, 1, 2, 3, 4, 5, 6, 6, 6, 6, 7, 7, 7, 6}

# # print(set1)
# # print(type(set1))


# # * [*] {*} - оператор распаковки из list in set и наоборот

# # ls = [1, 2, 'a', 0, False, True, 'n', 'b']
# # str1 = 'My name is John Snow!'

# # ls.extend(str1)
# # # print(ls)
# # # res = set(ls)
# # # print(res)

# # # ls1 = list(res)
# # # print(ls1)

# # print(ls)
# # set1 = {*ls}
# # res = [*set1]
# # print()
# # print(set1)
# # print(type(set1))
# # print()
# # print(res)
# # print(type(res))
# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# # pop() - удаляет и возвращает первый элемент множества

# #  FIFO (First in, first out), LIFO (Last in, first out)
# # a = {1, 2, 3, 4, 5}
# # print(a)
# # a.pop()
# # print(a)




# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# # remove / discard -> удаление елемента

# # remove - error
# # discard - None
# # set_ = {1, 2, 3, 4, 5, 6, 7}
# # print(set_.discard(4))


# # set_.remove(9)
# # print(set_)

# # # frozenset
# # a = {1, 2, 3, 4, 5}
# # f_set = frozenset([1, 2, 3, 4, 5])
# # print(type(a))
# # print(type(f_set))
# # print(a)
# # print(f_set)
# # print(dir(f_set))

# # a = set('qwerty')
# # b = frozenset('qwerty')
# # a.add(1)
# # print(a)
# # Ошибка!!!
# # b.add(1)
# # print(b)



# # ----------------------------------------------------------

# # Составьте код которая принимает номер месяца вашего рождения и в зависимости от сезона печатает на выходе следующее:
# # «Вы родились в <НАЗВАНИЕ_МЕСЯЦА>. <ОПИСАНИЕ_СОБЫТИЙ>».

# # В качестве ОПИСАНИЯ_СОБЫТИЙ будет характеристика сезона: 
# # - для зимы «За окном падал белый снег»,
# # - для весны «Птицы пели прекрасные песни»,
# # - для лета «Солнце светило ярче чем когда-либо»,
# # - для осени «Урожай был невероятным».

# # Важно учесть, что пользователи могут ввести любой тип данных в качестве аргумента 
# # (не попадитесь на этом и предупредите о том, что «Требуется ввести реальный номер месяца»).


# month = {
#     1: 'January',
#     2: 'February',
#     3: 'March',
#     4: 'April',
#     5: 'May',
#     6: 'June',
#     7: 'Jule',
#     8: 'August',
#     9: 'September',
#     10: 'Oktober',
#     11: 'November',
#     12: 'December'
# }

# while True:
#     number = input('Введите номер месяца в котором Вы родились(от 1 до 12): ')
#     if number == 'John':
#         break

#     if not number.isdigit():
#         print('Требуется ввести реальный номер месяца!')
#         continue

#     number = int(number)

#     if number not in range(1, 13):
#         print('Требуется ввести реальный номер месяца!')
#         continue

#     if number in range(3, 6):
#         print(f'Вы родились в {month[number]}. Птицы пели прекрасные песни.')
#     elif number in range(6, 9):
#         print(f'Вы родились в {month[number]}. Солнце светило ярче чем когда-либо.')
#     elif number in range(9, 12):
#         print(f'Вы родились в {month[number]}. Урожай был невероятным.')
#     else:
#         print(f'Вы родились в {month[number]}. За окном падал белый снег.')


















