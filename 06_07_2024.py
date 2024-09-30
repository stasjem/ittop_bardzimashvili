

class Homer:
    def __init__(self, name):
        self.name = name

class Daughter(Homer):
    pass

daughter1 = Daughter("Lisa")


print(daughter1.name)

class Shape:
    def calculate_area(self):
       pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        import math
        return math.pi * (self.radius ** 2)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height


rectangle = Rectangle(5, 10)
circle = Circle(7)
triangle = Triangle(6, 8)

print(rectangle.calculate_area())
print(circle.calculate_area())
print(triangle.calculate_area())

class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Bird(Animal):
    def make_sound(self):
        return "Tweet"


dog = Dog()
cat = Cat()
bird = Bird()

print(dog.make_sound())
print(cat.make_sound())
print(bird.make_sound())
