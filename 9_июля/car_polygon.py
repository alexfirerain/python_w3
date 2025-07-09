from car_lib import Car
from clicker import Separator
from sorter import Sorter

car = Car("Иж", "Сатурн", "красный")
car.start_engine()  # или car.start_entine = True, но это не по-энкапсуляторски
car.drive_to("город")

# "преодолеть барьер секретаря"
# классы можно КамелКейсом! снейк в именах классов не принят

car1 = Car()
car2 = Car(model="Юпитер")
print(Car.get_count())

autopark = [car, car2, car1]

print(dir(car))

for c in autopark:
    print(f'automobile {c.get_brand()} {c.get_model()}, {c.get_color()}')

N = 5
separator = Separator()
for _ in range(N):
    separator.add_num(int(input("Введи число: ")))

print("нечётные:", separator.get_odds())
print("чётные:", separator.get_evens())

s = Sorter()
for _ in range(N):
    s.add_word()

print(s.result())

# Д/З
# как сделать конструктор полиморфным? за счёт параметров по умолчанию
# иначе — распознав тип объекта
class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_left(self, weight):
        pass
    def add_right(self, weight):
        pass

    def result(self) -> str:
        # состояние весов в виде строки: "правая чаша перевесила" / "левая чаша перевесила" / "весы в равновесии"
        pass
