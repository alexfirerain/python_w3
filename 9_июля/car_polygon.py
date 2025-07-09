from car_lib import Car

car = Car("Иж", "Сатурн", "красный")
car.start_engine()  # или car.start_entine = True, но это не по-энкапсуляторски
car.drive_to("город")

# "преодолеть барьер секретаря"
# классы можно КамелКейсом! снейк в именах классов не принят

car1 = Car()
car2 = Car()
print(Car.get_count())