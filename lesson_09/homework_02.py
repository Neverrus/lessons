"""
Создать программу, которая импортирует класс из предыдущей задачи,
создает объект и при инициализации устанавливает марку Mercedes,
модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.
"""

from homework_01 import Car

if __name__ == "__main__":

    mercedes_car = Car("Mercedes", "E500", 2000, 0)
    speed_limit = 100
    while mercedes_car.speed < speed_limit:
        mercedes_car.speed_up()
    mercedes_car.show_speed()



