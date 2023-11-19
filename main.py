import time
class Point:
    "Test Point"
    # Атрибуты класса --> есть у каждого объекта класса
    name = 'Test Name Class'
    age = 'Test age Class'

    def __init__(self):
        self.name = None

print(time.__doc__)
print(hasattr(Point, 'name'))
delattr(Point, 'name')
print(Point.__dict__)
print(Point.__doc__)
# Объект класса -->
a = Point()
# Изменяем атрибут объекта класса + инициализация атрибута в объекте -->
a.name = 'qwerty'
print(a.name, a.age, a.__dict__)
print(type(a))
# Добовляем атрибут объекту класса 1
setattr(a, 'test12', 12)
# Добовляем атрибут объекту класса 2
a.test24 = 24
print(a.__dict__)
