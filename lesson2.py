class Point:
    color = 'red'

    circle = 2

    def set_cords(self, x, y):
        self.x = x
        self.y = y

    def get_cords(self):
        return self.x, self.y


pt = Point()
pt.set_cords(1, 2)
f = getattr(pt, 'get_cords')
print(f())