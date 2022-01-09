"""
Создать модель пользователя, атрибуты - id, email и модель товара, атрибуты - id, название, цена.
Создать модель покупок, атрибуты - id, ссылка на пользователя (Foreign key), ссылка на товар (Foreign key), количество и
дата покупки.
Добавить функции создания пользователя, товара и покупки.
Добавить функцию вывода всех товаров, купленных определенным пользователем.
Создать программу с пользовательским интерфейсом позволяющим выбирать определенную функцию и вводить необходимые данные.
"""

from sqlalchemy import create_engine, Integer, String, Column, Numeric, ForeignKey, DateTime
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

DB_USER = "never"
DB_PASSWORD = "never"
DB_NAME = "never"
DB_ECHO = True

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    customer = relationship("Purchase", backref="customers")

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Numeric)
    product = relationship("Purshase", backref="products")

class Purchase(Base):
    __tablename__ = "purshase"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    amount = Column(Integer)
    date_of_purchase = Column(DateTime(), default=datetime.now)


def create_customer(email: str):
    customer = Customer(email=email)
    session.add(customer)
    session.commit()
    return print("")

def create_product(product_name: str, price: int):
    product = Product(name=product_name, price=price)
    session.add(product)
    session.commit()
    return print("")




if __name__ == "__main__":

    engine = create_engine(
       f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )

    if not database_exists(engine.url):

        create_database(engine.url)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

