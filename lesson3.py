class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0): # Магический метод инициализации объекта
        print("Вызов __init__ - инициализатор")
        self.x = x
        self.y = y

    def __del__(self): # Магический метод Фрагментации объекта
        print(f"Удаление экземпляра {str(self)}")

    def set_cords(self, x, y):
        self.x = x
        self.y = y

    def get_cords(self):
        return self.x, self.y


# Объект класса
pt = Point(1, 2)

print(pt.__dict__)

