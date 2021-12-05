"""
Дана последовательность натуральных чисел, завершающаяся числом 0. Определите, какое наибольшее число подряд идущих элементов этой последовательности равны друг другу и что это за элемент.
Т.е. если программе на вход подать последовательность [1, 2, 2, 3, 7, 4, 4, 4, 0, 5, 5, 5], то на печать программа должна вывести числа 4 и 3, где 4 - повторяющийся элемент, 3 - количество повторений
"""


element = -1
rep_length = 0
max_repeats = 0
list = int(input())
while list != 0:
    if element == list:
        rep_length += 1
    else:
        element = list
        max_repeats = max(max_repeats, rep_length)
        rep_length = 1
    list = int(input())
max_repeats = max(max_repeats, rep_length)

if __name__ == "__main__":
    print("Повторяющийся элемент:", element)
    print("Количество повторений:", max_repeats)