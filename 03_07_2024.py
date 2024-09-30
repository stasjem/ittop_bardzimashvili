

class Person:
    pass

id_1 = Person()

setattr(id_1, "name", "Vasya")

setattr(id_1, "name", "Masha")

print(id_1.name)

class Person:
    setup = ['имя ', 'Годиков', 'работа', 'Учится ли?']

id_1 = Person()
for attribute in id_1.setup:
    value = input(f"Введите значение для {attribute}: ")
    setattr(id_1, attribute, value)


for attribute in id_1.setup:
    print(f"{attribute}: {getattr(id_1, attribute)}")

class Person:
    pass


id_1 = Person()


setattr(id_1, "dance", "Hip Hop")
setattr(id_1, "draw", "Sketching")
setattr(id_1, "sing", "Opera")


attributes = ["dance", "draw", "sing"]


for attr in attributes:
    print(getattr(id_1, attr))
