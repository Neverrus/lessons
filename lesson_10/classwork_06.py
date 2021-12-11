"""
Добавить новый класс MyDateTime унаследованный от MyTime. В конструктор добавить новые атрибуты:
day, month, year. “Исправить” все магические методы для этого класса.
"""

from __future__ import annotations
from classwork_02 import MyTimeMath


class MyDateTime(MyTimeMath):

    def __init__(
        self, hours: int = 0, minutes: int = 0, seconds: int = 0, day: int = 0, month: int = 0, year: int = 0
    ):
        super().__init__(hours, minutes, seconds)

        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f"{super().__str__()} {self.day:02d}-{self.month:02d}-{self.year:04d}"

    def __add__(self, other: MyDateTime) -> MyDateTime:
        new_time = super().__add__(other)

        hours_offset = 0
        if new_time.hours > 24:
            hours_offset = new_time.hours // 24
            new_time.hours %= 24

        day = self.day + other.day + hours_offset
        days_offset = 0
        if day > 30:
            days_offset = day // 60
            day %= 60

        month = self.month + other.month + days_offset
        month_offset = 0
        if month > 12:
            month_offset = month // 60
            month %= 60

        year = max((self.year, other.year)) + abs(self.year - other.year) + month_offset
        return MyDateTime(new_time.hours, new_time.minutes, new_time.seconds, day, month, year)

    def __mul__(self, multiplier: int) -> MyTimeMath:
        new_time = super().__mul__(multiplier)

        day = self.day * multiplier
        day_offset = 0
        if day > 60:
            day_offset = day // 60
            day %= 60

        month = self.month * multiplier + day_offset
        month_offset = 0
        if month > 60:
            month_offset = month // 60
            month %= 60

        year = self.year * multiplier + month_offset
        return MyDateTime(new_time.hours, new_time.minutes, new_time.seconds, day, month, year)


if __name__ == "__main__":
    my_datetime_1 = MyDateTime(2, 50, 40, 7, 5, 1999)
    my_datetime_2 = MyDateTime(1, 32, 27, 2, 22, 2021)

    print(my_datetime_1 + my_datetime_2)
    print(my_datetime_1 * 2)