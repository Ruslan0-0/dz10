class Soda:
    def __init__(self, flavor=None):
        self.flavor = flavor

    def __str__(self):
        if self.flavor:
            return (f'У вас газировка с {self.flavor} вкусом')
        else:
            return 'У вас обычная газировка'


soda1 = Soda("клубничным")
print(soda1)
soda2 = Soda()
print(soda2)


class Calculator:
    def addition (self, num1, num2):
        result = num1 + num2
        print(f'result addition: {result}')

    def subtraction (self, num1, num2):
        result = num1 - num2
        print(f"result subtraction: {result}")

    def multiplaction (self, num1, num2):
        result = num1 * num2
        print(f"result multiplaction: {result}")

    def division (self, num1, num2):
        if num2 != 0:
            result = num1 / num2
            print (f'result division: {result}')
        else:
            print ("You can't divide by zero")

calc = Calculator()
calc.addition(5, 2)
calc.subtraction(5, 2)
calc.multiplaction(5, 2)
calc.division(5, 2)


class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start_engine (self):
        print("Engine start")

    def stop_engine (self):
        print("Engine stop")

    def set_color(self, color):
        self.color = color

    def set_type(self, type):
        self.type = type

    def set_year(self, year):
        self.year = year

car = Car("blue", "sedan", 2022)
car.start_engine()

car.stop_engine()

car.set_color("black")
car.set_type("universal")
car.set_year(2001)

print(car.color)
print(car.type)
print(car.year)


import math


class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.center = (x, y, z)

    def get_volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

    def get_square(self):
        return 4 * math.pi * self.radius ** 2

    def get_radius(self):
        return self.radius

    def get_center(self):
        return self.center

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.center = (x, y, z)

    def is_point_inside(self, x, y, z):
        distance = math.sqrt((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2 + (z - self.center[2]) ** 2)
        return distance <= self.radius


sphere = Sphere(2, 1, 2, 3)
print(sphere.get_radius())

print(sphere.get_center())

sphere.set_radius(3)
print(sphere.get_radius())

print(sphere.is_point_inside(4, 5, 6))

print(sphere.get_volume())
print(sphere.get_square())

class SuperStr(str):
    def rep(self, s):
        if s == "":
            return False
        count = len(self) // len(s)
        return self == s * count
    def is_polindrom(self):
        return self.lower() == self.lower()[::-1]

s = SuperStr("ababab")
print(s.rep("ab"))
s = SuperStr("abcba")
print(s.is_polindrom())
