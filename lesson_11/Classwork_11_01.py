"""

"""

import sqlite3


def create_user_table():
    with sqlite3.connect("db.sqlite3") as session:
       cursor = session.cursor()
       cursor.execute(
           """
           CREATE TABLE user (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               firstname VARCHAR,
               lastname VARCHAR,
               email VARCHAR,
               password VARCHAR,
               age INTEGER,
               datetime DATETIME
           );
           """,
       )
       session.commit()


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age)
            VALUES (?, ?, ?, ?, ?);
            """,
           ( firstname, lastname, email, password, age),
        )
        session.commit()


def search_user(query: str):
    with sqlite3.connect("db.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE firstname = ?
            """,
            (query,),
        )
        session.commit()
        return cursor.fetchall()




if __name__ == "__main__":
    result = search_user("Sanya")
    print(result)