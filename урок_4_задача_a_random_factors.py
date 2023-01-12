'''
Задана натуральная степень k. Сформировать случайным образом список коэффициентов
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
если k = 2, то многочлены могут быть =>
2*x² + 4*x + 5 = 0
или x² + 5 = 0
или 10*x² = 0
'''

import random

def create_polynom(k):
    factor_list = [random_int() for i in range(k+1)]
    return factor_list

def random_int():
    return random.randint(0, 100)



def file_log(st):
    with open('poly_log.txt', 'w') as data:
        data.write(st)


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


k = int(input("Введите натуральную степень многочлена k = "))
factor = create_polynom(k)
# factor = [1,2,3,4,5,0,0,8,9]
file_log(create_str(factor))

print(f'Создан список случайных целых коэффициэнтов многочлена,\n\
слева направо в порядке возрастания степени, от 0 до {k}:\n', factor)
