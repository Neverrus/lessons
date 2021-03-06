"""
Головоломка “Ханойские башни” состоит из трех стержней, пронумерованных числами 1, 2, 3. На стержень 1 надета пирамидка из n дисков различного диаметра в порядке возрастания диаметра. Диски можно перекладывать с одного стержня на другой строго по одному, при этом диск нельзя класть на диск меньшего диаметра. Необходимо переложить всю пирамидку со стержня 1 на стержень 3 за минимальное число перекладываний.
Необходимо написать программу, которая для данного числа дисков n печатает последовательность перекладываний, необходимую для решения головоломки.
"""

def move(n, start, finish):
    if n > 0:
        temp = 6 - start - finish
        move(n - 1, start, temp)
        print(f"Перенести диск {n} со стержня {start} на стержень {finish}")
        move(n - 1, temp, finish)


n = int(input("Введите количество дисков: "))
move(n, 1, 3)
