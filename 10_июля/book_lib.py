from math import pi, hypot
from statistics import mean


class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimetr(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2


class Square:
    def __init__(self, side):
        self.side = side

    def perimetr(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def perimetr(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class SmartCircle:
    def __init__(self, radius):
        self.radius = radius
        self._name = "круг"

    def perimetr(self):
        return round(2 * pi * self.radius, 2)

    def area(self):
        return round(pi * self.radius ** 2, 2)

    def get_name(self) -> str:
        print(self._name)
        return self._name


class SmartSquare:
    def __init__(self, side):
        self.side = side
        self._name = "квадрат"

    def perimetr(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def get_name(self):
        return self._name


class SmartRectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self._name = "прямоугольник"

    def perimetr(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def get_name(self):
        return self._name


r, c, s = "прямоугольник", "круг", "квадрат"


def shape_class_info(shape: object):
    if isinstance(shape, Circle):
        fig = c
    elif isinstance(shape, Rectangle):
        fig = r
    elif isinstance(shape, Square):
        fig = s
    print(f'Площадь {fig}а: {shape.area()}, Периметр {shape.perimetr()}')


class Person:
    def __init__(self, name='Homo', age=1):
        self._name = name
        self._age = age

    def person_info(self):
        print(f'чел с именем {self._name} и возрастом {self._age}')

    def set_name(self, new_name):  # это сеттер
        if new_name:
            self._name = new_name
        else:
            print("не допускаются пустые имена")

    def set_age(self, new_age):
        if 0 < new_age < 150:
            self._age = new_age
        else:
            print(new_age, "не допустимое значение возраста")

    # а вот и геттеры
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age


class Student:
    def __init__(self, name, university):
        self.name = name
        self.university = university

    def get_university(self):
        return self.university


class Employee:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def get_company(self):
        return self.company


class Selector:
    def __init__(self, args: list[int]):
        self._args = args[:]  # чисто для гарантии, что скопировался, а не сослался

    def get_odds(self) -> list[int]:
        return list(filter(lambda n: n % 2 != 0, self._args))

    def get_evens(self) -> list[int]:
        return [n for n in self._args if not n % 2]  # 0 → False, != 0 → True


class Stat:
    def __init__(self, args: list[int]):
        self._args = args[:]
        self._not_integers = all(map(lambda n: isinstance(n, int), self._args))
        # если хоть одно число не целое, методы должны None возвращать

    def get_min(self):
        if self._not_integers:
            return None
        return min(self._args)

    def get_max(self):
        if self._not_integers:
            return None
        return max(self._args)

    def get_avr(self):
        if self._not_integers:
            return None
        return mean(self._args)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'<Точка: {self.x, self.y}>'

    def __repr__(self):
        return f'<Точка: {self.x, self.y}>'

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)  # а можно и абсолютную разницу и т.д. что душе угодно

    def get_distance_to(self, other):
        return hypot((self.x - other.x), (self.y - other.y))


class MyTime:
    def __init__(self, minutes, seconds):
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.minutes:02}:{self.seconds:02}'

    def __add__(self, other):
        m = self.minutes + other.minutes + (self.seconds + other.seconds) // 60
        s = (self.seconds + other.seconds) % 60
        return MyTime(m, s)


class QuadraticFunction:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x):  # y = ax^2 + bx + c
        return self.a * x ** 2 + self.b * x + self.c
