"""
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
"""

from Homework_01 import Point
from Homework_01 import Circle
from Homework_01 import Triangle
from Homework_01 import Square

if __name__ == '__main__':

    center_point = Point(12, 2)
    radius_point = Point(21, 8)
    circle = Circle(center_point, radius_point)

    triangle_point_1 = Point(15, 28)
    triangle_point_2 = Point(72, 28)
    triangle_point_3 = Point(72, 50)
    triangle = Triangle(triangle_point_1, triangle_point_2, triangle_point_3)

    square_point_1 = Point(8, 14)
    square_point_2 = Point(8, 25)
    square = Square(square_point_1, square_point_2)

    figure_list = [circle, triangle, square]
    for figure_area in figure_list:
        if figure_area == figure_list[0]:
            print(f"Площадь круга: {figure_area.area}")
        elif figure_area == figure_list[1]:
            print(f"Площадь треугольника: {figure_area.area}")
        elif figure_area == figure_list[2]:
            print(f"Площадь квадрата: {figure_area.area}")