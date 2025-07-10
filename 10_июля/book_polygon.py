from book_lib import *

book = Book("Язык C++", "Бьярн Страупструп")

print(f'{book.get_title(), book.get_author()}')  # можно в {} сразу несколько переменных!


def shape_info(shape):
    print(f'Площадь: {shape.area()}\nПериметр: {shape.perimetr()}')


s = Square(20)
shape_info(s)
c = Circle(10)
shape_info(c)
# такова дхарма полиморфизма!
# print(dir(s))
# print(dir(c))

# ДЗ "утиная типизация" чо такое воще?
# даже если переопределённый метод будет 'pass' — тот просто вернёт 'None'

r = Rectangle(10, 15)
shape_info(r)


def smart_shape_info(shape):
    print(shape.get_name())
    shape_info(shape)


sc = SmartCircle(10)
smart_shape_info(sc)
smart_shape_info(SmartSquare(20))
smart_shape_info(SmartRectangle(16, 9))

shape_class_info(s)
shape_class_info(c)
shape_class_info(r)

people = [
    Person('Alex', 27),
    Student('Max', 'Herzen'),
    Employee('Rex', 'Hastinapura')
]

for person in people:
    if isinstance(person, Student):
        print(person.get_university())  # несуществующий метод не вызовет ошибки!
    elif isinstance(person, Employee):
        print(person.get_company())
    else:
        print(person.get_name())

LST = list(range(1, 15))  # нельзя менять!
s = Selector(LST)
print(s.get_odds())
print(s.get_evens())

stat = Stat(LST)
print(stat.get_min())
print(stat.get_max())
print(stat.get_avr())

stat = Stat([3, 4.5, 7])
print(stat.get_min())
print(stat.get_max())
print(stat.get_avr())

stat = Stat([3.0, 7])
print(stat.get_min())
print(stat.get_max())
print(stat.get_avr())

p = Point()
print(p)
print(p.__str__())

pp = [Point(), Point()]  # __str__ не пашет, здесь пашет __repr__!
print(pp)

p1 = Point(5, 3)
p2 = Point(4, 12)
print(p1 - p2)
print(p1.get_distance_to(p2))

mt = MyTime(23, 9)
mt2 = MyTime(7, 53)
print(mt)
print(mt2)
print(mt + mt2)

qf = QuadraticFunction(1, 2, 3)
print(qf(2))
