"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark.
Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы объекта и
вывести на экран все его атрибуты.
"""


class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age


    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"run {self.name}")

    def bark(self):
        print(f"bark {self.name}")


    def change_name(self, name):
        self.name = name


if __name__ == "__main__":
    dog_bob = Dog(100, 100, "Bob", 10)
    cat_sam = Cat(20, 40, "Sam", 5)
    dog_bob.jump()
    dog_bob.run()
    dog_bob.bark()
    dog_bob.change_name("William")
    print(dog_bob.name)
    print(dog_bob.height)
    print(dog_bob.weight)
    print(dog_bob.age)
    dog_bob.bark()