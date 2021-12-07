"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5),
стоп (сброс скорости на 0), отображение скорости, задний ход (изменение знака скорости).
"""

class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def speed_up(self):
        self.speed += 5

    def speed_down(self):
        self.speed -= 5

    def stop(self):
        self.speed *= 0

    def show_speed(self):
        print(self.speed)

    def reverse(self):
        self.speed *= -1

if __name__ == "__main__":
    bmw_car = Car("BMW","E34", 1991, 0)
    bmw_car.speed_up()
    bmw_car.show_speed()
    bmw_car.reverse()
    bmw_car.show_speed()