"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure. Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности), Triangle (атрибуты: три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и периметра). При потребности создавать все необходимые методы не описанные в задании.
"""

import math

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center_point, radius_point):
        self.center_point = center_point
        self.radius_point = radius_point
        self.radius_1 = self.radius()
        self.perimeter = self.radius_1 * 2 * math.pi
        self.area = self.radius_1 ** 2 * math.pi

    def radius(self):
        x1 = self.center_point.x
        y1 = self.center_point.y
        x2 = self.radius_point.x
        y2 = self.radius_point.y

        radius_1 = abs((x2 - x1) + (y2 - y1))
        return radius_1

class Triangle:
    def __init__(self, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.side_1_2 = self.sides()[0]
        self.side_2_3 = self.sides()[1]
        self.side_1_3 = self.sides()[2]
        self.perimeter = self.side_1_2 + self.side_2_3 + self.side_1_3
        self.area = self.side_1_2 * self.side_2_3 / 2

    def sides(self):
        x1 = self.point_1.x
        y1 = self.point_1.y
        x2 = self.point_2.x
        y2 = self.point_2.y
        x3 = self.point_3.x
        y3 = self.point_3.y

        side_1_2 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        side_2_3 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        side_1_3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        return side_1_2, side_2_3, side_1_3

class Square:
    def __init__(self, point_1, point_2):
        self.point_1 = point_1
        self.point_2 = point_2
        self.side_1 = self.sides()
        self.perimeter = self.side_1 * 4
        self.area = self.side_1 ** 2

    def sides(self):
        x1 = self.point_1.x
        y1 = self.point_1.y
        x2 = self.point_2.x
        y2 = self.point_2.y

        side_1 = abs((x2 - x1) + (y2 - y1))
        return side_1

"""
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
"""