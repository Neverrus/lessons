"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""


import sqlite3


def create_product_table():                              #Создаем таблицу продуктов
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


def create_product(name: str, price: str, amount: str, comments: str):        #Создаем продукты
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


def read_product():                #Чтение из базы
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


def update_product():        #Обновляем продукт по id
    with sqlite3.connect("product.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            UPDATE user
            SET name = ?
            WHERE id = ?;
            """,
        )
        session.commit()


def delete_product():        #Удаляем продукт по id
    with sqlite3.connect("product.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM user
            WHERE id = ?;
            """,
        )
        session.commit()

if __name__ == "__main__":
    result = read_product()
    print(result)