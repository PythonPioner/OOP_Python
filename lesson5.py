class Vector:
    # Class Attribute
    MIN_CORD = 0
    MAX_CORD = 100

    @classmethod
    # cls - link to Vector class
    def validate(cls, arg):
        return cls.MIN_CORD <= arg <= cls.MAX_CORD

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # method on class Vector
    def get_cord(self):
        return self.x, self.y


v = Vector(1, 2)
res = Vector.get_cord(v)
print(res)
