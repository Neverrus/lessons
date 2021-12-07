"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
"""



class Cat:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age


    def jump(self):
        print(f"Jump {self.name}")

    def run(self):
        print(f"run {self.name}")

    def meow(self):
        print(f"meow {self.name}")


if __name__ == "__main__":
    cat_sam = Cat(20, 40, "Sam", 5)
    cat_sam.meow()