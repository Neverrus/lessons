"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах. Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы, которая считывает название города и выводит на печать страну.
"""


def input_name():
    d = {}
    while True:
        l = input('Input format<country city city1>:').lstrip().rstrip().split()
        if not l:
            continue
        elif l[0] == '\B':
            break
        elif len(l) > 1:
            for city in l[1:]:
                if city in d:
                    raise TypeError('This city already exist: %s' % city)
                d[city] = l[0]
        else:
            print('This input is incorrect: %s' % l)
    return d


def search_ctr(d):
    while True:
        city = input('city').lstrip().rstrip()
        if city == '\B':
            break
        elif city in d:
            print('Country: %s, City: %s' % (d[city], city))
        else:
            print('This city not found: %s' % city)


dcity = input_name()
search_ctr(dcity)