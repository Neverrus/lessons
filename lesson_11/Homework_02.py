"""
Создать программу с пользовательским интерфейсом позволяющим выбирать определенную функцию и вводить необходимые данные.
"""


from Homework_01 import create_product
from Homework_01 import read_product
from Homework_01 import update_product
from Homework_01 import delete_product


if __name__ == "__main__":

    while True:  # Запускаем бесконечный цикл для интерфейса
        choice = input("Что вы желаете сделать? create/read/update/delete/exit\n")  # Создаем несколько вариантов
        if choice == "create":                                                      # действий
            create_product(
                input("Введите имя: "),
                input("Введите цену: "),
                input("Введите количество: "),
                input("Введите комментарий: ")
            )
            continue
        elif choice == "read":
            result = read_product()
            print(result)
            continue
        elif choice == "update":
            update_product(
                input("Введите новое имя: "),
                input("Введите ID: "),
            )
            continue
        elif choice == "delete":
            delete_product(input("Введите ID: "))
            continue
        elif choice == 'exit':
            break

    print("До свидания!")
