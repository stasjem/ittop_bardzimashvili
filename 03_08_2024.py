
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True


singleton1 = Singleton("First Instance")
print(singleton1.value)

singleton2 = Singleton("Second Instance")
print(singleton2.value)


print(singleton1 is singleton2)


print(id(singleton1))
print(id(singleton2))


from abc import ABC, abstractmethod

# Абстрактный продукт A (например, Button)
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

# Абстрактный продукт B (например, Checkbox)
class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

# Конкретный продукт A1 (WindowsButton)
class WindowsButton(Button):
    def click(self):
        return "Windows Button Clicked"

# Конкретный продукт A2 (MacButton)
class MacButton(Button):
    def click(self):
        return "Mac Button Clicked"

# Конкретный продукт B1 (WindowsCheckbox)
class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows Checkbox Checked"

# Конкретный продукт B2 (MacCheckbox)
class MacCheckbox(Checkbox):
    def check(self):
        return "Mac Checkbox Checked"
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Конкретная фабрика для macOS
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()

    print(button.click())
    print(checkbox.check())

if __name__ == "__main__":
    print("Testing client code with WindowsFactory:")
    client_code(WindowsFactory())

    print("\nTesting client code with MacFactory:")
    client_code(MacFactory())
