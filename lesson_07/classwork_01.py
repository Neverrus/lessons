"""
Известно, что на шахматной доске 8×8 можно расставить ферзей так, чтобы они не били друг друга (ферзь может ходить по горизонтали, вертикали и диагонали). Вам дана расстановка двух ферзей на доске, определите могут ли ферзи бить друг друга. Программа получает на вход две пары чисел, первое число в паре - координата по горизонтали, второе - координата по вертикали. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.
"""



def check_coords(x1: int, y1: int, x2: int, y2: int) -> bool:
    return x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)

if __name__ == "__main__":
    x1 = int(input("Enter X1:"))
    y1 = int(input("Enter Y2:"))


    x2 = int(input("Enter X2:"))
    y2 = int(input("Enter Y2:"))

    if check_coords(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")

"""
if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 -y2)
    return True
return False

    if x1 == x2:
        return True
    if y1 == y2:
        return True
    if abs(x1 - x2) == abs(y1 - y2):
        return True
    return False
"""
