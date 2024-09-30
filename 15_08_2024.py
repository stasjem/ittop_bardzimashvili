
class Singleton:
    _instance = None  # Здесь будет храниться единственный экземпляр

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Этот класс является синглтоном! Используйте метод get_instance() для получения экземпляра.")
        else:
            Singleton._instance = self

# Примеры использования:
singleton1 = Singleton.get_instance()
singleton2 = Singleton.get_instance()

print(singleton1 == singleton2)  # Выведет True, так как это один и тот же экземпляр


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")


factory = AnimalFactory()

dog = factory.create_animal("dog")
cat = factory.create_animal("cat")

print(dog.speak())
print(cat.speak())

class Observer:
    def update(self, message: str):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

# Пример конкретного наблюдателя:
class ConcreteObserver(Observer):
    def update(self, message: str):
        print(f"Observer получил сообщение: {message}")

# Примеры использования:
subject = Subject()

observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.attach(observer1)
subject.attach(observer2)

subject.notify("Изменение состояния")  # Оба наблюдателя получат сообщение

subject.detach(observer1)
subject.notify("Новое изменение состояния")  # Только observer2 получит сообщение
