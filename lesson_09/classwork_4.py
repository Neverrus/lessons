"""
Создать общий класс Animal, содержащий все общие методы классов Dog и Cat.
Унаследовать Dog и Cat от класса Animal и Удалить в дочерних классах те методы, которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы.
"""

class Animal:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age


    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"run {self.name}")

    def change_name(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(f"bark {self.name}")

class Cat(Animal):
    def meow(self):
        print(f"meow {self.name}")

if __name__ == "__main__":
    cat_sam = Cat(20, 40, "Sam", 5)
    dog_bob = Dog(100, 100, "Bob", 10)

    print(dog_bob.name)
    dog_bob.jump()
    dog_bob.run()
    dog_bob.bark()
    print(dog_bob.height)
    print(dog_bob.weight)
    print(dog_bob.age)

    print(cat_sam.name)
    cat_sam.jump()
    cat_sam.run()
    cat_sam.meow()
    print(cat_sam.height)
    print(cat_sam.weight)
    print(cat_sam.age)