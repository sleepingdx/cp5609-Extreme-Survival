import math


class Vector:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.z - other.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.z * scalar)

    def __str__(self):
        return f"({self.x}, {self.z})"

    def normalize(self):
        magnitude = math.sqrt(self.x ** 2 + self.z ** 2)
        if magnitude != 0:
            self.x /= magnitude
            self.z /= magnitude
