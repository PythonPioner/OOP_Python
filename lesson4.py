class Point:
    def __new__(cls, *args, **kwargs):
        """
        Магический метод __new__
        cls ссылается на class
        """
        print(f"Вызов __new__  для {str(cls)}")
        # возврощаем ссылку в объект класса
        return super().__new__(cls)


    def __init__(self, x=0, y=0):
        """
        Магический метод __init__
        self ссылается на объект(экзэмпляр)
        """
        print(f"Вызовт __init__ для {str(self)}")
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt)


class DataBase:
    __instance = None

    # Magical method __new__ - Работает до создания объекта класса
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    # Magical method __del__ - Работает после удаления объекта в финале
    # если действий с объектом не происходит
    def __del__(self):
        DataBase.__instance = None
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'соеденение с БД {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('закрытие соединения с БД')

    def read(self):
        print('Данные из БД')

    def write(self, data):
        print(f'Запись в БД {data}')


