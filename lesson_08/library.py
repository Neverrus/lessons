
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

def prime_numbers(n: int, m: int) -> list:
    result = []
    my_count = 0
    for element in range(n, m + 1):
        # Проверяем текущий элемент, что он простое число
        # Для этого пробуем делить текущий элемент на все предыдущие по очереди
        is_prime = True
        for divider in range(2, element):
            # Если текущий элемент делится без остатка на текущий делитель
            # то этот элемент не является простым числом
            if divider > 1 and element % divider == 0:
                is_prime = False
                break
        # Текущий элемент - простое число
        if is_prime:
            result.append(element)
    return result