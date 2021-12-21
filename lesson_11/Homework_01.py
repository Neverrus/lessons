"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""


import sqlite3


def create_product_table():                              # Создаем таблицу продуктов
    with sqlite3.connect("product.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           CREATE TABLE user (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR,
               price VARCHAR,
               amount VARCHAR,
               comments VARCHAR
           );
           """,
       )
       session.commit()


def create_product(name: str, price: str, amount: str, comments: str):        # Создаем продукты
    with sqlite3.connect("product.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (name, price, amount, comments)
            VALUES (?, ?, ?, ?);
            """,
            (name, price, amount, comments),
        )
        session.commit()


def read_product():                # Чтение из базы
   with sqlite3.connect("product.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           SELECT *
           FROM user;
           """,
       )
       session.commit()
       return cursor.fetchall()


def update_product(query: str, query2: str):        # Обновляем продукт по id
    with sqlite3.connect("product.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            UPDATE user
            SET name = ?
            WHERE id = ?;
            """,
            (query, query2,),  # указываем количество аргументов для ввода
        )
        session.commit()


def delete_product(query: str):        # Удаляем продукт по id
    with sqlite3.connect("product.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM user
            WHERE id = ?;
            """,
            (query,),
        )
        session.commit()

if __name__ == "__main__":
    print("Заглушка")
"""
    delete_product(input("Введите ID: "))

    update_product(
                   input("Введите новое имя: "),
                   input("Введите ID: "),
                   )

    create_product(
                   input("Введите имя: "),
                   input("Введите цену: "),
                   input("Введите количество: "),
                   input("Введите комментарий: ")
                   )
"""
