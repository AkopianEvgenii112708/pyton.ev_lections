# /// TASK3 \\\
# Запросите у пользователей 5 раз их имя и фамилию, но в списке сохраните лишь фамилию, также учтите, что
# у человека ФИО может состоять не только из 2 слов. При выводе должен выходить отсортированный
# в алфавитном порядке список

# Наример:
# Name: Maya Angelou
# Name: Chimamanda Ngozi Adichie
# Name: Tobias Wolff
# Name: Sherman Alexie
# Name: Jane Austen
# Результат:
# ['Adichie', 'Alexie', 'Angelou', 'Austen', 'Wolff']

# names = []
# for x in range(0, 5):
#     name = input('Vvedite imia: ')
#     names.append(name)
# result = []
# for x in names:
#     x = x.split(' ')
#     result.append(x[-1])
# result.sort()
# print(result)


# range(start, stop, [step]) - возвращает последовательность из целых чисел,
# начиная с start до stop, возвращает итеррируемый тип данных range

# x = range(1, 11)
# print(list(x))
# for num in x:
#     print(num)
# n = 1
# for t in range(1, 10):
#     n = n * t
# print(n)


list5 = []
list1 = ['HelloWorld!']
ln = len(list1)
if ln % 2 == 0:
    for x in list1:
        list5.append(list1[ln // 2:])
        list5.append(list1[:ln // 2])
else:
    list5.append(list1[round(ln // 2):])
    list5.append(list1[:round((ln // 2)) + 0.5])

print(list5)



# /// TASK8 \\\
# Вам дан список, напишите код, который будет соединять в новый список элементы по n-ному шагу
# Например:
# n = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Результат:
# [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]




# n = 3
# list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# list1 = []
# list2 = []
# list3 = []

# for x in range(0, len(list_), n):
#     list1.append(list_[x])
#     list2.append(list_[x+1])
#     if x + 2 >= len(list_):
#         break
#     list3.append(list_[x+2])
# res = [list1, list2, list3]
# print(res)




# res = []
# for x in range(0, 3):
#     ls = []
#     for x in range(0, 3):
#         ls.append(0)
#     res.append(ls)
# print(res)


# list_ = [1, 2, 3]
# from itertools import permutations

# res = list(permutations(list_, 3))
# print(res)














