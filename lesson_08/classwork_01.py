"""
Дан список словарей. Каждый словарь описывает машину (серийный номер, цвет и год выпуска). Создать функцию, которая возвращает новый список со всеми машинами, год выпуска которых больше Х.
"""
"""
CAR_LIST = [
    {
        "serial": 123456,
        "color": "red",
        "year": 1999,
    },
    {
        "serial": 123456,
        "color": "black",
        "year": 1998,
    },
    {
        "serial": 1233836,
        "color": "white",
        "year": 2012,
    },
]

def filter_cars(year: int) -> list:
    result = []
    for car in CAR_LIST:
        if car["year"] < year:
            result.append(car)
    return result



if __name__ == "__main__":

"""

def filter_cars(car_list: list, year: int) -> list:
    result = []
    for car in car_list:
        if car["year"] < year:
            result.append(car)
    return result

if __name__ == "__main__":
    car_list = [
        {
            "serial": 123456,
            "color": "red",
            "year": 1999,
        },
        {
            "serial": 123456,
            "color": "black",
            "year": 1998,
        },
        {
            "serial": 1233836,
            "color": "white",
            "year": 2012,
        },
    ]

    year = int(input("Year: "))
    print(filter_cars(car_list, year))

    print(list(y for y in car_list if y["year"] < year))
    print(list(filter(lambda x: x["year"] < year, car_list)))