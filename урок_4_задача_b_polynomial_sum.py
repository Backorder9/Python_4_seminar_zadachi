'''
Даны два файла, в каждом из которых находится запись многочлена.
Задача - сформировать файл, содержащий сумму многочленов.
'''

import random

# запись в файл


def file_log(name, st):
    with open(name, 'w') as data:
        data.write(st)

# создание случайного числа от 0 до 100


def random_int():
    return random.randint(0, 100)

# создание коэффициентов многочлена


def make_poly(k):
    lst = [random_int() for i in range(k+1)]
    return lst

# создание многочлена в виде строки


def create_str(lst):
    f_list = lst[::-1]
    poly = ''
    if len(f_list) < 1:
        poly = 'x = 0'
    else:
        for i in range(len(f_list)):
            if i != len(f_list) - 1 and f_list[i] != 0 and f_list[i] != 1 and i != len(f_list) - 2:
                poly += f'{f_list[i]}x^{len(f_list)-i-1}'
                if f_list[i+1] != 0:
                    poly += ' + '
            elif f_list[i] == 0 and f_list[i+1] != 0:
                poly += ' + '
            elif f_list[i] == 1 and i != len(f_list) - 1 and i != len(f_list) - 2:
                poly += f'x^{len(f_list)-i-1}'
                if f_list[i+1] != 0:
                    poly += ' + '
            elif i == len(f_list) - 2 and f_list[i] != 0:
                poly += f'{f_list[i]}x'
                if f_list[i+1] != 0:
                    poly += ' + '
            elif i == len(f_list) - 1 and f_list[i] != 0:
                poly += f'{f_list[i]} = 0'
            elif i == len(f_list) - 1 and f_list[i] == 0:
                poly += ' = 0'
    return poly

# получение степени многочлена


def poly_pwr(k):
    if 'x^' in k:
        i = k.find('^')
        num = int(k[i+1:])
    elif ('x' in k) and ('^' not in k):
        num = 1
    else:
        num = -1
    return num

# получение коэффицента члена многочлена


def k_mn(k):
    if 'x' in k:
        i = k.find('x')
        num = int(k[:i])
    return num

# разбор многочлена и получение его коэффициентов


def parse_poly(st):
    st = st[0].replace(' ', '').split('=')
    st = st[0].split('+')
    lst = []
    l = len(st)
    k = 0
    if poly_pwr(st[-1]) == -1:
        lst.append(int(st[-1]))
        l -= 1
        k = 1
    i = 1  # степень
    ii = l-1  # индекс
    while ii >= 0:
        if poly_pwr(st[ii]) != -1 and poly_pwr(st[ii]) == i:
            lst.append(k_mn(st[ii]))
            ii -= 1
            i += 1
        else:
            lst.append(0)
            i += 1

    return lst


# создание двух файлов
k1 = int(input("Введите натуральную степень для первого файла k = "))
k2 = int(input("Введите натуральную степень для второго файла k = "))
factor1 = make_poly(k1)
factor2 = make_poly(k2)
file_log("file_a.txt", create_str(factor1))
file_log("file_b.txt", create_str(factor2))

# нахождение суммы многочлена

with open('file_a.txt', 'r') as data:
    st1 = data.readlines()
with open('file_b.txt', 'r') as data:
    st2 = data.readlines()
print(f"Первый многочлен {st1}")
print(f"Второй многочлен {st2}")
lst1 = parse_poly(st1)
lst2 = parse_poly(st2)
ll = len(lst1)
if len(lst1) > len(lst2):
    ll = len(lst2)
lst_new = [lst1[i] + lst2[i] for i in range(ll)]
if len(lst1) > len(lst2):
    mm = len(lst1)
    for i in range(ll, mm):
        lst_new.append(lst1[i])
else:
    mm = len(lst2)
    for i in range(ll, mm):
        lst_new.append(lst2[i])
file_log('file_result.txt', create_str(lst_new))
with open('file_result.txt', 'r') as data:
    st3 = data.readlines()
print(f"Итоговый многочлен {st3}")