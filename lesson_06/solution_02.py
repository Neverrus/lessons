"""
В школе решили набрать три новых класса по программированию.
Так как занятия по у них проходят в одно и то же время, было решено выделить кабинет для каждого класса и купить в них новые парты.
За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на всех учеников? Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
"""

def class_func(class_1, class_2, class_3, desk):
    cabinet_1 = (class_1 // desk)
    cabinet_2 = (class_2 // desk)
    cabinet_3 = (class_3 // desk)
    all_desk = (cabinet_1 + cabinet_2 + cabinet_3)
    print(all_desk)
    return
class_func(class_1=28,class_2=31,class_3=29,desk=2)










"""
def class_func(class_1, class_2, class_3):
    cabinet_1 = (class_1 // 2)
    cabinet_2 = (class_2 // 2)
    cabinet_3 = (class_3 // 2)
    all_desk = (cabinet_1 + cabinet_2 + cabinet_3)
    print(all_desk)
    return
class_func(class_1=input("Class 1 size: "),class_2=input("Class 2 size: "),class_3=input("Class 3 size: "))
"""
