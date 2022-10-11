# import random

# ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Oromo']

# p = 0
# m = 0
# k = 0
# l = 0
# o = 0

# for x in range(0, 1000000):
#     # print(x)
#     choice = random.choice(ls)
#     if choice == 'Plov':
#         p += 1
#     elif choice == 'Manty':
#         m += 1
#     elif choice == 'Kuurdak':
#         k += 1
#     elif choice == 'Lagman':
#         l += 1
#     else:
#         o +=1

# if p > m and p > k and p > l and p > o:
#     print(f'Plov: {p}')
# elif m > k and m > l and m > o:
#     print(f'Manty: {m}')
# elif k > l and k > o:
#     print(f'Kuurdak: {k}')
# elif l > o:
#     print(f'Lagman: {l}')
# else:
#     print(f'Oromo: {o}')


# print(max(p, m, k, l, o))