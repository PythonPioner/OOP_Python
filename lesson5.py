class Vector:
    # Class Attribute
    MIN_CORD = 0
    MAX_CORD = 100

    @classmethod
    # cls - link to Vector class
    def validate(cls, arg):
        return cls.MIN_CORD <= arg <= cls.MAX_CORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x, self.y))

    # method on class Vector
    def get_cord(self):
        return self.x, self.y

    # Static method
    @staticmethod
    def norm2(x, y):
        return x*x + y*y


v = Vector(1, 20)
print(Vector.norm2(10, 20))

