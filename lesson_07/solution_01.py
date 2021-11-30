"""
Используя условие первой задачи из урока, проверить то же самое только для коней.
"""

def check_coords(x1: int, y1: int, x2: int, y2: int) -> bool:
    return abs(x1 - x2) == 1 and abs(y1 - y2) == 2 or abs(x1 - x2) == 2 and abs(y1 - y2) == 1

if __name__ == "__main__":
    x1 = int(input("Enter X1: "))
    y1 = int(input("Enter Y1: "))

    x2 = int(input("Enter X2: "))
    y2 = int(input("Enter Y2: "))

    if check_coords(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")